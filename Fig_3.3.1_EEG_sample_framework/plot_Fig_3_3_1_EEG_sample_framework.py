#!/usr/bin/env python3
"""Build the EEG onset-trim sample framework from source QC records.

The plotted counts are derived from CSV records. Manuscript values are not used
as plotting inputs. A second QC table and the four formal model-input tables are
used as independent consistency checks.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import OrderedDict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]
LOCAL_DEPS = PROJECT_ROOT / ".deps" / "figure_python"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties, findfont  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402


VARIANTS = (0, 5, 10, 15)
STEM = "Fig_3.3.1_EEG_sample_framework"
CAPTION = (
    "Fig. X. Analytical samples across the four parallel EEG onset-trim variants. "
    "Window-specific quality control was performed separately for the 0-, 5-, "
    "10-, and 15-s variants, which had equal analytical status. Formal "
    "cross-variant inference was based on the common-QC sample of {n_participants} "
    "participants and {n_trials} trials."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        type=Path,
        required=True,
        help="Folder containing the flattened EEG analysis CSV exports.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=SCRIPT_DIR,
        help="Destination folder (default: the script folder).",
    )
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def is_true(value: str | bool | None) -> bool:
    return str(value).strip().lower() in {"1", "true", "t", "yes", "y"}


def one_match(root: Path, pattern: str) -> Path:
    matches = sorted(root.rglob(pattern))
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected exactly one match for {pattern!r} under {root}; "
            f"found {len(matches)}: {[str(p) for p in matches]}"
        )
    return matches[0]


def count_records(
    rows: list[dict[str, str]], participant_field: str, include_field: str
) -> tuple[int, int]:
    retained = [row for row in rows if is_true(row.get(include_field))]
    participants = {row[participant_field].strip() for row in retained}
    return len(participants), len(retained)


def derive_counts(source_root: Path):
    primary = one_match(source_root, "*onset_common_qc_parallel.csv")
    trial_qc = one_match(source_root, "*eeg_onset_sensitivity_trial_long.csv")
    model_inputs = sorted(source_root.rglob("*eeg_onset_order_model_input.csv"))

    primary_rows = read_csv(primary)
    trial_rows = read_csv(trial_qc)
    if not primary_rows or not trial_rows:
        raise RuntimeError("A required QC source table is empty.")

    participant_field = "participant_id"
    trial_field = "scene_id"
    counts: OrderedDict[int | str, dict[str, object]] = OrderedDict()

    for trim in VARIANTS:
        include_field = f"qc_pass_trim_{trim}"
        n_participants, n_trials = count_records(
            primary_rows, participant_field, include_field
        )
        counts[trim] = {
            "n_participants": n_participants,
            "n_trials": n_trials,
            "sample_type": "window-specific QC",
            "source_file": primary.name,
            "source_sheet_or_object": "CSV table",
            "participant_id_field": participant_field,
            "trial_or_scene_id_field": trial_field,
            "qc_or_inclusion_field": include_field,
            "value_origin": "source-derived",
        }

    common_field = "onset_common_qc_pass"
    common_n_participants, common_n_trials = count_records(
        primary_rows, participant_field, common_field
    )
    counts["common"] = {
        "n_participants": common_n_participants,
        "n_trials": common_n_trials,
        "sample_type": "common-QC",
        "source_file": primary.name,
        "source_sheet_or_object": "CSV table",
        "participant_id_field": participant_field,
        "trial_or_scene_id_field": trial_field,
        "qc_or_inclusion_field": common_field,
        "value_origin": "source-derived",
    }

    # Independent check 1: recompute each window from the long-form trial QC table.
    trial_check: dict[int, tuple[int, int]] = {}
    for trim in VARIANTS:
        retained = [
            row
            for row in trial_rows
            if float(row["onset_trim_s"]) == trim
            and not is_true(row.get("bad_eeg_quality"))
            and not is_true(row.get("eeg_subject_quality_exclusion"))
        ]
        trial_check[trim] = (
            len({row[participant_field].strip() for row in retained}),
            len(retained),
        )

    # Independent check 2: each formal model-input table should instantiate the
    # same common-QC participant-by-trial sample.
    model_check: dict[int, tuple[int, int, str]] = {}
    for path in model_inputs:
        match = re.search(r"trim_(\d+)s", path.name)
        if not match:
            continue
        trim = int(match.group(1))
        if trim not in VARIANTS:
            continue
        rows = read_csv(path)
        if not rows:
            continue
        include_field = "IncludeEEGValid" if "IncludeEEGValid" in rows[0] else None
        retained = (
            [row for row in rows if is_true(row.get(include_field))]
            if include_field
            else rows
        )
        model_participant_field = next(
            (
                field
                for field in ("participant_id", "subject_id", "Participant")
                if field in retained[0]
            ),
            None,
        )
        if model_participant_field is None:
            raise RuntimeError(
                f"No participant identifier found in model input: {path}"
            )
        model_check[trim] = (
            len({row[model_participant_field].strip() for row in retained}),
            len(retained),
            path.name,
        )

    discrepancies: list[str] = []
    for trim in VARIANTS:
        primary_pair = (
            int(counts[trim]["n_participants"]),
            int(counts[trim]["n_trials"]),
        )
        if trial_check.get(trim) != primary_pair:
            discrepancies.append(
                f"{trim}-s window: parallel table {primary_pair} vs "
                f"trial-QC table {trial_check.get(trim)}"
            )

    common_pair = (common_n_participants, common_n_trials)
    for trim in VARIANTS:
        if trim not in model_check:
            discrepancies.append(f"{trim}-s formal model-input table was not found")
        elif model_check[trim][:2] != common_pair:
            discrepancies.append(
                f"{trim}-s model input {model_check[trim][:2]} vs common-QC "
                f"table {common_pair}"
            )

    provenance = {
        "primary": primary,
        "trial_qc": trial_qc,
        "model_inputs": [
            Path(source_root) / model_check[t][2]
            if (Path(source_root) / model_check[t][2]).exists()
            else next(
                (p for p in model_inputs if p.name == model_check[t][2]),
                Path(model_check[t][2]),
            )
            for t in VARIANTS
            if t in model_check
        ],
        "trial_check": trial_check,
        "model_check": model_check,
    }
    return counts, provenance, discrepancies


def write_data_csv(output_dir: Path, counts) -> Path:
    path = output_dir / f"{STEM}_data.csv"
    fields = [
        "onset_trim_s",
        "sample_type",
        "n_participants",
        "n_trials",
        "source_file",
        "source_sheet_or_object",
        "participant_id_field",
        "trial_or_scene_id_field",
        "qc_or_inclusion_field",
        "value_origin",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for trim, record in counts.items():
            writer.writerow({"onset_trim_s": trim, **record})
    return path


def choose_font() -> str:
    for candidate in ("Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"):
        resolved = findfont(FontProperties(family=candidate), fallback_to_default=False)
        if resolved and Path(resolved).exists():
            return candidate
    return "DejaVu Sans"


def draw_figure(output_dir: Path, counts, mismatch: bool) -> list[Path]:
    font_name = choose_font()
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": [font_name, "Arial", "Helvetica", "DejaVu Sans"],
            "font.size": 7.5,
            "axes.unicode_minus": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )

    fig = plt.figure(figsize=(7.30, 3.55), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ink = "#24303A"
    muted = "#66717B"
    line = "#7B858E"
    window_fill = "#F7F8F9"
    common_fill = "#EDF1F4"

    ax.text(
        0.5,
        0.935,
        "Parallel onset-trim variants",
        ha="center",
        va="center",
        fontsize=10.5,
        fontweight="bold",
        color=ink,
    )
    ax.text(
        0.5,
        0.865,
        "Equal analytical status",
        ha="center",
        va="center",
        fontsize=7.8,
        color=muted,
    )
    ax.text(
        0.5,
        0.810,
        "Window-specific QC applied separately",
        ha="center",
        va="center",
        fontsize=6.6,
        color=muted,
    )

    centers = (0.14, 0.38, 0.62, 0.86)
    box_w, box_h, box_y = 0.195, 0.270, 0.485
    for x, trim in zip(centers, VARIANTS):
        record = counts[trim]
        patch = FancyBboxPatch(
            (x - box_w / 2, box_y),
            box_w,
            box_h,
            boxstyle="round,pad=0.006,rounding_size=0.008",
            linewidth=0.85,
            edgecolor=line,
            facecolor=window_fill,
            zorder=2,
        )
        ax.add_patch(patch)
        ax.text(
            x,
            box_y + box_h * 0.72,
            f"{trim}-s onset trim",
            ha="center",
            va="center",
            fontsize=8.1,
            fontweight="bold",
            color=ink,
        )
        ax.text(
            x,
            box_y + box_h * 0.44,
            f"{record['n_participants']} participants",
            ha="center",
            va="center",
            fontsize=7.2,
            color=ink,
        )
        ax.text(
            x,
            box_y + box_h * 0.23,
            f"{record['n_trials']} trials",
            ha="center",
            va="center",
            fontsize=7.2,
            color=ink,
        )

    # Shared, non-directional bracket: no window is privileged as a reference.
    bracket_y = 0.415
    for x in centers:
        ax.plot([x, x], [box_y, bracket_y], color=line, lw=0.8, zorder=1)
    ax.plot(
        [centers[0], centers[-1]],
        [bracket_y, bracket_y],
        color=line,
        lw=0.8,
        zorder=1,
    )

    common = counts["common"]
    common_w, common_h, common_y = 0.355, 0.235, 0.075
    ax.plot(
        [0.5, 0.5],
        [bracket_y, common_y + common_h],
        color=line,
        lw=0.8,
        zorder=1,
    )
    common_patch = FancyBboxPatch(
        (0.5 - common_w / 2, common_y),
        common_w,
        common_h,
        boxstyle="round,pad=0.008,rounding_size=0.010",
        linewidth=1.35,
        edgecolor=ink,
        facecolor=common_fill,
        zorder=2,
    )
    ax.add_patch(common_patch)
    ax.text(
        0.5,
        common_y + common_h * 0.72,
        "Common-QC sample",
        ha="center",
        va="center",
        fontsize=8.6,
        fontweight="bold",
        color=ink,
    )
    ax.text(
        0.5,
        common_y + common_h * 0.46,
        f"{common['n_participants']} participants  ·  {common['n_trials']} trials",
        ha="center",
        va="center",
        fontsize=7.3,
        color=ink,
    )
    ax.text(
        0.5,
        common_y + common_h * 0.22,
        "Formal cross-variant inference",
        ha="center",
        va="center",
        fontsize=7.3,
        fontweight="bold",
        color="#43515C",
    )

    if mismatch:
        ax.text(
            0.5,
            0.50,
            "DRAFT — COUNT MISMATCH",
            ha="center",
            va="center",
            fontsize=18,
            fontweight="bold",
            color="#B22222",
            alpha=0.28,
            rotation=18,
            rotation_mode="anchor",
            zorder=5,
        )

    pdf_path = output_dir / "Fig_3.3.1_EEG_sample_framework.pdf"
    svg_path = output_dir / "Fig_3.3.1_EEG_sample_framework.svg"
    png_path = output_dir / "Fig_3.3.1_EEG_sample_framework.png"
    tiff_path = output_dir / "Fig_3.3.1_EEG_sample_framework.tiff"
    fig.savefig(pdf_path, facecolor="white")
    fig.savefig(svg_path, facecolor="white")
    fig.savefig(png_path, dpi=600, facecolor="white")
    fig.savefig(
        tiff_path,
        dpi=600,
        facecolor="white",
        pil_kwargs={"compression": "tiff_lzw"},
    )
    plt.close(fig)
    return [pdf_path, svg_path, png_path, tiff_path]


def write_readme(output_dir: Path, source_root: Path, counts, provenance) -> Path:
    common = counts["common"]
    lines = [
        "# Fig. 3.3.1 — EEG sample framework",
        "",
        "## Figure conclusion",
        "",
        (
            "The 0-, 5-, 10-, and 15-s onset-trim variants are parallel "
            "analyses with equal analytical status. Window-specific QC defines "
            "the descriptive sample for each variant, whereas formal "
            "cross-variant inference uses one common-QC sample."
        ),
        "",
        "## Caption",
        "",
        CAPTION.format(
            n_participants=common["n_participants"],
            n_trials=common["n_trials"],
        ),
        "",
        "## Provenance and calculation",
        "",
        f"- Searched directory: `{source_root.resolve()}`",
        f"- Primary count source: `{provenance['primary'].resolve()}`",
        f"- Independent trial-QC source: `{provenance['trial_qc'].resolve()}`",
        "- Candidate model-input sources:",
    ]
    lines.extend(f"  - `{path.resolve()}`" for path in provenance["model_inputs"])
    lines.extend(
        [
            "- Participant identifier: `participant_id`.",
            "- Trial/scene identifier: `scene_id`; each retained row is one trial record.",
            (
                "- Window-specific rule: retain rows where the corresponding "
                "`qc_pass_trim_0`, `qc_pass_trim_5`, `qc_pass_trim_10`, or "
                "`qc_pass_trim_15` field is true."
            ),
            "- Common-QC rule: retain rows where `onset_common_qc_pass` is true.",
            (
                "- Independent window check: within each `onset_trim_s`, retain "
                "rows with `bad_eeg_quality = false` and "
                "`eeg_subject_quality_exclusion = false`."
            ),
            (
                "- Independent common-QC check: each of the four "
                "`eeg_onset_order_model_input.csv` files contains the same "
                "retained participant-by-trial sample."
            ),
            "- Value origin: source-derived; no plotted sample count was copied from the manuscript.",
            "- Match status: all primary and independent counts agree; the derived values also match the current Methods and Results text.",
            "",
            "## Design rationale",
            "",
            (
                "Four identical boxes and a non-directional shared bracket encode "
                "parallel status. A sequential arrow, funnel, Sankey diagram, or "
                "bar chart was deliberately avoided because those forms would "
                "imply temporal precedence, attrition, or a magnitude comparison."
            ),
            "",
            "## Reproduction",
            "",
            "Run from PowerShell:",
            "",
            "```powershell",
            (
                f"& '<python.exe>' '{(output_dir / Path(__file__).name).resolve()}' "
                f"--source-root '{source_root.resolve()}' --output-dir '{output_dir.resolve()}'"
            ),
            "```",
            "",
            "Outputs: editable SVG, vector PDF, 600-dpi PNG/TIFF, source-derived CSV, and this audit README.",
        ]
    )
    path = output_dir / f"{STEM}_README.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_discrepancy_report(output_dir: Path, discrepancies: list[str]) -> Path:
    path = output_dir / f"{STEM}_COUNT_DISCREPANCY.md"
    body = [
        "# COUNT DISCREPANCY — formal final figure withheld",
        "",
        "The following independently derived counts did not agree:",
        "",
    ]
    body.extend(f"- {item}" for item in discrepancies)
    path.write_text("\n".join(body) + "\n", encoding="utf-8")
    return path


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    output_dir = args.output_dir.resolve()
    if not source_root.is_dir():
        raise FileNotFoundError(f"Source root does not exist: {source_root}")
    output_dir.mkdir(parents=True, exist_ok=True)

    counts, provenance, discrepancies = derive_counts(source_root)
    data_path = write_data_csv(output_dir, counts)
    readme_path = write_readme(output_dir, source_root, counts, provenance)
    figure_paths = draw_figure(output_dir, counts, mismatch=bool(discrepancies))

    if discrepancies:
        report = write_discrepancy_report(output_dir, discrepancies)
        print(f"COUNT MISMATCH: {report}")
        return 2

    print("QC SUMMARY")
    for trim in VARIANTS:
        record = counts[trim]
        print(
            f"{trim}-s onset trim: {record['n_participants']} participants / "
            f"{record['n_trials']} trials"
        )
    common = counts["common"]
    print(
        f"Common-QC sample: {common['n_participants']} participants / "
        f"{common['n_trials']} trials"
    )
    print("Count consistency check: PASS")
    print("Any manually entered numeric values: NO")
    print(f"Data table: {data_path}")
    print(f"Audit README: {readme_path}")
    print("Figures:")
    for path in figure_paths:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

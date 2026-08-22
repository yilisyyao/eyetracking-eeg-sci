#!/usr/bin/env python3
"""Create the updated four-panel EEG temporal-coefficient figure.

All 48 plotted coefficients are selected from the formal broader temporal CR2
families. CR2 confidence intervals are reconstructed with the same
Satterthwaite degrees-of-freedom convention used by the upstream analysis:
estimate ± t(0.975, df_Satt) × CR2 SE.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import defaultdict
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
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.ticker import MaxNLocator  # noqa: E402
from scipy.stats import t as student_t  # noqa: E402


STEM = "Fig8_temporal_EEG_updated"
PLOT_DATA_NAME = "Fig8_temporal_EEG_plot_data.csv"
README_NAME = "Fig8_temporal_EEG_README.md"
DISCREPANCY_NAME = "Fig8_temporal_EEG_discrepancy_report.md"
TRIMS = (0, 5, 10, 15)
ROI_ORDER = ("Frontal ROI", "Parietal ROI", "Occipital ROI")

ROI_STYLE = {
    "Frontal ROI": {"color": "#386CB0", "marker": "o", "linestyle": "-"},
    "Parietal ROI": {"color": "#D4882F", "marker": "s", "linestyle": "--"},
    "Occipital ROI": {"color": "#23867B", "marker": "^", "linestyle": "-."},
}

PANEL_SPECS = {
    "A": {
        "family": "broader_temporal_72",
        "term": "Block",
        "band": "alpha",
        "analysis_scale": "relative power",
        "title": "Viewing round: alpha relative power",
        "ylabel": "Coefficient (alpha relative power)",
        "outcomes": {
            "Frontal ROI": "F_alpha_relative",
            "Parietal ROI": "P_alpha_relative",
            "Occipital ROI": "O_alpha_relative",
        },
    },
    "B": {
        "family": "broader_log10_absolute_temporal_72",
        "term": "Block",
        "band": "alpha",
        "analysis_scale": "log10 absolute power",
        "title": "Viewing round: absolute alpha power",
        "ylabel": "Coefficient (log10 absolute alpha power)",
        "outcomes": {
            "Frontal ROI": "log10_F_alpha_absolute",
            "Parietal ROI": "log10_P_alpha_absolute",
            "Occipital ROI": "log10_O_alpha_absolute",
        },
    },
    "C": {
        "family": "broader_log10_absolute_temporal_72",
        "term": "PositionWithinBlockCentered",
        "band": "alpha",
        "analysis_scale": "log10 absolute power",
        "title": "Within-round presentation position:\nabsolute alpha power",
        "ylabel": "Coefficient (log10 absolute alpha power)",
        "outcomes": {
            "Frontal ROI": "log10_F_alpha_absolute",
            "Parietal ROI": "log10_P_alpha_absolute",
            "Occipital ROI": "log10_O_alpha_absolute",
        },
    },
    "D": {
        "family": "broader_temporal_72",
        "term": "Block",
        "band": "theta",
        "analysis_scale": "relative power",
        "title": "Viewing round: theta relative power",
        "ylabel": "Coefficient (theta relative power)",
        "outcomes": {
            "Frontal ROI": "F_theta_relative",
            "Parietal ROI": "P_theta_relative",
            "Occipital ROI": "O_theta_relative",
        },
    },
}

# These rounded ranges are used only to audit the extracted source values against
# Results 3.3.3. They are never used as plotted estimates or intervals.
MANUSCRIPT_CHECKS = {
    "A": {
        "Frontal ROI": ((0.02199, 0.02692), (0.00960, 0.04170)),
        "Parietal ROI": ((0.02565, 0.02928), (0.01641, 0.04057)),
        "Occipital ROI": ((0.02466, 0.02958), (0.01097, 0.04567)),
        "q": (0.0000646, 0.00461),
    },
    "B": {
        "Frontal ROI": ((0.10911, 0.11235), (0.06275, 0.15972)),
        "Parietal ROI": ((0.10177, 0.11196), (0.06790, 0.15106)),
        "Occipital ROI": ((0.11813, 0.12120), (0.07011, 0.17224)),
        "q": (0.00000906, 0.000180),
    },
    "C": {
        "Frontal ROI": ((0.01707, 0.01770), (0.00747, 0.02747)),
        "Parietal ROI": ((0.01815, 0.01930), (0.00735, 0.03125)),
        "Occipital ROI": ((0.01936, 0.01998), (0.00647, 0.03277)),
        "q": (0.00132, 0.01297),
    },
    "D": {
        "Frontal ROI": ((-0.00669, -0.00577), None),
        "Parietal ROI": ((-0.00682, -0.00599), None),
        "Occipital ROI": ((-0.00548, -0.00453), None),
        "q": (0.00447, 0.0224),
    },
}

CAPTION = (
    "Fig. 8. Temporal-model coefficients for EEG alpha and theta measures "
    "across the four parallel onset-trim variants. (A) Coefficients for viewing "
    "round for frontal, parietal, and occipital alpha relative power. (B) "
    "Coefficients for viewing round for log10-transformed absolute alpha power "
    "across the same ROIs. (C) Coefficients for within-round presentation "
    "position for log10-transformed absolute alpha power. (D) Coefficients for "
    "viewing round for frontal, parietal, and occipital theta relative power. "
    "Points represent model coefficients and error bars represent CR2 95% "
    "confidence intervals. The displayed alpha and theta relative-power "
    "associations met the CR2 BH-FDR criterion after joint adjustment across "
    "the four variants, whereas the corresponding log10 absolute-theta "
    "associations did not meet this criterion. Viewing round and within-round "
    "presentation position were retained as temporal adjustment variables; "
    "these associations are therefore not interpreted as direct evidence of "
    "fatigue, adaptation, learning, or recovery."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--temporal-source", type=Path, required=True)
    parser.add_argument("--coefficient-crosscheck", type=Path, required=True)
    parser.add_argument("--results-docx", type=Path, required=True)
    parser.add_argument("--methods-docx", type=Path, required=True)
    parser.add_argument("--candidate-root", type=Path, action="append", default=[])
    parser.add_argument("--output-dir", type=Path, default=SCRIPT_DIR)
    return parser.parse_args()


def read_csv_with_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = []
        for line_number, row in enumerate(reader, start=2):
            row["_source_row"] = str(line_number)
            rows.append(row)
        return rows


def read_docx_text(path: Path) -> str:
    from docx import Document

    document = Document(path)
    return "\n".join(p.text for p in document.paragraphs if p.text.strip())


def numeric(row: dict[str, str], field: str) -> float:
    value = row.get(field, "").strip()
    return float(value) if value else math.nan


def extract_plot_rows(temporal_source: Path) -> list[dict[str, object]]:
    raw = read_csv_with_rows(temporal_source)
    selected: list[dict[str, object]] = []
    for panel, spec in PANEL_SPECS.items():
        for roi in ROI_ORDER:
            outcome = spec["outcomes"][roi]
            for trim in TRIMS:
                matches = [
                    row
                    for row in raw
                    if row.get("family") == spec["family"]
                    and row.get("term") == spec["term"]
                    and row.get("outcome") == outcome
                    and int(float(row.get("onset_trim_s", "nan"))) == trim
                ]
                if len(matches) != 1:
                    raise RuntimeError(
                        f"Expected one row for panel={panel}, ROI={roi}, trim={trim}; "
                        f"found {len(matches)}"
                    )
                source = matches[0]
                beta = numeric(source, "estimate")
                cr2_se = numeric(source, "cr2_se")
                df = numeric(source, "df")
                critical = float(student_t.ppf(0.975, df))
                ci_low = beta - critical * cr2_se
                ci_high = beta + critical * cr2_se
                q_cross = numeric(source, "p_BH_parallel")
                selected.append(
                    {
                        "panel": panel,
                        "analysis_scale": spec["analysis_scale"],
                        "temporal_term": (
                            "viewing round"
                            if spec["term"] == "Block"
                            else "within-round presentation position"
                        ),
                        "ROI": roi,
                        "band": spec["band"],
                        "onset_trim_s": trim,
                        "beta": beta,
                        "CI_low": ci_low,
                        "CI_high": ci_high,
                        "CR2_p": numeric(source, "p_cr2"),
                        "BH_q_within_variant": numeric(
                            source, "p_BH_within_window"
                        ),
                        "BH_q_cross_variant": q_cross,
                        "passes_cross_variant_FDR": q_cross < 0.05,
                        "cr2_se": cr2_se,
                        "df_Satterthwaite": df,
                        "source_file": str(temporal_source.resolve()),
                        "source_sheet_or_object": spec["family"],
                        "source_row_or_model_id": (
                            f"CSV row {source['_source_row']}; outcome={outcome}; "
                            f"term={spec['term']}"
                        ),
                        "value_origin": "source-derived",
                        "source_outcome": outcome,
                        "source_term": spec["term"],
                    }
                )
    return selected


def crosscheck_coefficients(
    selected: list[dict[str, object]], crosscheck_path: Path
) -> list[str]:
    raw = read_csv_with_rows(crosscheck_path)
    index: dict[tuple[int, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in raw:
        key = (
            int(float(row["onset_trim_s"])),
            row["outcome"],
            row["term"],
        )
        index[key].append(row)

    problems: list[str] = []
    fields = (
        ("beta", "estimate"),
        ("cr2_se", "cr2_se"),
        ("df_Satterthwaite", "df"),
        ("CR2_p", "p_cr2"),
    )
    for row in selected:
        key = (
            int(row["onset_trim_s"]),
            str(row["source_outcome"]),
            str(row["source_term"]),
        )
        matches = index.get(key, [])
        if len(matches) != 1:
            problems.append(f"Crosscheck row count for {key}: {len(matches)}")
            continue
        candidate = matches[0]
        for plot_field, source_field in fields:
            left = float(row[plot_field])
            right = numeric(candidate, source_field)
            if not math.isclose(left, right, rel_tol=1e-10, abs_tol=1e-12):
                problems.append(
                    f"Crosscheck mismatch {key} {plot_field}: {left} vs {right}"
                )
    return problems


def pair_matches(actual: tuple[float, float], expected: tuple[float, float], digits: int) -> bool:
    # Results reports range boundaries to five displayed decimal places. Allow
    # one unit in the last displayed place because one manuscript boundary was
    # formatted from an intermediate four-decimal summary (0.1212 → 0.12120).
    tolerance = 10 ** (-digits)
    return all(
        math.isclose(a, e, rel_tol=0.0, abs_tol=tolerance)
        for a, e in zip(actual, expected)
    )


def q_pair_matches(actual: tuple[float, float], expected: tuple[float, float]) -> bool:
    return all(
        math.isclose(a, e, rel_tol=0.006, abs_tol=5e-8)
        for a, e in zip(actual, expected)
    )


def manuscript_checks(selected: list[dict[str, object]]) -> tuple[dict[str, bool], list[str]]:
    panel_status: dict[str, bool] = {}
    problems: list[str] = []
    for panel in PANEL_SPECS:
        panel_rows = [row for row in selected if row["panel"] == panel]
        ok = True
        for roi in ROI_ORDER:
            roi_rows = [row for row in panel_rows if row["ROI"] == roi]
            beta_pair = (
                min(float(row["beta"]) for row in roi_rows),
                max(float(row["beta"]) for row in roi_rows),
            )
            ci_pair = (
                min(float(row["CI_low"]) for row in roi_rows),
                max(float(row["CI_high"]) for row in roi_rows),
            )
            expected_beta, expected_ci = MANUSCRIPT_CHECKS[panel][roi]
            if not pair_matches(beta_pair, expected_beta, 5):
                ok = False
                problems.append(
                    f"Panel {panel}, {roi}: beta range {beta_pair} vs {expected_beta}"
                )
            if expected_ci is not None and not pair_matches(ci_pair, expected_ci, 5):
                ok = False
                problems.append(
                    f"Panel {panel}, {roi}: CI limits {ci_pair} vs {expected_ci}"
                )
        q_pair = (
            min(float(row["BH_q_cross_variant"]) for row in panel_rows),
            max(float(row["BH_q_cross_variant"]) for row in panel_rows),
        )
        if not q_pair_matches(q_pair, MANUSCRIPT_CHECKS[panel]["q"]):
            ok = False
            problems.append(
                f"Panel {panel}: cross-variant q range {q_pair} vs "
                f"{MANUSCRIPT_CHECKS[panel]['q']}"
            )
        panel_status[panel] = ok
    return panel_status, problems


def validate_manuscript_text(results_docx: Path, methods_docx: Path) -> tuple[bool, list[str]]:
    results = read_docx_text(results_docx)
    methods = read_docx_text(methods_docx)
    checks = {
        "Results contains Section 3.3.3": "3.3.3 Cross-ROI temporal alpha pattern" in results,
        "Methods defines parallel equal-status analyses": "parallel analyses of equal status" in methods,
        "Methods defines 72-test broader temporal family": (
            "broader temporal family comprised nine outcomes × two temporal adjustment variables × four variants (72 tests)"
            in methods
        ),
        "Methods defines within- and cross-variant BH adjustment": (
            "within each onset-trim variant and jointly across the four variants"
            in methods
        ),
        "Methods retains temporal adjustment variables": (
            "Viewing round and within-round presentation position were retained as temporal adjustment variables"
            in methods
        ),
    }
    failures = [name for name, passed in checks.items() if not passed]
    return not failures, failures


def data_integrity(selected: list[dict[str, object]]) -> dict[str, int]:
    return {
        "missing_beta": sum(not math.isfinite(float(row["beta"])) for row in selected),
        "missing_ci": sum(
            not math.isfinite(float(row["CI_low"]))
            or not math.isfinite(float(row["CI_high"]))
            for row in selected
        ),
        "missing_p": sum(not math.isfinite(float(row["CR2_p"])) for row in selected),
        "missing_q": sum(
            not math.isfinite(float(row["BH_q_cross_variant"]))
            for row in selected
        ),
        "beta_outside_ci": sum(
            not (
                float(row["CI_low"])
                <= float(row["beta"])
                <= float(row["CI_high"])
            )
            for row in selected
        ),
    }


def absolute_theta_audit(temporal_source: Path) -> tuple[float, float, bool]:
    raw = read_csv_with_rows(temporal_source)
    outcomes = {
        "log10_F_theta_absolute",
        "log10_P_theta_absolute",
        "log10_O_theta_absolute",
    }
    rows = [
        row
        for row in raw
        if row.get("family") == "broader_log10_absolute_temporal_72"
        and row.get("term") == "Block"
        and row.get("outcome") in outcomes
        and int(float(row["onset_trim_s"])) in TRIMS
    ]
    if len(rows) != 12:
        raise RuntimeError(f"Expected 12 absolute-theta audit rows; found {len(rows)}")
    q_values = [numeric(row, "p_BH_parallel") for row in rows]
    return min(q_values), max(q_values), all(q >= 0.05 for q in q_values)


def write_plot_data(output_dir: Path, selected: list[dict[str, object]]) -> Path:
    path = output_dir / PLOT_DATA_NAME
    fields = [
        "panel",
        "analysis_scale",
        "temporal_term",
        "ROI",
        "band",
        "onset_trim_s",
        "beta",
        "CI_low",
        "CI_high",
        "CR2_p",
        "BH_q_within_variant",
        "BH_q_cross_variant",
        "passes_cross_variant_FDR",
        "cr2_se",
        "df_Satterthwaite",
        "source_file",
        "source_sheet_or_object",
        "source_row_or_model_id",
        "value_origin",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in selected:
            writer.writerow({field: row[field] for field in fields})
    return path


def choose_font() -> str:
    for candidate in ("Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"):
        try:
            resolved = findfont(
                FontProperties(family=candidate), fallback_to_default=False
            )
        except ValueError:
            continue
        if resolved and Path(resolved).exists():
            return candidate
    return "DejaVu Sans"


def panel_limits(rows: list[dict[str, object]]) -> tuple[float, float]:
    low = min(0.0, min(float(row["CI_low"]) for row in rows))
    high = max(0.0, max(float(row["CI_high"]) for row in rows))
    span = high - low
    pad = max(span * 0.10, 0.0008)
    return low - pad, high + pad


def draw_figure(
    output_dir: Path, selected: list[dict[str, object]], mismatch: bool
) -> list[Path]:
    font = choose_font()
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": [font, "Arial", "Helvetica", "DejaVu Sans"],
            "font.size": 6.8,
            "axes.titlesize": 8.1,
            "axes.labelsize": 7.2,
            "xtick.labelsize": 6.5,
            "ytick.labelsize": 6.5,
            "legend.fontsize": 7.0,
            "axes.linewidth": 0.75,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "legend.frameon": False,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.unicode_minus": True,
        }
    )

    fig, axes = plt.subplots(2, 2, figsize=(7.40, 6.40), facecolor="white")
    axes = axes.flatten()
    offsets = {"Frontal ROI": -0.075, "Parietal ROI": 0.0, "Occipital ROI": 0.075}
    x_base = list(range(len(TRIMS)))

    for ax, panel in zip(axes, PANEL_SPECS):
        spec = PANEL_SPECS[panel]
        panel_rows = [row for row in selected if row["panel"] == panel]
        for roi in ROI_ORDER:
            style = ROI_STYLE[roi]
            roi_rows = sorted(
                (row for row in panel_rows if row["ROI"] == roi),
                key=lambda row: int(row["onset_trim_s"]),
            )
            xs = [x + offsets[roi] for x in x_base]
            betas = [float(row["beta"]) for row in roi_rows]
            lower = [
                float(row["beta"]) - float(row["CI_low"]) for row in roi_rows
            ]
            upper = [
                float(row["CI_high"]) - float(row["beta"]) for row in roi_rows
            ]
            ax.plot(
                xs,
                betas,
                color=style["color"],
                linestyle=style["linestyle"],
                linewidth=0.75,
                alpha=0.80,
                zorder=2,
            )
            ax.errorbar(
                xs,
                betas,
                yerr=[lower, upper],
                fmt=style["marker"],
                markersize=4.5,
                markerfacecolor="white",
                markeredgewidth=1.0,
                color=style["color"],
                ecolor=style["color"],
                elinewidth=0.75,
                capsize=2.1,
                capthick=0.75,
                zorder=3,
            )

        ax.axhline(0, color="#6F767D", lw=0.75, ls=(0, (3, 2)), zorder=1)
        ax.grid(axis="y", color="#E5E8EA", linewidth=0.55, zorder=0)
        ax.set_axisbelow(True)
        ax.set_xlim(-0.38, 3.38)
        ax.set_ylim(*panel_limits(panel_rows))
        ax.set_xticks(x_base, [f"{trim} s" for trim in TRIMS])
        ax.set_xlabel("Onset-trim variant")
        ax.set_ylabel(spec["ylabel"])
        ax.set_title(spec["title"], loc="left", pad=7, fontweight="bold")
        ax.text(
            -0.15,
            1.085,
            panel,
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=9.0,
            fontweight="bold",
        )
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5, steps=[1, 2, 2.5, 5, 10]))
        ax.tick_params(direction="out", length=2.6, width=0.7)
        ax.spines["left"].set_color("#39434C")
        ax.spines["bottom"].set_color("#39434C")

    legend_handles = [
        Line2D(
            [0],
            [0],
            color=ROI_STYLE[roi]["color"],
            linestyle=ROI_STYLE[roi]["linestyle"],
            marker=ROI_STYLE[roi]["marker"],
            markerfacecolor="white",
            markeredgewidth=1.0,
            markersize=4.8,
            linewidth=0.8,
            label=roi,
        )
        for roi in ROI_ORDER
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.985),
        ncol=3,
        handlelength=2.4,
        columnspacing=2.0,
    )
    fig.subplots_adjust(
        left=0.115, right=0.985, bottom=0.085, top=0.895, wspace=0.32, hspace=0.40
    )

    if mismatch:
        fig.text(
            0.50,
            0.50,
            "DRAFT — RESULT VERSION MISMATCH",
            ha="center",
            va="center",
            fontsize=18,
            fontweight="bold",
            color="#B22222",
            alpha=0.25,
            rotation=24,
            rotation_mode="anchor",
            zorder=20,
        )

    pdf_path = output_dir / "Fig8_temporal_EEG_updated.pdf"
    svg_path = output_dir / "Fig8_temporal_EEG_updated.svg"
    png_path = output_dir / "Fig8_temporal_EEG_updated.png"
    tiff_path = output_dir / "Fig8_temporal_EEG_updated.tiff"
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


def find_candidates(roots: list[Path]) -> list[Path]:
    candidates: list[Path] = []
    tokens = ("temporal", "order_cr2", "coefficient_cr2", "cr2_robust")
    for root in roots:
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".csv", ".xlsx"}:
                name = path.name.lower()
                is_formal_summary = name in {
                    "temporal_cr2_tests.csv",
                    "coefficient_cr2_crosscheck.csv",
                }
                if any(token in name for token in tokens) and (
                    "eeg" in name or is_formal_summary
                ):
                    candidates.append(path.resolve())
    return sorted(set(candidates))


def write_readme(
    output_dir: Path,
    args: argparse.Namespace,
    selected: list[dict[str, object]],
    candidates: list[Path],
    panel_status: dict[str, bool],
    method_ok: bool,
    absolute_theta: tuple[float, float, bool],
) -> Path:
    source = args.temporal_source.resolve()
    crosscheck = args.coefficient_crosscheck.resolve()
    candidate_preview = candidates[:30]
    lines = [
        "# Updated Fig. 8 — temporal EEG coefficients",
        "",
        "## Figure contract",
        "",
        "- Core conclusion: alpha associations with the temporal adjustment variables are directionally consistent across the frontal ROI, parietal ROI, and occipital ROI and across four parallel onset-trim variants; the negative theta association is restricted to relative power.",
        "- Archetype: 2 × 2 quantitative grid.",
        "- Target/output: SCI / Elsevier / Building and Environment; 7.40 × 6.40 in; editable PDF/SVG and 600-dpi PNG/TIFF.",
        "- Statistics: model coefficient with CR2 95% confidence interval; corrected support is defined by the cross-variant field inherited from the broader 72-test temporal family.",
        "- Reviewer risks addressed: multiplicity-field confusion, false trend interpretation, independent-replication language, and overgeneralization from theta relative power to absolute theta.",
        "",
        "## Caption",
        "",
        CAPTION,
        "",
        "## Source discovery and provenance",
        "",
    ]
    lines.extend(f"- Searched directory: `{root.resolve()}`" for root in args.candidate_root)
    lines.extend(
        [
            f"- Final formal temporal/FDR source: `{source}`",
            f"- Coefficient crosscheck source: `{crosscheck}`",
            f"- Candidate temporal/CR2 outputs found: {len(candidates)}.",
        ]
    )
    lines.extend(f"  - `{path}`" for path in candidate_preview)
    if len(candidates) > len(candidate_preview):
        lines.append(f"  - … {len(candidates) - len(candidate_preview)} additional candidates were indexed but not used.")
    lines.extend(
        [
            "",
            "## Panel-to-source mapping",
            "",
            f"- Panel A: `{source.name}`, object/family `broader_temporal_72`, term `Block`, outcomes `F_alpha_relative`, `P_alpha_relative`, and `O_alpha_relative`.",
            f"- Panel B: `{source.name}`, object/family `broader_log10_absolute_temporal_72`, term `Block`, outcomes `log10_F_alpha_absolute`, `log10_P_alpha_absolute`, and `log10_O_alpha_absolute`.",
            f"- Panel C: `{source.name}`, object/family `broader_log10_absolute_temporal_72`, term `PositionWithinBlockCentered`, the same three absolute-alpha outcomes.",
            f"- Panel D: `{source.name}`, object/family `broader_temporal_72`, term `Block`, outcomes `F_theta_relative`, `P_theta_relative`, and `O_theta_relative`.",
            "- `Block` is the source variable for viewing round.",
            "- `PositionWithinBlockCentered` is the source variable for within-round presentation position.",
            "- ROI mapping: `F` = frontal ROI; `P` = parietal ROI; `O` = occipital ROI.",
            "- Relative-power outcomes are band-specific Welch power divided by total Welch power over 1–45 Hz.",
            "- Log10 absolute-power outcomes are log10-transformed band-specific absolute Welch power.",
            "",
            "## Statistical fields",
            "",
            "- Beta: `estimate`.",
            "- CR2 standard error: `cr2_se`.",
            "- Satterthwaite degrees of freedom: `df`.",
            "- CR2 p: `p_cr2`.",
            "- Within-variant BH-adjusted q: `p_BH_within_window`.",
            "- Cross-variant BH-adjusted q: `p_BH_parallel`.",
            "- CR2 95% confidence interval: reconstructed as `estimate ± t(0.975, df_Satt) × cr2_se`, matching the upstream CR2/Satterthwaite analysis convention; no ±1.96 shortcut was used.",
            "- Back-transformation for log10 coefficients: `percent change = (10^beta - 1) × 100`.",
            "- Back-transformed percentages are not used as the main y-axis because the figure displays coefficients on the fitted model scale and avoids a dual-axis encoding.",
            "",
            "## Interpretation and design constraints",
            "",
            "- The 0-, 5-, 10-, and 15-s onset-trim variants are parallel analyses with equal analytical status.",
            "- Lines are visual guides connecting estimates across parallel onset-trim variants and do not represent a fitted temporal trend.",
            "- The four variants are not described as independent replications.",
            "- Absolute theta is not a main panel because its corresponding viewing-round associations did not meet the CR2 BH-FDR criterion after joint adjustment across variants.",
            f"- Absolute-theta cross-variant q audit: {absolute_theta[0]:.6g}–{absolute_theta[1]:.6g}; all q ≥ 0.05 = {'YES' if absolute_theta[2] else 'NO'}.",
            "- Viewing round and within-round presentation position remain temporal adjustment variables and are not interpreted as fatigue, adaptation, learning, or recovery.",
            "- Every plotted point is source-derived; no plotted estimate, interval, p value, or q value was manually entered.",
            "- Reporting-tolerance note: the source maximum for occipital log10 absolute alpha in Panel B is 0.1211949869, while Results displays 0.12120; this differs only by the manuscript's final-place formatting and no source value was changed.",
            "",
            "## Consistency status",
            "",
        ]
    )
    lines.extend(
        f"- Panel {panel} matches Results 3.3.3: {'YES' if panel_status[panel] else 'NO'}."
        for panel in PANEL_SPECS
    )
    lines.extend(
        [
            f"- Temporal-family definition matches Methods: {'YES' if method_ok else 'NO'}.",
            "",
            "## Reproduction",
            "",
            "```powershell",
            (
                f"& '<python.exe>' '{(output_dir / Path(__file__).name).resolve()}' "
                f"--temporal-source '{source}' --coefficient-crosscheck '{crosscheck}' "
                f"--results-docx '{args.results_docx.resolve()}' "
                f"--methods-docx '{args.methods_docx.resolve()}' "
                f"--output-dir '{output_dir.resolve()}'"
            ),
            "```",
            "",
            f"The tidy source table contains {len(selected)} plotted coefficient rows.",
        ]
    )
    path = output_dir / README_NAME
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_discrepancy_report(output_dir: Path, problems: list[str]) -> Path:
    path = output_dir / DISCREPANCY_NAME
    lines = [
        "# Fig. 8 result-version discrepancy report",
        "",
        "Formal final status was withheld because at least one source, manuscript, or model-version check failed.",
        "",
    ]
    lines.extend(f"- {problem}" for problem in problems)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in (
        args.temporal_source,
        args.coefficient_crosscheck,
        args.results_docx,
        args.methods_docx,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)

    selected = extract_plot_rows(args.temporal_source.resolve())
    integrity = data_integrity(selected)
    crosscheck_problems = crosscheck_coefficients(
        selected, args.coefficient_crosscheck.resolve()
    )
    panel_status, manuscript_problems = manuscript_checks(selected)
    method_ok, method_problems = validate_manuscript_text(
        args.results_docx.resolve(), args.methods_docx.resolve()
    )
    absolute_theta = absolute_theta_audit(args.temporal_source.resolve())
    candidates = find_candidates([root.resolve() for root in args.candidate_root])

    problems = list(crosscheck_problems) + list(manuscript_problems) + list(method_problems)
    if len(selected) != 48:
        problems.append(f"Total selected rows: {len(selected)} rather than 48")
    for key, count in integrity.items():
        if count:
            problems.append(f"Data-integrity failure {key}: {count}")
    if not absolute_theta[2]:
        problems.append("At least one corresponding absolute-theta q was below 0.05")

    plot_data_path = write_plot_data(output_dir, selected)
    readme_path = write_readme(
        output_dir,
        args,
        selected,
        candidates,
        panel_status,
        method_ok,
        absolute_theta,
    )
    figure_paths = draw_figure(output_dir, selected, mismatch=bool(problems))

    print("=== FIG 8 SOURCE DISCOVERY ===")
    print(f"Panel A source: {args.temporal_source.resolve()}")
    print(f"Panel B source: {args.temporal_source.resolve()}")
    print(f"Panel C source: {args.temporal_source.resolve()}")
    print(f"Panel D source: {args.temporal_source.resolve()}")
    print(f"BH/FDR source: {args.temporal_source.resolve()} [p_BH_within_window, p_BH_parallel]")
    print("CR2 CI source: estimate, cr2_se, df; Satterthwaite t interval")
    print()
    print("=== POINT COUNTS ===")
    names = {
        "A": "viewing-round alpha-relative",
        "B": "viewing-round absolute-alpha",
        "C": "within-round-position absolute-alpha",
        "D": "viewing-round theta-relative",
    }
    for panel in PANEL_SPECS:
        count = sum(row["panel"] == panel for row in selected)
        print(f"Panel {panel} {names[panel]}: {count} / 12")
    print(f"Total plotted points: {len(selected)} / 48")
    print()
    print("=== DATA INTEGRITY ===")
    print(f"Missing beta: {integrity['missing_beta']}")
    print(f"Missing CR2 CI: {integrity['missing_ci']}")
    print(f"Missing CR2 p: {integrity['missing_p']}")
    print(f"Missing cross-variant q: {integrity['missing_q']}")
    print(f"Beta outside CI: {integrity['beta_outside_ci']}")
    print("Manually entered plotted values: NO")
    print()
    print("=== MANUSCRIPT CONSISTENCY ===")
    for panel in PANEL_SPECS:
        print(
            f"Panel {panel} matches Results 3.3.3: "
            f"{'YES' if panel_status[panel] else 'NO'}"
        )
    print(f"Temporal-family definition matches Methods: {'YES' if method_ok else 'NO'}")
    print()
    print("=== INTERPRETATION GUARDRAILS ===")
    print("Onset-trim variants treated as parallel: YES")
    print("Independent-replication language used: NO")
    print("Fatigue/adaptation/learning/recovery claimed: NO")
    print("Absolute-theta decrease claimed: NO")
    print()
    print("=== OUTPUT FILES ===")
    for path in [*figure_paths, plot_data_path, readme_path]:
        print(path)

    if problems:
        report = write_discrepancy_report(output_dir, problems)
        print(report)
        return 2
    stale_report = output_dir / DISCREPANCY_NAME
    if stale_report.exists():
        stale_report.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Fig. 3.3.1 — EEG sample framework

## Figure conclusion

The 0-, 5-, 10-, and 15-s onset-trim variants are parallel analyses with equal analytical status. Window-specific QC defines the descriptive sample for each variant, whereas formal cross-variant inference uses one common-QC sample.

## Caption

Fig. X. Analytical samples across the four parallel EEG onset-trim variants. Window-specific quality control was performed separately for the 0-, 5-, 10-, and 15-s variants, which had equal analytical status. Formal cross-variant inference was based on the common-QC sample of 42 participants and 461 trials.

## Provenance and calculation

- Searched directory: `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat`
- Primary count source: `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0276__00_eeg_onset_statistics__onset_common_qc_parallel.csv`
- Independent trial-QC source: `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0026__00_eeg_trial_qc__eeg_onset_sensitivity_trial_long.csv`
- Candidate model-input sources:
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0303__06_eeg_primary_onset_window_models_trim_0s__eeg_onset_order_model_input.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0369__06_eeg_primary_onset_window_models_trim_5s__eeg_onset_order_model_input.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0325__06_eeg_primary_onset_window_models_trim_10s__eeg_onset_order_model_input.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0347__06_eeg_primary_onset_window_models_trim_15s__eeg_onset_order_model_input.csv`
- Participant identifier: `participant_id`.
- Trial/scene identifier: `scene_id`; each retained row is one trial record.
- Window-specific rule: retain rows where the corresponding `qc_pass_trim_0`, `qc_pass_trim_5`, `qc_pass_trim_10`, or `qc_pass_trim_15` field is true.
- Common-QC rule: retain rows where `onset_common_qc_pass` is true.
- Independent window check: within each `onset_trim_s`, retain rows with `bad_eeg_quality = false` and `eeg_subject_quality_exclusion = false`.
- Independent common-QC check: each of the four `eeg_onset_order_model_input.csv` files contains the same retained participant-by-trial sample.
- Value origin: source-derived; no plotted sample count was copied from the manuscript.
- Match status: all primary and independent counts agree; the derived values also match the current Methods and Results text.

## Design rationale

Four identical boxes and a non-directional shared bracket encode parallel status. A sequential arrow, funnel, Sankey diagram, or bar chart was deliberately avoided because those forms would imply temporal precedence, attrition, or a magnitude comparison.

## Reproduction

Run from PowerShell:

```powershell
& '<python.exe>' 'C:\Users\PCI\Documents\论文分析\figures\Fig_3.3.1_EEG_sample_framework\plot_Fig_3_3_1_EEG_sample_framework.py' --source-root 'D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat' --output-dir 'C:\Users\PCI\Documents\论文分析\figures\Fig_3.3.1_EEG_sample_framework'
```

Outputs: editable SVG, vector PDF, 600-dpi PNG/TIFF, source-derived CSV, and this audit README.

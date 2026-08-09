# Fig. 8 rationale

**Core conclusion:** Model 1 Block and within-block position coefficients show outcome-specific, directionally repeated patterns across four equal-status onset-trim windows.

**Archetype:** Quantitative forest grid (four outcomes × two temporal terms; four categorical windows per cell).

**Backend:** R only (`ggplot2`; R SVG/PDF/Cairo PNG/TIFF devices).

**Design decision:** Forest-style point ranges were selected. Windows are arranged as categorical rows and are not connected, preventing interpretation as a true time series or selection of a preferred window.

**Statistics:** t-based 95% CI uses the df supplied in each 0805 CR2 file. Estimates and CI are multiplied by 100; the axis therefore states “absolute percentage-point change in relative power”.

**Sources:**
- `SRC0297__06_eeg_primary_onset_window_models_trim_0s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0297__06_eeg_primary_onset_window_models_trim_0s__09_eeg_order_CR2.csv`
- `SRC0363__06_eeg_primary_onset_window_models_trim_5s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0363__06_eeg_primary_onset_window_models_trim_5s__09_eeg_order_CR2.csv`
- `SRC0319__06_eeg_primary_onset_window_models_trim_10s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0319__06_eeg_primary_onset_window_models_trim_10s__09_eeg_order_CR2.csv`
- `SRC0341__06_eeg_primary_onset_window_models_trim_15s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0341__06_eeg_primary_onset_window_models_trim_15s__09_eeg_order_CR2.csv`

**Reviewer risks controlled:** identical plotting rule for all windows; zero reference line; no fatigue/adaptation labels; no p stars; core outcomes only; all numerical rows delivered in `Fig8_plot_data.csv`.

**Exports:** `Fig8_final.png`, `.svg`, `.pdf`, `.tiff`.

# Fig. 7 rationale

**Core conclusion:** The six descriptive cells show different gaze-allocation profiles across the three categorical WWR levels and two complexity levels without implying a continuous dose response.

**Archetype:** Quantitative grid (three aligned panels).

**Backend:** R only (`ggplot2`; R SVG/PDF/Cairo PNG/TIFF devices).

**Design decision:** Point + 95% CI was selected over line + point + CI. Lines would visually imply a continuous WWR trajectory; WWR15/45/75 are discrete experimental levels.

**CI decision:** Participant-condition t-based 95% CI is used for the descriptive figure. Within-subject normalized CI was not selected because QC yields an unbalanced 254-cell participant-condition table, and model-based CI would mix ordered-beta and LMM scales. Formal inference remains in Table 5.

**Source:** `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0055__02_eye_stage2__07_participant_condition_summary.xlsx`.

**Statistics:** n is the number of available participant-condition cells in each WWR×Complexity cell (41–44); center is the arithmetic mean; interval is mean ± t(0.975,n−1)×SE.

**Reviewer risks controlled:** no connecting lines; WWR labeled categorical; C0/C1 encoded by both color and shape; no significance symbols; error-bar definition and source data delivered.

**Exports:** `Fig7_final.png`, `.svg`, `.pdf`, `.tiff`; source data in `Fig7_plot_data.csv`.

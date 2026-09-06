# FINAL ANALYSIS FAMILY MAP

## Eye tracking

### Core outcomes and models

| Outcome | Primary model | Companion / robust layer | Primary complete-case n |
|---|---|---|---|
| Table Share | ordered-beta mixed model | companion LMM + CR2 | 434 |
| Window Share | ordered-beta mixed model | companion LMM + CR2 | 434 |
| Table–Window Share Difference (`RawCompetition`) | LMM | CR2 on the same LMM coefficient scale | 434 |
| Log Table Enrichment | LMM | CR2 on the same LMM coefficient scale | 399 |
| Log Window Enrichment | LMM | CR2 on the same LMM coefficient scale | 371 |
| Table–Window Enrichment Difference (`AdjustedCompetition`) | LMM | CR2 on the same LMM coefficient scale | 339 |

There are **six primary models plus two companion LMMs**. The diagnostics CSV explicitly records successful fitting for all six primary models; the four primary LMMs are non-singular. The two companion LMMs produced CR2 outputs but do not have a separate convergence/singularity diagnostics table in the package.

### Eye coefficient families

Each outcome contributes 14 non-intercept coefficients:

`WWR45 + WWR75 + C1 + low exercise frequency + gender + viewing round + within-round position + two sequence dummies + two WWR×C1 + two WWR×exercise-frequency + one C1×exercise-frequency = 14`.

- Family A: Table Share + Window Share + Table–Window Share Difference = `3 × 14 = 42` tests.
- Family B: Log Table Enrichment + Log Window Enrichment + Table–Window Enrichment Difference = `3 × 14 = 42` tests.
- BH-FDR was applied **separately to A and B**, not once over 84 tests and not separately by outcome.
- Fourteen coefficients have CR2 BH q<.05; 13 satisfy the model-specific primary criterion. Window Share WWR45×C1 is companion-only.
- Ordered-beta primary support means likelihood p<.05 and the model-based 95% CI excludes zero. For the four primary LMM outcomes, the stored primary criterion is a conventional model-based 95% CI excluding zero; CR2 p/q is the robust inference layer.
- The Table 5 CI values are primary model-based intervals, not CR2 intervals.

### Eye pairwise and sensitivities

- WWR pairwise: six outcomes × three WWR contrasts = 18. Holm adjustment is within outcome (family size 3). Seven Holm-adjusted contrasts are <.05.
- Primary threshold: 60%, 46 participants/434 trials. Alternatives: 50%=50/487; 70%=43/347.
- Leave one participant out: 46 omissions × six models = 276 refits; 4,140 coefficient rows; all status=`fit`.
- First-round-only and exact eye–EEG intersection were also refitted. The latter is **34 participants/302 trials**, not the EEG 42/461 common-QC cohort.
- The 14 CR2-BH effects keep their directions across 51 stored sensitivity estimates per effect (three thresholds + first-round + EEG-common + 46 LOO).
- ±5-pixel AOI perturbation was performed only for the two difference outcomes.
- FCR/TFD/TTFF/visited and Equipment Share are not current core outcomes. The exported visited/TFD/two-part and Equipment C1-only model attempts are marked `fit_failed`.

## EEG

### Samples and outcomes

- Window-specific QC: 0 s=42/471; 5 s=42/469; 10 s=43/484; 15 s=43/486.
- Formal common-QC input: 42 participants/461 trials.
- Four core relative-power outcomes: occipital theta, frontal theta, occipital alpha and occipital beta.
- Nine broader relative-power outcomes: frontal/parietal/occipital theta, alpha and broad beta. Low beta and high beta are **not** members of the nine-outcome families.
- Corresponding log10 absolute-power outcomes form separate sensitivity families.

### Fixed structure and coding

`Outcome ~ WWR*visual complexity + WWR*exercise frequency + visual complexity*exercise frequency + gender + viewing round + within-round presentation position + sequence group + (1|participant)`.

References are WWR15, C0 and high exercise frequency. The two sequence dummy coefficients use `new order2` as the observed reference in the R model matrix. `Block` is viewing round; `PositionWithinBlockCentered` is within-round position centered at 3.5. Sequence is adjusted for but is not part of the 72-test temporal substantive family.

### EEG multiplicity families

| Family | Exact composition | Inference | Result |
|---|---|---|---|
| Core coefficient | 4 outcomes × 9 condition coefficients × 4 windows = 144; 36/window | CR2 coefficient p; BH within window and joint | 3 raw p<.05; 0 corrected |
| Core factor | 4 outcomes × 6 factors × 4 = 96; 24/window | CR2 HTZ Wald; BH within/joint | Occipital-theta visual-complexity marginal contrast corrected in all four windows |
| Broader coefficient | 9 outcomes × 9 coefficients × 4 = 324; 81/window | 18-Aug LMM CR2 cross-check; BH within/joint | 14 raw p<.05; 0 corrected |
| Broader factor | 9 outcomes × 6 factors × 4 = 216; 54/window | CR2 HTZ Wald; BH within/joint | Above occipital-theta results plus 15-s parietal-beta WWR omnibus joint q=.02816 |
| Core log10 absolute factor | 4×6×4=96 | CR2 HTZ; BH within/joint | 0 corrected |
| Broader log10 absolute factor | 9×6×4=216 | CR2 HTZ; BH within/joint | 0 corrected |
| Broader relative temporal | 9 outcomes × 2 predictors × 4 = 72 | CR2 coefficient p; BH within/joint | Current 3.3.3 values verified |
| Broader log10 absolute temporal | 9 outcomes × 2 predictors × 4 = 72 | CR2 coefficient p; BH within/joint | Current 3.3.3 values verified |
| Previous-scene | 4 core outcomes × 3 prior-condition coefficients × 4 = 48; 12/window | CR2 coefficient p; BH within/joint | 2 raw p<.05; 0 corrected; analyzed n=386 |
| Direct onset comparison | 9 relative outcomes × 14 GEE coefficients × 6 window pairs = 756 | descriptive difference CI only | all CIs include 0; no p/equivalence test |

The six factor tests are WWR, visual complexity, exercise frequency, WWR×visual complexity, WWR×exercise frequency and visual complexity×exercise frequency. WWR and the two WWR interactions are multi-df tests; binary main effects and visual-complexity×exercise-frequency are one-df tests.

The factor-level visual-complexity estimand is an **equal-weight marginal C1−C0 contrast averaged over WWR and exercise-frequency levels**. The reference-coded `ComplexityC1` coefficient is the simple C1−C0 effect at WWR15/high exercise frequency. Therefore their raw p values are not expected to be identical; the discrepancy is not merely a 96-versus-144 BH-family-size effect.

The 14 coefficients used in the 756 descriptive contrasts are: intercept, nine condition/group coefficients, gender, viewing round, within-round position and **one** sequence-group dummy. This is the exported participant-clustered GEE specification, not the 15-coefficient R Model 1 LMM (which contains two sequence dummies). That difference is another reason the 756 rows must remain descriptive and supplementary.

## Cross-modality covariate and coding map

| Modality | Viewing round in primary model | Within-round position in primary model | Sequence in primary model | Multiplicity role | Substantive reporting role |
|---|---|---|---|---|---|
| Questionnaire | Yes | Yes | Yes | Included in the questionnaire model family described in the current manuscript; raw machine-readable questionnaire family was outside the two designated source folders | Adjustment variables; do not interpret automatically as fatigue/learning |
| Eye tracking | Yes, as `Block` | Yes, centered | Yes, two dummy coefficients | All four adjustment coefficients per outcome are inside eye family A or B | Round/position summarized; sequence currently omitted but all q≥.490 |
| EEG Model 1 | Yes, as `Block` | Yes, centered | Yes, two dummy coefficients | The 144/324 condition families exclude adjustment coefficients; separate temporal families include round and position only | Round/position reported as temporal patterns; sequence is adjustment only |

| Modality/sample | Low exercise frequency | High exercise frequency | Reference / contrast |
|---|---:|---:|---|
| Questionnaire analytical cohort | 26 | 16 | High reference; treatment/dummy contrast Low−High |
| Eye primary 60% tracking cohort | 23 | 23 | High reference; treatment/dummy contrast Low−High |
| EEG common-QC cohort | 26 | 16 | High reference; treatment/dummy contrast Low−High |

All three modalities use the Q1.4 exercise-frequency classification. `Sport experience`, `sports-specific experience`, `high-experience` and `low-experience` are legacy labels and must not be used as synonyms.

## Methods legacy-status map

| Methods item | Status | Audit basis |
|---|---|---|
| Six core eye outcomes and their primary/companion models | KEEP | Complete machine-readable model and CR2 outputs exist |
| Eye WWR Holm pairwise and specified sensitivities | KEEP | Complete 18-row pairwise and sensitivity outputs exist |
| FCR, TFD, TTFF and visited as completed inferential outcomes | DELETE AS LEGACY | Not current core; visited/TFD/two-part exported model attempts are `fit_failed`; TTFF/FCR lack final core outputs |
| Binary visited GLMM described as completed | DELETE AS LEGACY | Exported GLMM attempt is `fit_failed` |
| Equipment Share as core/current inferential outcome | DELETE AS LEGACY | C1-only equipment models are `fit_failed`; may be retained only as a descriptive derived variable in Supplementary |
| ±5-pixel AOI perturbation | KEEP | Successful outputs exist, but only for the two difference outcomes |
| Four EEG relative-power core outcomes, common-QC and Model 1 | KEEP | Directly traceable to 0805 outputs |
| Log10 absolute power | KEEP AS SUPPLEMENTARY | Complete 18-Aug factor/temporal sensitivity outputs exist; no corrected condition finding |
| Gray-screen/post-stimulus `ΔO_alpha` recovery | DELETE AS LEGACY | No corresponding output/script/model in 0803 or 0805 |
| Three-way interaction exclusion statement | KEEP | Correctly states that the current core model does not include it |
| Old nonlinear/quadratic EEG analysis or WWR45-peak claim | DELETE AS LEGACY | Not supported by the current corrected families |
| `sport experience` group definition | DELETE AS LEGACY | True variable is Q1.4 exercise frequency |
| Filtering/notch/re-reference/ICA details | UNRESOLVED | Not recoverable from the two designated packages; keep only with separately archived upstream evidence |
| 756 direct onset-window comparisons | MOVE TO SUPPLEMENTARY | Descriptive GEE coefficient differences, not formal CR2/equivalence inference |

### Provenance boundary

- The 144 core coefficient results and their four focal frontal-theta values come directly from the 0805 common-QC Model 1 CR2 CSVs.
- The 96/216 factor tests, 324 CR2 coefficient cross-check, temporal families and 72-model diagnostics were generated on 18 August from the 0805 common-QC model inputs by `C:\Users\PCI\Documents\论文分析\work\eeg_audit\reanalyse_factor_tests.R` and `C:\Users\PCI\Documents\论文分析\work\eeg_audit\summarize_temporal.py`. They are reproducible complementary outputs, but not original 0803/0805 factor-level tables.
- The 0805 methods report operationally labels four windows parallel/equal status, while also documenting a 10-s backwards-compatible reference export. A dated pre-outcome analysis plan is not present, so prospective historical prespecification remains unverified.

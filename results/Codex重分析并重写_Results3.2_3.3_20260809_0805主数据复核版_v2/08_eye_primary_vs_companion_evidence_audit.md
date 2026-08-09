# TableShare / WindowShare primary versus companion evidence audit

## Final answers

1. **Does the original “14 Robust” label require correction?** YES. The defensible statement is: 14 non-intercept terms met companion CR2–BH q<.05; 13 also passed the corresponding primary-model criterion.
2. **Concordant evidence count:** 13 among the original 14; within the six original Robust TableShare/WindowShare terms, 5.
3. **Companion-only count:** 1 among the original 14; the same single exception occurs within TableShare/WindowShare.
4. **WindowShare WWR45 × C1:** Companion-only. Primary ordered-beta β=-.344242, SE=.211902, 95% CI [-.759562,.071078], likelihood p=.104262; companion LMM β=-.024443, CR2 SE=.007987, df=36.150, p=.004152, BH q=.012457.
5. **Was Table 5 rebuilt?** YES. It now has separate primary-model and companion-model β/uncertainty/inference columns plus Evidence_status.
6. **Was Results 3.2 updated?** YES. It states 14 companion-positive terms, 13 Concordant terms and one Companion-only term; no sentence describes WindowShare WWR45×C1 as jointly supported.
7. **Which 0803/0805 wording is outdated or imprecise?** The SRC0083 rule `Robust requires primary and CR2 q<0.05...` is not satisfied by its own WindowShare WWR45×C1 row because `PrimaryAdjustedP` duplicates the companion BH q instead of the primary likelihood p. The SRC0085 sentence claiming that evidence grades integrate primary fits and CR2 is therefore too broad, and the `PrimaryAdjustedP`/`CR2AdjustedP` headers in SRC0084/SRC0085 are misleading for ordered-beta rows. Both analysis generations contain the same affected files.

## Scope-specific counts

- Original 14 across all six eye outcomes: companion q<.05=14; Concordant=13; Companion-only=1; Primary-only=0; No corrected evidence=0.
- All 28 non-intercept TableShare/WindowShare terms: companion q<.05=6; Concordant=5; Companion-only=1; Primary-only=0; No corrected evidence=22.

## Bottom-level sources

- `SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
- `SRC0059__02_eye_stage2__10_familyB_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0059__02_eye_stage2__10_familyB_primary_models.csv`
- `SRC0063__02_eye_stage2__12_CR2_robust_results.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0063__02_eye_stage2__12_CR2_robust_results.csv`

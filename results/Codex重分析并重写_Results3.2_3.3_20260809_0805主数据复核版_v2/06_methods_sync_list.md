# Methods synchronization list

The Methods section should later be synchronized with the rewritten Results as follows:

1. Define the six eye-tracking outcomes and their scales: TableShare, WindowShare, RawCompetition, LogTableEnrichment, LogWindowEnrichment and AdjustedCompetition.
2. State that 60% valid tracking is the primary threshold (46 participants/434 trials); 50% and 70% are sensitivity thresholds only.
3. Specify ordered-beta mixed models for TableShare/WindowShare and participant-random-intercept LMMs for the other four outcomes.
4. For TableShare/WindowShare, report primary ordered-beta beta/SE/CI/likelihood p separately from companion LMM beta/CR2 SE/df/p/BH q; do not construct a cross-scale CR2 CI or call companion-only evidence jointly supported.
5. Define evidence status as Concordant, Companion-only, Primary-only or No corrected evidence. State that 14 terms passed companion CR2–BH, of which 13 were Concordant and WindowShare WWR45×C1 was Companion-only.
6. Define BH families for companion coefficients and Holm correction for within-outcome WWR pairwise comparisons.
7. Rename `ExperienceGroup` in manuscript prose as the Q1.4-based table-tennis exercise-frequency group; avoid expertise/expert/novice terminology.
8. Describe eye sensitivity analyses: 50/60/70% thresholds, Block 1, leave-one-participant-out, EEG common-sample and AOI ±5 px.
9. Record the Stage 3 C0-empty-value coding limitation and state that fit_failed/empty tables are not negative results.
10. Give 0/5/10/15 s EEG windows equal status and distinguish window-specific QC from the 42-participant/461-trial common sample.
11. Define the four core relative-power outcomes: O_theta_relative, F_theta_relative, O_alpha_relative and O_beta_relative.
12. Define Model 1 temporal covariates: Block and PositionWithinBlockCentered, with CR2 standard errors and df-based t intervals.
13. Predefine the 36 condition tests per window and both BH families: within-window 36 and joint four-window 144.
14. Define the broader nine-outcome 324-test audit as supplementary and non-overriding.
15. Define the 48-term PreviousScene audit and its within-window and joint corrections.
16. Define `onset_window_comparisons.csv` as descriptive sensitivity (`parallel_descriptive_pairwise`), not a new inferential family.
17. Retain the 10 s/42-participant/474-trial analysis only as compatibility/reference, never as the final EEG main sample.

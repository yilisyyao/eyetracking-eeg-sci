# QUESTIONS STILL UNRESOLVED

Only items that cannot be settled from the supplied handoff files are listed here.

1. **Historical prespecification of the four onset-trim variants.** The 0805 pipeline outputs operationally treat 0/5/10/15 s as parallel equal-status analyses, but no dated statistical analysis plan or version-controlled config predating outcome inspection was supplied. The same methods report calls 10 s a backwards-compatible reference export.
2. **Origin of the abandoned EEG coefficient set** `.00995/.00935/.00841/.00549`. No matching four-row output was found in 0803, 0805, 260813, 260905 or the 18-Aug machine-readable outputs. It must not be used without its source file.
3. **Why WWR=30 was hard-coded in the discarded 18-Aug document builder.** No statistical output contains WWR30; the script provenance explains how it entered prose but not why the author of that code chose it.
4. **Separate diagnostics for the two eye companion LMMs.** CR2 coefficient outputs prove that the models were fit, but a dedicated convergence/singularity table for those two companion fits is absent.
5. **Original executable scripts for several 0803/0805 exports.** Run manifests and formula-bearing CSVs are present, but the eye-stage scripts, the reviewer previous-scene script, and the Python onset-pairwise generator are not archived in the supplied packages. Exact numbers are traceable; full from-scratch reproducibility is incomplete.
6. **Upstream EEG preprocessing.** The 0805 methods report explicitly says filter/reference history is not recoverable from the exporter. Filtering, notch, re-reference and ICA can only remain as detailed Methods claims if the separate upstream evidence audit, raw EEGLAB history or preprocessing logs are formally linked to this analysis version.
7. **Questionnaire-side raw Q1.4 provenance.** The current manuscript and EEG/eye model inputs agree on the 26-low/16-high common cohort and on high as reference, but the raw questionnaire recoding script/input is not part of the two designated 0803/0805 folders.

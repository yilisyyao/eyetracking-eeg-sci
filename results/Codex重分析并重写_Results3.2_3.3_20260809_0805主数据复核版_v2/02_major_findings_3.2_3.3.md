# Results 3.2–3.3 主要结论及底层证据

> 分析日期：2026-08-09  
> 数据代际：眼动与 EEG 主分析输入均来自 0805；0803 仅用于跨版本一致性核对。  
> 证据规则：关键数字优先采用 0805 底层 CSV/XLSX；报告与交接索引仅用于定位和交叉核对。

## A. Results 3.2 主要结论

### 【3.2-1】60% tracking 阈值定义了眼动主样本，六条件均值复算与报告一致

**Data relationship / 数据关系：** The prespecified 60% valid-tracking threshold retained 46 participants and 434 trials. / 预设的 60% 有效追踪率阈值保留 46 名参与者、434 个试次。

**Key statistics / 关键数字：** 50%、60%、70% 阈值分别为 50/487、46/434、43/347。参与者—条件汇总表含 254 个可用单元。TableShare 在 C0 的 WWR15/45/75 均值为 29.04%/27.99%/27.96%，在 C1 为 19.29%/19.72%/24.70%；WindowShare 分别为 2.01%/8.15%/13.56% 与 1.59%/5.29%/11.24%；RawCompetition 分别为 27.03%/19.85%/14.40% 与 17.70%/14.43%/13.46%。18 个均值与指令中四位小数口径一致。

**Source files / 源数据文件：**
- `SRC0055__02_eye_stage2__07_participant_condition_summary.xlsx`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0055__02_eye_stage2__07_participant_condition_summary.xlsx`
- `SRC0056__02_eye_stage2__08_core_descriptive_statistics.xlsx`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0056__02_eye_stage2__08_core_descriptive_statistics.xlsx`
- `SRC0065__02_eye_stage2__13_tracking_threshold_sensitivity.xlsx`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0065__02_eye_stage2__13_tracking_threshold_sensitivity.xlsx`

**Evidence status / 证据状态：** Descriptive + QC.

**Discussion boundary / Discussion 边界：** Results 仅报告份额和差值；“注意竞争”“更专注”或为何出现这些均值模式应留到 Discussion。

### 【3.2-2】六个核心眼动模型全部拟合；14 项通过 companion CR2–BH，其中 13 项为双层一致证据

**Data relationship / 数据关系：** All six prespecified eye-tracking models fitted successfully. Fourteen non-intercept terms met the companion CR2–BH threshold; 13 were also supported by the corresponding primary-model inference. / 六个预设眼动模型均成功拟合。14 个非截距项达到 companion CR2–BH 阈值，其中 13 项同时得到相应主模型推断支持。

**Key statistics / 关键数字：** TableShare 与 WindowShare 为 ordered-beta mixed models（各 n=434）；RawCompetition 为 LMM（n=434）；LogTableEnrichment、LogWindowEnrichment、AdjustedCompetition 的 n 分别为 399、371、339。14 项分布为 RawCompetition 5 项、TableShare 3 项、WindowShare 3 项、LogTableEnrichment 2 项、LogWindowEnrichment 1 项；AdjustedCompetition 为 0 项。

**Source files / 源数据文件：**
- `SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
- `SRC0059__02_eye_stage2__10_familyB_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0059__02_eye_stage2__10_familyB_primary_models.csv`
- `SRC0063__02_eye_stage2__12_CR2_robust_results.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0063__02_eye_stage2__12_CR2_robust_results.csv`
- `SRC0080__02_eye_stage2__17_core_model_diagnostics.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0080__02_eye_stage2__17_core_model_diagnostics.csv`

**Evidence status / 证据状态：** 13 Concordant；1 Companion-only；0 Primary-only；0 No corrected evidence（此计数范围为原报告的 14 项）。

**Discussion boundary / Discussion 边界：** “14 项”是 q<0.05 的重算计数，不自动等同于机制性“robust effects”。尤其 WindowShare 的 WWR45×C1 项存在主模型与 companion CR2 推断不一致，必须如实并列。

### 【3.2-3】WWR 的主要眼动关系集中在 WindowShare 与 RawCompetition

**Data relationship / 数据关系：** Relative to WWR15, WindowShare increased at WWR45 and WWR75, whereas RawCompetition decreased at both levels. / 相对 WWR15，WWR45 和 WWR75 的 WindowShare 增加，而 RawCompetition 在两个水平下降。

**Key statistics / 关键数字：** WindowShare 主 ordered-beta：WWR45 β=1.00184、SE=.17838、95% CI .65222–1.35147、likelihood p=1.95×10^-8；WWR75 β=1.59320、SE=.16471、95% CI 1.27038–1.91602、p=3.93×10^-22。Companion LMM–CR2：WWR45 β=.05515、CR2 p=1.80×10^-6、q=5.40×10^-6；WWR75 β=.11043、p=2.48×10^-8、q=7.43×10^-8。RawCompetition：WWR45 β=-.0603（CR2 95% CI -.1111 至 -.00963，p=.0216，q=.0325）；WWR75 β=-.0913（-.1481 至 -.0345，p=.00281，q=.00422）。Holm 比较中 WindowShare 和 RawCompetition 的三个 WWR 两两对比均 p<.05；TableShare 的三个对比均未达到 Holm 阈值。

**Source files / 源数据文件：**
- `SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
- `SRC0061__02_eye_stage2__11_WWR_posthoc_Holm.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0061__02_eye_stage2__11_WWR_posthoc_Holm.csv`

**Evidence status / 证据状态：** WindowShare 两项 WWR 主效应为 Concordant；RawCompetition 为同尺度 LMM 主模型与 CR2 推断；另有 outcome-wise Holm post-hoc。

**Discussion boundary / Discussion 边界：** WWR 是三个离散水平；不得写成连续剂量反应、倒 U 形或“最佳 WWR”。

### 【3.2-4】复杂度及其与 WWR75 的交互达到校正阈值

**Data relationship / 数据关系：** C1 was associated with lower TableShare, RawCompetition and LogTableEnrichment, with positive WWR75×C1 interaction coefficients for the same three outcomes. / C1 与较低的 TableShare、RawCompetition 和 LogTableEnrichment 相关，同时这三项的 WWR75×C1 交互系数为正。

**Key statistics / 关键数字：** TableShare 主 ordered-beta 的 C1 β=-.60770、SE=.12160、95% CI -.84603 至 -.36936、likelihood p=5.81×10^-7；companion LMM β=-.09958、CR2 p=.000308、q=.000487。TableShare WWR75×C1 主模型 β=.43805、SE=.14586、95% CI .15218–.72392、p=.00267；companion β=.07987、CR2 p=.00195、q=.00293。RawCompetition C1 β=-.105（CR2 95% CI -.158 至 -.0525，p=.000324，q=.000487）；LogTableEnrichment C1 β=-.527（-.707 至 -.347，p=1.99×10^-6，q=5.97×10^-6）。

**Source files / 源数据文件：**
- `SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
- `SRC0059__02_eye_stage2__10_familyB_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0059__02_eye_stage2__10_familyB_primary_models.csv`

**Evidence status / 证据状态：** TableShare 两项均为 Concordant；连续 LMM 结局使用同尺度主模型与 CR2 推断。

**Discussion boundary / Discussion 边界：** Results 可报告交互方向与条件均值；“复杂度效应被削弱的原因”属于 Discussion。

### 【3.2-5】Q1.4-based 乒乓球运动频率组交互仅出现在 WWR75 的两项核心结局

**Data relationship / 数据关系：** At WWR75, the low table-tennis exercise-frequency group had negative interaction coefficients for TableShare and RawCompetition. / 在 WWR75 条件下，低乒乓球运动频率组对 TableShare 和 RawCompetition 的交互系数为负。

**Key statistics / 关键数字：** TableShare WWR75×Low 主 ordered-beta β=-.49879、SE=.14487、95% CI -.78273 至 -.21485、likelihood p=.000575；companion LMM β=-.09478、CR2 p=.000372、q=.00112。RawCompetition WWR75×Low β=-.117（同尺度 CR2 95% CI -.190 至 -.0446，p=.00230，q=.00345）。

**Source files / 源数据文件：**
- `SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0057__02_eye_stage2__09_familyA_primary_models.csv`

**Evidence status / 证据状态：** Primary interaction terms.

**Discussion boundary / Discussion 边界：** 论文统一称 “Q1.4-based table-tennis exercise-frequency group / 基于 Q1.4 的乒乓球运动频率组”，不称 expert/novice/expertise。

### 【3.2-6】时间项未过 BH；14 项 companion 筛选结果均方向稳定，但 Stage 3 的失败模型不能作为阴性证据

**Data relationship / 数据关系：** No eye-tracking Block or within-block position coefficient met companion CR2–BH q<0.05; each of the 14 companion-selected terms retained its direction in all 51 available Stage 2 sensitivity estimates. / 眼动 Block 与区组内位置项均未达到 companion CR2–BH q<0.05；14 个 companion 筛选项在各自 51 个 Stage 2 敏感性估计中方向均一致。

**Key statistics / 关键数字：** Block/Position 的 q 范围为 .255–.815；每项 51/51（100%）方向一致，来源为 50/60/70% 阈值、Block 1、46 次 leave-one-participant-out 和 EEG common-sample。Stage 3 诊断为 4 fit、17 fit_failed；可估计结果仅限 AOI ±5 px 边界模型，其他失败与 C0 被编码为空值有关。

**Source files / 源数据文件：**
- `SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0057__02_eye_stage2__09_familyA_primary_models.csv`
- `SRC0059__02_eye_stage2__10_familyB_primary_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0059__02_eye_stage2__10_familyB_primary_models.csv`
- `SRC0066__02_eye_stage2__13_tracking_threshold_sensitivity_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0066__02_eye_stage2__13_tracking_threshold_sensitivity_models.csv`
- `SRC0070__02_eye_stage2__14_block1_sensitivity_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0070__02_eye_stage2__14_block1_sensitivity_models.csv`
- `SRC0072__02_eye_stage2__15_leave_one_participant_out.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0072__02_eye_stage2__15_leave_one_participant_out.csv`
- `SRC0075__02_eye_stage2__16_EEG_valid_common_sample_sensitivity.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0075__02_eye_stage2__16_EEG_valid_common_sample_sensitivity.csv`
- `SRC0107__04_eye_stage3__03b_AOI_boundary_sensitivity_models.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0107__04_eye_stage3__03b_AOI_boundary_sensitivity_models.csv`
- `SRC0139__04_eye_stage3__17_stage3_model_diagnostics.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0139__04_eye_stage3__17_stage3_model_diagnostics.csv`
- `SRC0148__04_eye_stage3__eye_stage3_model_input.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0148__04_eye_stage3__eye_stage3_model_input.csv`

**Evidence status / 证据状态：** Sensitivity + model diagnostics.

**Discussion boundary / Discussion 边界：** “未达到校正阈值”不能写成无效应；fit_failed 更不能写成“无效应”。

## B. Results 3.3 主要结论

### 【3.3-1】0805 四窗口具有同等地位；正式共同样本为 42 人/461 试次

**Data relationship / 数据关系：** The 0-, 5-, 10- and 15-s onset-trim windows were analyzed in parallel on a common-QC sample. / 0、5、10、15 s 起始截窗在共同 QC 样本上平行分析。

**Key statistics / 关键数字：** 独立 QC：0 s=42/471，5 s=42/469，10 s=43/484，15 s=43/486；共同 QC=42/461。核心 relative-power outcomes 为 O_theta_relative、F_theta_relative、O_alpha_relative、O_beta_relative。

**Source files / 源数据文件：**
- `SRC0277__00_eeg_onset_statistics__onset_parallel_sample_flow.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0277__00_eeg_onset_statistics__onset_parallel_sample_flow.csv`
- `SRC0276__00_eeg_onset_statistics__onset_common_qc_parallel.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0276__00_eeg_onset_statistics__onset_common_qc_parallel.csv`
- `SRC0288__06_eeg_primary_onset_window_models__onset_variant_model_index.xlsx`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0288__06_eeg_primary_onset_window_models__onset_variant_model_index.xlsx`
- `SRC0194__06_eeg_primary__01_eeg_outcome_classification.xlsx`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0194__06_eeg_primary__01_eeg_outcome_classification.xlsx`
- `SRC0195__06_eeg_primary__02_eeg_model_contract.xlsx`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0195__06_eeg_primary__02_eeg_model_contract.xlsx`
- `SRC0208__06_eeg_primary__06_eeg_variable_dictionary.xlsx`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0208__06_eeg_primary__06_eeg_variable_dictionary.xlsx`
- `SRC0283__00_eeg_onset_statistics__onset_methods_and_limitations.md`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0283__00_eeg_onset_statistics__onset_methods_and_limitations.md`

**Evidence status / 证据状态：** QC + model contract.

**Discussion boundary / Discussion 边界：** 0803 的 10 s/42 人/474 试次仅为 compatibility/reference，不得作为最终主样本。

### 【3.3-2】Block 关系跨四窗方向一致；Position 关系仅在两个 theta 结局跨四窗达到 raw p<.05

**Data relationship / 数据关系：** Across all four windows, Model 1 Block coefficients were negative for occipital and frontal theta, positive for occipital alpha, and not statistically reliable for occipital beta. / 四窗中，Model 1 的 Block 系数在枕区与额区 theta 为负、在枕区 alpha 为正，而枕区 beta 未形成统计可靠关系。

**Key statistics / 关键数字：** O_theta Block β=-.00453 至 -.00548（四窗 raw p=.00179–.00379）；F_theta β=-.00577 至 -.00669（p=.000320–.00127）；O_alpha β=.02465–.02957（p=.000458–.000774）；O_beta β=.00145–.00194（p=.679–.748）。O_theta Position β=-.000952 至 -.00116（p=.00937–.0394）；F_theta Position β=-.00104 至 -.00135（p=.00159–.0267）；O_alpha 与 O_beta Position 的四窗 raw p 均>.05。

**Source files / 源数据文件：**
- `SRC0297__06_eeg_primary_onset_window_models_trim_0s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0297__06_eeg_primary_onset_window_models_trim_0s__09_eeg_order_CR2.csv`
- `SRC0363__06_eeg_primary_onset_window_models_trim_5s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0363__06_eeg_primary_onset_window_models_trim_5s__09_eeg_order_CR2.csv`
- `SRC0319__06_eeg_primary_onset_window_models_trim_10s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0319__06_eeg_primary_onset_window_models_trim_10s__09_eeg_order_CR2.csv`
- `SRC0341__06_eeg_primary_onset_window_models_trim_15s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0341__06_eeg_primary_onset_window_models_trim_15s__09_eeg_order_CR2.csv`

**Evidence status / 证据状态：** Primary Model 1 temporal covariates, raw CR2 p and t-based 95% CI.

**Discussion boundary / Discussion 边界：** 只报告实验进程相关数据关系；不得命名为疲劳、适应、学习、警觉或神经效率。

### 【3.3-3】核心 144 个条件系数中仅 3 个 raw p<.05，校正后为 0

**Data relationship / 数据关系：** No core condition-related coefficient survived either the within-window or joint four-window BH correction. / 核心条件系数没有任何一项通过窗口内或四窗口联合 BH 校正。

**Key statistics / 关键数字：** 4 outcomes×9 terms×4 windows=144。仅 F_theta_relative 的 WWR45×C1 在 0/5/10 s 有 raw p<.05：β=.00757（p=.0288，窗口 q=.650，联合 q=.668）、.00856（p=.0132，q=.475/.668）、.00750（p=.0334，q=.524/.668）；15 s β=.00475（p=.170，q=.721/.698）。最终计数=3/0/0。

**Source files / 源数据文件：**
- `SRC0297__06_eeg_primary_onset_window_models_trim_0s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0297__06_eeg_primary_onset_window_models_trim_0s__09_eeg_order_CR2.csv`
- `SRC0363__06_eeg_primary_onset_window_models_trim_5s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0363__06_eeg_primary_onset_window_models_trim_5s__09_eeg_order_CR2.csv`
- `SRC0319__06_eeg_primary_onset_window_models_trim_10s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0319__06_eeg_primary_onset_window_models_trim_10s__09_eeg_order_CR2.csv`
- `SRC0341__06_eeg_primary_onset_window_models_trim_15s__09_eeg_order_CR2.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0341__06_eeg_primary_onset_window_models_trim_15s__09_eeg_order_CR2.csv`

**Evidence status / 证据状态：** Primary core multiplicity audit.

**Discussion boundary / Discussion 边界：** raw p<.05 不得写成正式显著，也不得据此建立 WWR/复杂度神经机制。

### 【3.3-4】九结局 broader audit 为 324 项，14 个 raw p<.05，校正后仍为 0

**Data relationship / 数据关系：** The broader nine-outcome audit produced raw signals but no coefficient met either FDR threshold. / 九结局广泛审计出现未经校正信号，但没有系数达到任一 FDR 阈值。

**Key statistics / 关键数字：** 9 outcomes×9 terms×4 windows=324；36 个 window×outcome 模型全部 fit；计数=14 raw p<.05、0 within-window FDR、0 joint FDR。

**Source files / 源数据文件：**
- `SRC0286__00_eeg_onset_statistics__onset_variant_model_results.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0286__00_eeg_onset_statistics__onset_variant_model_results.csv`
- `SRC0285__00_eeg_onset_statistics__onset_variant_model_diagnostics.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0285__00_eeg_onset_statistics__onset_variant_model_diagnostics.csv`

**Evidence status / 证据状态：** Broader audit.

**Discussion boundary / Discussion 边界：** 该层不能覆盖四个 core relative-power outcomes 的主分析。

### 【3.3-5】Previous-scene 48 项仅 2 个 raw p<.05，校正后为 0

**Data relationship / 数据关系：** No previous-scene coefficient met the corrected threshold. / 没有前序场景系数达到校正阈值。

**Key statistics / 关键数字：** 10 s O_theta_relative×PreviousWWR75 β=.00309，p=.0443，窗口 q=.532，联合 q=.807；15 s β=.00425，p=.00986，窗口 q=.118，联合 q=.473。48 项总计=2/0/0。

**Source files / 源数据文件：**
- `SRC0421__07_reviewer_analysis__Reviewer1_parallel_previous_scene_FDR.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0421__07_reviewer_analysis__Reviewer1_parallel_previous_scene_FDR.csv`

**Evidence status / 证据状态：** Previous-scene sensitivity.

**Discussion boundary / Discussion 边界：** 只能写 “no previous-scene coefficient met the corrected threshold”；不得写 carryover absent/eliminated。

### 【3.3-6】窗口比较文件仅承担描述性敏感性角色

**Data relationship / 数据关系：** All 756 pairwise window-comparison rows are labeled `parallel_descriptive_pairwise`. / 756 行窗口两两比较均被标记为 `parallel_descriptive_pairwise`。

**Key statistics / 关键数字：** inference_role 唯一值为 parallel_descriptive_pairwise。

**Source files / 源数据文件：**
- `SRC0287__00_eeg_onset_statistics__onset_window_comparisons.csv`
  - `D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0287__00_eeg_onset_statistics__onset_window_comparisons.csv`

**Evidence status / 证据状态：** Descriptive window sensitivity.

**Discussion boundary / Discussion 边界：** 优先放 Supplement；不得由此新建显著性主线或选择“最好”的窗口。

# 0803/0805 分析报告与底层数据交叉核对

## 核对范围

- 0803 报告：`D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0803-（剔除eeg0 5 10 15）\论文数据分析结果报告-0803.docx`
- 0805 报告：`D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\论文数据分析结果报告-0805.docx`
- 0803 交接索引：`D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0803-（剔除eeg0 5 10 15）\数据来源交接索引.xlsx`
- 0805 交接索引：`D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\数据来源交接索引.xlsx`
- 最终真值：本目录 `01_source_inventory.csv` 所列底层 CSV/XLSX/MD。

## 1. 与底层数据完全一致的报告结论

1. **Eye main sample：一致。** 60% 阈值为 46 人/434 试次；50% 与 70% 分别为 50/487 与 43/347。
2. **Eye descriptive means：一致。** TableShare、WindowShare、RawCompetition 的 18 个六条件均值均与参与者—条件汇总表重算一致，报告差异仅为四舍五入。
3. **Eye model fit：一致。** 六个核心模型全部 fit，outcome-specific n 为 434/434/434/399/371/339。
4. **Eye companion q<.05 count：数值一致但标签需修正。** 非截距 companion CR2–BH q<.05 确为 14 项；AdjustedCompetition 为 0 项；Block/Position 为 0 项。14 不能直接称为“双层共同支持”。
5. **Eye direction sensitivity：一致。** 14 个 companion 筛选项各有 51 个 Stage 2 敏感性估计，方向一致率均为 100%；方向一致不替代 primary-model 显著性。
6. **Stage 3 边界：一致。** 诊断为 4 fit、17 fit_failed；成功项为 AOI ±5 px 边界模型，失败项不得解释为阴性。
7. **EEG 0805 sample：一致。** 独立 QC 为 42/471、42/469、43/484、43/486；共同样本为 42/461。
8. **Broader audit：一致。** 324 项中 14 个 raw p<.05、0 个窗口内 FDR、0 个联合 FDR。
9. **Previous-scene：一致。** 48 项中 2 个 raw p<.05，校正后 0。

## 2. 因分析世代更新而过时的报告结论

1. **0803 的 EEG 42 人/474 试次不能再作为 3.3 主样本。** 它仅是 10 s compatibility/reference；最终主分析为 0805 四窗口共同 42/461。
2. **0803 的 10–15 s、42 人/465 试次等效性叙事不是最终 parallel 主线。** 0805 以四个窗口同等地位、共同 QC 和 window/joint FDR 为准。
3. **0803 单一 10 s PreviousWWR75 结果（β≈.00370，p≈.0156）已被四窗口 48 项审计取代。** 0805 的 10 s 与 15 s raw 信号分别为 β=.00309 与 .00425，均未过校正。
4. **0805 报告 Table 9 的 10 s 时间项数值是 compatibility/reference 口径。** Results 3.3 现改用四个 42/461 common-sample 文件，四窗同等报告。

## 3. 数字轻微差异但可由样本或推断口径解释

1. **Eye means：** 报告使用百分比两位小数，本次重算保留完整精度；最大差异小于 0.005 个百分点，属于四舍五入。
2. **EEG 10 s time terms：** 0805 报告中的估计、CI 或 p 与 common-sample 10 s 文件有轻微差异，原因是 compatibility 42/474 与 parallel common 42/461 的样本和 CR2 推断口径不同。新正文只使用 42/461 文件。
3. **Eye 双模型尺度：** ordered-beta 主模型的 β/SE/CI/likelihood p 与 companion LMM 的 β/CR2 SE/df/p/q 不在同一模型尺度；不能混拼为一个“CR2 CI”，也不能只展示 primary β 却把 companion q 写成同一模型的校正结果。新 Table 5 与证据审计表分别展示两套 β。

## 4. “Robust”标签复核与需视为过时/不严谨的原句

底层重算得到：14 个非截距项达到 companion CR2–BH q<.05，其中 13 项同时通过相应 primary-model 标准，1 项为 Companion-only。TableShare/WindowShare 原标记 Robust 的 6 项中，5 项 Concordant，1 项 Companion-only。

1. **FAIL — SRC0083 的规则句：** `Robust requires primary and CR2 q<0.05...`。该规则本身要求两层均通过，但同表的 `PrimaryAdjustedP` 对 ordered-beta 项并非 primary likelihood p，而是与 `CR2AdjustedP` 完全相同的 companion BH q；因此这句话不能验证 WindowShare WWR45×C1 的 primary 层。
2. **FAIL — SRC0083 的 WindowShare `WWRWWR45:ComplexityC1` 行：** `EvidenceGrade=Robust`、`PrimaryAdjustedP=.01245714`、`CR2AdjustedP=.01245714`。底层 primary ordered-beta 实际为 β=-.34424、SE=.21190、95% CI [-.75956,.07108]、likelihood p=.10426；companion LMM 为 β=-.024443、CR2 SE=.007987、df=36.150、p=.004152、BH q=.012457。最终分类必须为 **Companion-only**。
3. **WARN — SRC0085 英文概述句：** `Evidence grades integrate primary fits, CR2 and structural sensitivity results rather than statistical significance alone.` 这句话过于笼统；对上述例外会让读者误认为 primary 与 companion 均通过。应改为逐层报告，方向敏感性另列。
4. **WARN — SRC0084/SRC0085 表头：** `PrimaryAdjustedP` 与 `CR2AdjustedP` 并列，但 ordered-beta 行的两个值来自同一 companion BH q，不能作为两套独立证据。0803 与 0805 中这些文件内容相同，故同样需要视为过时标签。

除 WindowShare WWR45×C1 的证据分级外，未发现其余 13 个 companion q<.05 项存在 primary/companion 分类冲突。

## 5. 只属于 Discussion、不应进入 Results 的解释性语言

以下 8 类报告语言已从重写 Results 中删除或改为纯数据关系：

1. “窗户获得更多注意后，球桌优势减弱”的机制化解释；Results 只报告 RawCompetition 的均值和系数。
2. “提示复杂度效应受到 WWR 调节”的解释性扩展；Results 只报告交互系数。
3. “空间体验与任务相关注意之间存在维度权衡”。
4. 将 EEG Block/Position 命名为疲劳、适应、学习、警觉或任务熟悉。
5. “降低了 carryover 混杂的可能性”。
6. “眼动提供最稳定客观行为证据”等证据价值判断。
7. “EEG 支持认知负荷/注意机制/神经效率”。
8. “45%/75% 最佳”、倒 U、连续剂量或最优 WWR 语言。

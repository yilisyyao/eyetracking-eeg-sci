# AUDIT EXECUTIVE SUMMARY

1. **3.2 是否有真正的数值矛盾？** 核心 14 个 CR2 BH-FDR 结果、13/14 个主模型支持、唯一的 Window Share WWR45×C1 companion-only、Holm 两两比较及 round/position 的 q 值范围均可由 0805 输出复现；未发现会改变 3.2 结论的数值错误。需要纠正的是推断说明与样本说明，而不是 Table 5 数字。

2. **3.2 的 Methods–Results/legacy 问题？** 有。眼动 BH 实际是两个独立的 42-test families；六个 primary models 之外另有两个 companion LMMs；Table 5 CI 是主模型 model-based CI，不是 CR2 CI；EEG-common 眼动敏感性样本是 34/302；sequence 进入模型但主文未交代。FCR/TFD/TTFF/visited、binary GLMM 与 Equipment Share 的最终模型不是成功的核心分析，应删除、降级或明确失败/探索性地位。

3. **3.3 最关键 unresolved 是否仍是 factor-level finding 的版本归属？** 不是。版本归属已经解决：该 finding 是 2026-08-18 用 0805 common-QC 输入（42/461）补做的 LMM+CR2 factor-level reanalysis。数值可复现；真正未解决的是能否称为预设/确认性分析，以及作者是否正式把它纳入最终分析体系。当前 260905 只介绍了 96 tests，却漏写四窗口均校正显著的 occipital-theta C1−C0 finding，这是 CRITICAL。

4. **0/5/10/15 s 是否真实 equal-status？** 在 0805 最终管线中，它们被同样建模并以 common-QC 做平行推断，因此可称“final pipeline 中 parallel”。但现有文件不能证明四窗口在查看结果前已经共同预设；而 0805 methods report 还保留“10-s backwards-compatible reference”的历史痕迹。投稿时不宜无证据写“prospectively prespecified equal status”。

5. **哪些结果可安全使用？** 可用：3.2 Table 5/14 effects、18-row Holm 表、3.3.2 四个 Model 1 common-QC 系数、144/324 的零校正结论、3.3.3 temporal 数字、P-beta 15-s omnibus q=.0282（仅 supplementary/hypothesis-generating）、previous-scene 两个 raw hits 且零校正结论、756 descriptive comparisons。需暂停或修正后再用：occipital-theta factor-level finding（先明确 complementary 地位并补写）；previous-scene 的 461-trial 表述（实际分析 386）；1–30 Hz denominator（应为 1–45 Hz）；gray-screen recovery；旧 WWR45 theta peak/nonlinear/neural-efficiency/sport-experience 叙事；任何 WWR30 或旧四系数集合；“24 participants”摘要表述。

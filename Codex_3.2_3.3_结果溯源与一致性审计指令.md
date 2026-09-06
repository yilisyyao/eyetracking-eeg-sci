# Codex 指令：3.2 眼动 + 3.3 EEG 结果溯源与前后一致性审计

## 任务目标

请对当前稿件中的 **3.2 Eye-Tracking Results** 与 **3.3 EEG Results** 做一次“结果溯源 + 前后一致性审计”。

这一步 **不要重写论文正文，不要重新分析数据，不要根据正文猜测答案**。请优先从实际分析脚本、输出 CSV/XLSX/JSON/RDS、模型对象、日志、图表生成文件、machine-readable supplementary outputs 中追溯每一个结果的来源。

当前稿件母本优先使用：

- `260905-final1_Methods_and_new_3.1_highlighted.docx`

如需要追溯历史变化，可以查看旧稿或旧分析输出，但 **旧稿只能用于解释“为什么数值发生变化”，不能反过来覆盖当前最终结果**。

---

# 一、审计原则

1. **Source of truth 优先级**：最终分析脚本 / 最终输出表 > 模型对象 / 日志 > 当前稿件正文 > 旧稿。
2. 每一个结论必须给出：
   - 最终准确数值；
   - 对应分析样本；
   - 模型类型；
   - reference coding / factor coding；
   - multiple-testing family；
   - 校正方法；
   - 来源文件路径；
   - 生成该结果的脚本或函数。
3. 如果正文与输出不一致，不要自动选择正文。请标记为 `CONFLICT`，说明哪一个版本应作为最终值及理由。
4. 如果某项无法由现有文件确认，请标记为 `UNRESOLVED`，不要推测。
5. 此轮只做审计与溯源，不要为了“让论文更好看”删除负结果或改写分析历史。
6. 特别区分：
   - raw / unadjusted p；
   - CR2 p；
   - Holm-adjusted p；
   - BH-adjusted q；
   - primary-model inference；
   - companion/robustness inference；
   - descriptive sensitivity evidence。

---

# 二、3.2 Eye-Tracking：需要重点核对的问题

## A. Methods 与 Results 是否存在直接矛盾

### ET-01. temporal/order covariates 的适用范围是否写错

当前 `2.5 Procedure` 写法倾向于：

> viewing round, within-round presentation position, and sequence group were retained in the questionnaire models...

但 `2.7.2` 又写：

> All eye-tracking models used ... temporal/order covariates...

且 `3.2.3` 实际报告了 round 与 within-round presentation position 的眼动结果。

请确认：

- round / within-round position / sequence group 是否实际进入了 **全部 6 个核心眼动模型**？
- 如果是，`2.5` 的 “questionnaire models” 是否只是残留旧措辞，应改为更广义的 “statistical models / modality-specific models”？
- EEG 中是否也使用了这些变量？

输出最终应统一的变量名称和适用模态。

---

### ET-02. “All six fitted eye-tracking models converged” 是否准确

当前 2.7.2 定义：

- 6 个 core eye-tracking outcomes；
- Table Share 与 Window Share 各有 1 个 primary ordered-beta model + 1 个 companion LMM；
- 另外 4 个 outcome 用 LMM。

因此实际拟合模型至少可能是：

- 6 个 primary models；
- 再加 2 个 companion LMMs；
- 合计 8 个核心拟合对象。

请确认 `3.2.2` 中：

> All six fitted eye-tracking models converged successfully

到底是指：

- 6 个 primary models；还是
- 所有模型（若所有则数字可能不对）。

请给出所有 core + companion 模型的实际数量、模型名称、是否收敛、是否 singular。

---

## B. CR2 / BH-FDR / primary-model 逻辑是否完全一致

### ET-03. 眼动 CR2 BH-FDR family 到底有多少个检验

`2.7.2` 目前只写：

> BH-FDR correction was applied to the prespecified coefficient family used for the companion/CR2 inference.

但没有写 family size。

请明确列出：

- 6 个 core outcomes；
- 每个 outcome 纳入哪些 non-intercept coefficients；
- WWR 是否以 2 个 dummy coefficients进入；
- sequence group 若为多水平，贡献几个 coefficients；
- round、position 是否纳入同一个 BH family；
- family 总测试数是多少；
- BH 是一次对全部 core coefficients 联合校正，还是按 outcome / model 分别校正。

请生成完整公式，例如：

`6 outcomes × X coefficients = N tests`

并指出当前正文 `14 non-intercept effects met the CR2 BH-FDR criterion` 的 q 值来自哪一个精确 family。

---

### ET-04. “14个 CR2-BH 显著、13个 primary 也支持” 是否可完全复现

请从最终输出中逐条列出这 14 个 effects：

- outcome；
- effect；
- primary model estimate / CI / p；
- companion or CR2 estimate / SE / p；
- BH q；
- evidence classification。

确认是否确实只有：

> Window Share: WWR45 × C1

属于 companion-only，其余 13 个均满足 primary-model criterion。

若不是，请标记冲突。

---

### ET-05. “primary-model criterion” 对不同 outcome 的定义是否一致、是否写清楚

当前结构中：

- Table Share / Window Share：primary = ordered-beta；companion = LMM + CR2；
- 其余 4 个 outcome：primary = LMM，CR2 是同一线性模型的 robust inference layer。

请确认：

1. 对 Table Share / Window Share，primary criterion 是什么？
   - likelihood p < .05？
   - 95% CI excludes 0？
   - 两者之一或两者都要？
2. 对另外 4 个 LMM outcomes，所谓 “primary-model criterion” 是什么？
   - conventional model-based p / CI？
   - 还是 CR2 本身就是主要 inference？
3. `Concordant` 这一标签是否在 6 个 outcome 上使用同一逻辑？

如果不同 outcome 的“concordant”实际含义不同，请建议更精确的 Methods 定义，但本轮先不要改正文。

---

### ET-06. Table 5 中 LMM 的 95% CI 到底是哪一种 CI

例如：

> Table–Window Share Difference, C1: β = −0.105, 95% CI [−0.156, −0.055], CR2 p < 0.001, q < 0.001

请确认这个 95% CI 是：

- conventional LMM model-based CI；还是
- CR2 robust CI；还是
- 其他算法。

对 Table Share / Window Share ordered-beta 的 CI 也请确认来源。

最终要求 Table 5 每一列的 inferential scale / CI source 明确无歧义。

---

## C. exercise-frequency coding 与解释是否可能反向

### ET-07. “WWR75 × low exercise frequency” 的 coding 必须溯源

当前 Table 5 与 3.2.3 报告：

> WWR75 × low exercise frequency

请确认：

- exercise-frequency factor 的 reference level 是 low 还是 high？
- 软件内部 contrast coding 是什么？
- 这个 coefficient 的实际含义是什么？
- β = −0.499（Table Share）与 β = −0.117（Table–Window Share Difference）的方向应如何解释？

请不要根据标签猜。请从 model matrix / factor levels / contrasts 设置中确认。

同时确认全文使用的是：

- exercise frequency；
- sport experience；
- sports-specific experience；

哪一个才是当前真实变量定义。当前变量实际来自 Q1.4 exercise frequency，不应因旧稿概念而被误标。

---

## D. temporal/order 结果是否报告完整

### ET-08. sequence group 为什么在 Methods 中进入模型，但 3.2.3 没有报告

`2.7.2` 表示所有眼动模型包含 temporal/order covariates；`2.5` 明确列出：

- viewing round；
- within-round presentation position；
- sequence group。

但 `3.2.3` 只报告：

> no coefficient for round or within-round presentation position met CR2 BH-FDR (q = 0.255–0.815)

请确认：

- sequence group 是否实际进入所有模型？
- 有几个 dummy coefficients？
- 是否纳入 BH-FDR family？
- 是否有任何 sequence coefficient 达到 raw p < .05 或 BH q < .05？
- 如果全不显著，为什么正文未提？是否应在 Supplementary 完整列出？

---

## E. 核心 outcome 与 Methods 中定义的其他 eye-tracking metrics 是否残留冲突

### ET-09. FCR / TFD / TTFF / visited 是否还属于当前分析

`2.6.2` 仍定义：

- fixation count rate (FCR)；
- total fixation duration (TFD)；
- time to first fixation (TTFF)；
- binary visited indicator。

`2.7.3` 还写：

> Binary eye-tracking outcomes, including the AOI-visited indicator, were analysed using generalized linear mixed models with a logit link.

但当前 `3.2` 核心结果只围绕 6 个 outcomes：

1. Table Share
2. Window Share
3. Table–Window Share Difference
4. Log Table Enrichment
5. Log Window Enrichment
6. Table–Window Enrichment Difference

请追溯并确认：

- FCR / TFD / TTFF / visited 是否仍被正式建模？
- 如果是，结果放在哪里？是否为 supplementary？
- 如果没有进入当前最终分析，Methods 中是否属于 legacy text，应删除或降级为“derived but not used”？
- binary GLMM 的描述是否仍有必要保留？

这是一个重要的 Methods–Results 一致性问题。

---

### ET-10. Equipment Share 的地位是否清楚

`2.6.2` 定义了 Equipment Share，但 core six outcomes 中没有 Equipment Share，3.2 主文也基本没有报告。

请确认：

- Equipment Share 是否只用于描述？
- 是否在 C1-only 数据中建模过？
- 是否有 supplementary 结果？
- 当前最终稿是否应明确说 Equipment Share 不属于六个 core inferential outcomes，原因是 C0 中 structurally absent？

---

## F. pairwise WWR comparisons 是否存在选择性报告风险

### ET-11. Holm pairwise comparisons 的完整集合

Methods 写：

> WWR pairwise comparisons were evaluated separately within outcome using Holm adjustment.

Results 只明确报告了部分 outcome 的 pairwise results。

请确认：

- 是否对 6 个 core outcomes 都做了 WWR15–45、15–75、45–75 三组 pairwise？
- 还是只在某个 omnibus WWR criterion 达标后才做？
- 每个 outcome 的 Holm family 是 3 个 pairwise comparisons 吗？
- Table Share、Log Table Enrichment、Table–Window Enrichment Difference 中是否有未写入正文的 pairwise结果？

请输出完整 pairwise 表及 source path。

---

## G. sensitivity analyses 的样本与执行范围必须明确

### ET-12. alternative tracking thresholds 的实际样本量

请给出：

- 50% threshold：participants / trials；
- 60% threshold：46 participants / 434 trials 是否确认；
- 70% threshold：participants / trials。

并确认这些阈值下 14 个 CR2-BH effects 的方向是否全部一致。

---

### ET-13. EEG-common eye-tracking sample 到底是哪一套样本

3.2.3 写 sensitivity analyses 包含：

> EEG-common sample

请确认这是：

- EEG 四窗口 common-QC 的 42 participants；还是
- 只要有合格 EEG 数据的 participant subset；还是
- 其他定义。

并给出该眼动敏感性分析实际 participants / trials。

---

### ET-14. leave-one-participant-out 是否所有 refit 都成功

请确认：

- 一共进行了多少次 leave-one-participant-out refits；
- 是否所有 primary / companion models 都成功拟合；
- “available estimates” 是否意味着有缺失/失败模型；
- 若有，请列出失败情况。

---

### ET-15. ±5-pixel AOI-boundary perturbation 到底只用于哪些 outcomes

当前 3.2.3 明确写：

- Table–Window Share Difference；
- Table–Window Enrichment Difference。

但 Methods 的概括较宽。

请确认实际是否只对这两个 outcomes 做 perturbation sensitivity。如果是，Methods 应精确到这两个 outcome，不要让人误以为六个 core outcomes 全都做了边界扰动分析。

---

## H. 3.2 描述统计与模型结果的方向是否一致

### ET-16. 逐项核对 3.2.1 descriptive means 与 3.2.2 model coefficients

请自动检查以下方向是否一致或至少不冲突：

- Window Share 随 WWR15→45→75 的描述趋势；
- Table Share 在 C0 / C1 下的趋势；
- Table–Window Share Difference 的趋势；
- C1 main effect；
- WWR75 × C1 interaction。

如果某个模型系数方向与 raw descriptive pattern 看似相反，请解释是否由 reference coding / covariate adjustment / interaction parameterization 导致。

---

# 三、3.3 EEG：需要继续溯源的核心问题

## EEG-01. factor-level visual complexity → occipital theta 是否仍属于当前最终分析

请确认在当前最终分析中：

- visual complexity factor 对 occipital theta relative power 是否在 0/5/10/15 s 四个 onset-trim variants 中都达到 cross-variant CR2 BH-FDR？
- 此前出现过的：
  - C1–C0 = 0.00436–0.00503；
  - cross-variant q = 0.00205–0.00443；
  是否属于当前最终分析结果。

必须给出每个窗口：

- estimate / marginal difference；
- CR2 SE；
- 95% CI；
- raw CR2 p；
- within-window q；
- joint/cross-variant q；
- sample；
- source file / script。

---

## EEG-02. 96-test factor-level family 与 144-test coefficient-level family 为什么可能得出不同校正结论

当前稿件同时存在：

- 96 factor-level tests；
- 144 reference-coded coefficient tests。

请明确：

- 6 个 factor 是什么；
- factor test 用什么 CR2 Wald/F test；
- visual complexity 只有两个水平时，factor-level test 与 C1 coefficient 的 estimate / raw p 是否完全等价；
- 如果 raw p 相同而 BH q 不同，是否仅由 family size / p-value distribution 不同造成；
- 如果 raw p 本身不同，则原因是什么。

要求给出真实输出证明，而不是统计学推测。

---

## EEG-03. 当前 WWR45 × C1 frontal-theta 四个系数的最终版本

当前 260905 稿写：

- 0 s: β = 0.00757, raw CR2 p = 0.0288
- 5 s: β = 0.00856, p = 0.0132
- 10 s: β = 0.00750, p = 0.0334
- 15 s: β = 0.00475, p = 0.1704

旧分析曾出现另一套：

- 0.00995 / 0.00935 / 0.00841 / 0.00549

请追溯差异具体来源：

- common-QC sample？
- fixed effects？
- exercise-frequency recoding？
- gender adjustment？
- round / position / sequence adjustment？
- reference coding？
- QC pipeline？
- CR2 implementation？
- 不同脚本或不同数据生成批次？

最终明确哪一套是唯一 current final values。

---

## EEG-04. 0/5/10/15 s 到底是 equal-status parallel analyses，还是 primary + sensitivity windows

请根据分析历史、脚本版本、分析计划和输出生成顺序确认，不要依据当前正文倒推。

请回答：

- 四窗口是在正式推断前就同时确定的吗？
- 还是先有某个主窗口，后增加其他窗口检查 early-scene transient？
- `equal analytical status` 是否真实反映分析历史？

这决定 Methods 能否写成 “four parallel variants of equal status”。

---

## EEG-05. 96 factor-level tests 的精确组成

请确认 6 factors 是否为：

1. WWR
2. visual complexity
3. exercise frequency
4. WWR × visual complexity
5. WWR × exercise frequency
6. visual complexity × exercise frequency

并确认：

`4 core outcomes × 6 factors × 4 windows = 96 tests`

每个多自由度 factor 的 CR2 检验方式也要说明。

---

## EEG-06. broader factor-level audit 的 family size 与 q = 0.0282 的来源

当前 3.3.4 有：

> parietal beta relative-power WWR factor, 15-s q = 0.0282

请确认：

- broader factor-level audit 总测试数；
- 是否为 9 outcomes × 6 factors × 4 windows = 216 tests；
- q = 0.0282 是：
  - within-window q？
  - joint cross-window q？
  - 来自 96 family、216 family，还是其他 family？

并列出 0/5/10/15 s 对应的 raw p 和 q。

---

## EEG-07. condition-related log10 absolute-power factor-level sensitivity 的 family 组成

请明确：

- outcomes 数量；
- factors 数量；
- windows 数量；
- 总 tests；
- within-window / joint BH family；
- 是否存在任何 corrected finding。

---

## EEG-08. temporal 72-test families 的精确组成

当前写 relative-power 与 absolute-power 各有 separate 72-test family。

请确认是否为：

`9 outcomes × 2 temporal predictors × 4 windows = 72 tests`

其中 predictors 是否恰为：

- viewing round；
- within-round presentation position。

请列出 9 EEG outcomes 的准确名称，并确认 low beta / high beta 是否包含在这 9 个 outcome 中。

---

## EEG-09. previous-scene 48 coefficients 如何组成、首个 scene 如何处理

请确认是否为：

`4 core outcomes × 3 previous-scene coefficients × 4 windows = 48`

3 previous-scene coefficients 是否为：

- Previous WWR45
- Previous WWR75
- Previous C1

并确认：

- 每个 round 第一个 trial 无 previous scene 时怎么处理；
- 是否跨 round 连接 previous scene；
- missing trial 是否被模型自动删除；
- previous-scene 模型实际 participants / trials；
- 48 coefficients 是否全部基于同一 common-QC sample。

---

## EEG-10. 756 onset-trim pairwise contrasts 的构成

请精确反推：

- 756 = 哪些 outcomes × 哪些 coefficients/factors × 6 window pairs；
- 比较的是 model coefficients、marginal means、还是其他量；
- 使用 common-QC 还是 window-specific QC；
- CI 的计算方法；
- 是否有任何 formal p test；
- 为什么被定义为 descriptive sensitivity analysis；
- 是否真正用于选窗口。

---

## EEG-11. common-QC 42 participants / 461 trials 的适用范围

请分别确认下列分析是否都使用 common-QC：

- 144 coefficient tests；
- 96 factor tests；
- broader 324 coefficient audit；
- broader factor audit；
- temporal 72-test relative family；
- temporal 72-test absolute family；
- previous-scene models；
- onset-trim direct contrasts。

如果任何分析使用 window-specific QC，请单独列出。

---

## EEG-12. block / round / position / sequence 的变量命名和模型使用必须统一

当前文本中出现：

- experimental block；
- viewing round；
- within-block presentation position；
- within-round presentation position；
- sequence group。

请确认：

- block 是否就是 round；
- EEG 最终模型是否包含 sequence group；
- temporal 72-test family 是否只检验 round 与 position，而 sequence 只是 adjustment variable；
- 最终建议统一变量名。

---

# 四、跨 3.2 与 3.3 的共同一致性检查

## CROSS-01. round / position / sequence 在三种模态中的角色

请输出一张表，分别列 Questionnaire / Eye tracking / EEG：

- round 是否进入 primary model；
- position 是否进入 primary model；
- sequence 是否进入 primary model；
- 是否参与 multiplicity correction；
- 是否作为 substantive result 报告；
- 是否只是 adjustment covariate。

---

## CROSS-02. exercise frequency 的定义与 reference coding

请确认 Questionnaire / Eye tracking / EEG 三种模型中：

- 使用的是同一个 Q1.4 low/high classification；
- low/high participant counts；
- reference level；
- contrast coding；
- 命名是否统一。

特别检查是否仍有旧稿中的 `sport experience / high-experience / low-experience` 残留导致方向或含义误读。

---

## CROSS-03. 当前稿件中哪些 Methods 内容属于 legacy analysis

请扫描 2.6–2.7，标记所有目前 Results 不再对应的旧分析描述，例如可能包括：

- FCR / TFD / TTFF / visited；
- post-stimulus recovery / ΔO_alpha；
- old EEG outcomes；
- three-way interactions；
- 旧的 group definition；
- 旧的 nonlinear/quadratic analysis；
- 任何已不再生成结果的 sensitivity procedure。

每项标记：

- KEEP
- MOVE TO SUPPLEMENTARY
- DELETE AS LEGACY
- UNRESOLVED

不要直接改文稿。

---

# 五、最终必须输出的文件 / 表格

请生成以下结果，优先输出 Markdown + CSV：

## Output 1. `FINAL_SOURCE_OF_TRUTH_MATRIX.md`

列：

| Section | Outcome | Effect / Factor | Model | Sample | Estimate | SE / CI | raw p | adjusted p/q | Correction family | Status | Source file | Script/function |

覆盖 3.2 与 3.3 主文中所有被报告的 inferential results。

---

## Output 2. `DISCREPANCY_AUDIT.md`

列：

| ID | Location | Current manuscript statement | Source output | Conflict type | Severity | Correct value / wording | Required action |

Severity：

- `CRITICAL`：会改变结论或数值；
- `MAJOR`：会造成统计逻辑/方法错误；
- `MINOR`：术语或表述不一致；
- `NONE`：核对后无问题。

---

## Output 3. `FINAL_ANALYSIS_FAMILY_MAP.md`

至少包含：

### Eye tracking
- 6 core outcomes；
- primary model type；
- companion model type；
- coefficient family size；
- BH-FDR scope；
- Holm pairwise scope；
- sensitivity analyses；
- sample sizes。

### EEG
- 4 core outcomes；
- 9 broader outcomes；
- 144 coefficient family；
- 96 factor family；
- broader coefficient family；
- broader factor family；
- relative temporal 72 family；
- absolute temporal 72 family；
- previous-scene family；
- onset-trim direct comparison；
- samples。

---

## Output 4. `QUESTIONS_STILL_UNRESOLVED.md`

只列无法从当前仓库/文件追溯确认的问题，不要猜答案。

---

# 六、最后汇总要求

最终请给一个不超过 1 页的总结，明确回答：

1. **3.2 当前是否存在真正的数值矛盾？有哪些？**
2. **3.2 当前是否存在 Methods–Results 结构矛盾或 legacy text？有哪些？**
3. **3.3 当前最关键的 unresolved issue 是否仍是 factor-level visual-complexity finding 的版本归属？**
4. **0/5/10/15 s 是否真实属于 equal-status parallel analyses？**
5. **当前哪些结果可以安全用于下一版正文，哪些必须先暂停使用？**

在完成以上审计前，请不要自动重写 3.2 / 3.3 正文。

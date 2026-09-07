# EEG四窗口CR2原始表与Codex BH校正的完整说明

生成日期：2026-09-07  
用途：供作者、学生及后续GPT/Codex进行Results 3.3统计溯源、一致性核查和正文改写。

## 一、结论摘要

1. 学生0805分析包中，与0、5、10和15 s四个onset-trim variant相对应的核心EEG CR2结果共有四张独立CSV表。每张表均包含β、CR2 SE、df和CR2 p，但没有BH-adjusted q。
2. 目录中还可看到四张名为`eeg_cr2_robust_results.csv`的表；经SHA256核验，它们分别与相应窗口的`09_eeg_order_CR2.csv`完全相同。因此这是“四张独立表各保存了两个同内容文件名”，不是八套独立结果。
3. “144项”不是凭空生成的数值，而是从上述四张表中按固定规则提取：4个核心EEG outcome × 9个Model 1条件相关项 × 4个onset-trim variant = 144个系数；每个variant为36项。
4. 144项的BH-adjusted q不是学生0805管线保留的原始输出，而是Codex于2026-08-09读取学生保存的CR2 p后进行的可复现后续校正。计算结果表和计算代码均仍存在。
5. 这组q值在统计上重要：如果正文报告三个unadjusted CR2 p < 0.05，就必须交代多重比较控制，否则容易把偶然小p值误写成EEG发现。Codex的BH复核显示，没有任何一个系数达到校正后的判定标准。
6. 但是，这组q值的来源身份必须写准确。它可以表述为“对归档CR2 p进行的post hoc multiplicity audit”，不能表述为“学生0805原始管线已经输出的BH结果”，也不能在缺乏运行前方案时称为“prospectively prespecified primary multiplicity family”。
7. 另一组temporal q（正确范围为0.00447–0.02239）来自2026-08-18的另一套post hoc complementary reanalysis，并非上述四张0805 CR2表直接包含的结果。后来正文中的0.00461–0.02239不是另一套正式结果，而是范围下限抄写/汇总错误。

## 二、0805四张独立CR2原始表的位置

共同目录：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat
```

### 0 s

原始表：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0297__06_eeg_primary_onset_window_models_trim_0s__09_eeg_order_CR2.csv
```

SHA256：

```text
2DE2006CCAAE1CD75D36693F621C121950CDACC7882AE53177563468E8017454
```

同内容别名副本：

```text
SRC0299__06_eeg_primary_onset_window_models_trim_0s__eeg_cr2_robust_results.csv
```

### 5 s

原始表：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0363__06_eeg_primary_onset_window_models_trim_5s__09_eeg_order_CR2.csv
```

SHA256：

```text
B7CC8B40EC24A5C12688AA72700DE7615CFEF13CC50EE6DC085CA96E4D4A40BD
```

同内容别名副本：

```text
SRC0365__06_eeg_primary_onset_window_models_trim_5s__eeg_cr2_robust_results.csv
```

### 10 s

原始表：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0319__06_eeg_primary_onset_window_models_trim_10s__09_eeg_order_CR2.csv
```

SHA256：

```text
7A6D5DBE783A2143789D33EDA70A17A2F1FED492782BDE32FD7754337A099845
```

同内容别名副本：

```text
SRC0321__06_eeg_primary_onset_window_models_trim_10s__eeg_cr2_robust_results.csv
```

### 15 s

原始表：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0341__06_eeg_primary_onset_window_models_trim_15s__09_eeg_order_CR2.csv
```

SHA256：

```text
F85B6B5C910AE108C64BA9291E29A4CA5D77939576DDDD638C54802115BB2511
```

同内容别名副本：

```text
SRC0343__06_eeg_primary_onset_window_models_trim_15s__eeg_cr2_robust_results.csv
```

### 表结构核验

四张表各有176行，列名均为：

```text
outcome, model, term, estimate, std.error, df, p.value
```

四个outcome为：

- `O_theta_relative`：occipital theta relative power；
- `F_theta_relative`：frontal theta relative power；
- `O_alpha_relative`：occipital alpha relative power；
- `O_beta_relative`：occipital beta relative power。

表中包含`Model0`、`Model1`和`PreviousScene`三类结果。它们确实没有BH-adjusted q列。

注意：0805包还包含其他用途的CR2文件，例如眼动、单一参考运行、secondary、supplemental及crossmodal结果。这里所称“四张CR2原始表”，特指四个onset-trim variant对应、用于144项核心Model 1系数审计的四张独立表。

## 三、Codex如何从四张原始表得到144项

### 1. 输入映射

Codex脚本将四个variant映射至四张学生原始表：

```python
window_prefix = {
    0: "SRC0297",
    5: "SRC0363",
    10: "SRC0319",
    15: "SRC0341",
}
```

### 2. 筛选规则

从每张表中仅保留：

- `model == "Model1"`；
- 下列9个条件相关项。

```text
WWRWWR45
WWRWWR75
ComplexityC1
ExperienceGroupLow
WWRWWR45:ComplexityC1
WWRWWR75:ComplexityC1
WWRWWR45:ExperienceGroupLow
WWRWWR75:ExperienceGroupLow
ComplexityC1:ExperienceGroupLow
```

因此：

```text
4 core outcomes × 9 condition-related terms = 36 coefficients per variant
36 coefficients × 4 variants = 144 coefficients
```

这144项不包括截距、viewing round、within-round presentation position和PreviousScene项。

### 3. 计算脚本

保留的计算实现位于：

```text
C:\Users\PCI\Documents\论文分析\analysis_workspace\reanalyze_results.py
```

关键位置：

- 第40–52行：Benjamini–Hochberg调整函数；
- 第369–375行：四张输入表和9个条件相关项；
- 第396行：提取Model 1的144项；
- 第397行：每个variant内对36个CR2 p进行BH调整；
- 第398行：将四个variant的全部144个CR2 p合并后进行联合BH调整；
- 第402行：输出144项结果表。

BH计算实现为标准步骤：将同一family内的有效p值从小到大排序；对第i个p值计算`p(i) × m / i`；从最大秩向最小秩进行累计最小值处理，以保证调整值单调；最后将结果截断至1。

核心代码为：

```python
def bh_adjust(values):
    values = pd.to_numeric(values, errors="coerce")
    result = pd.Series(np.nan, index=values.index, dtype=float)
    valid = values.dropna()
    order = valid.sort_values().index
    ranked = valid.loc[order].to_numpy(dtype=float)
    m = len(ranked)
    adjusted = ranked * m / np.arange(1, m + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    adjusted = np.minimum(adjusted, 1.0)
    result.loc[order] = adjusted
    return result

core144 = eeg_all[
    (eeg_all["model"] == "Model1") &
    eeg_all["term"].isin(condition_terms)
].copy()

core144["q_within_window_recomputed"] = (
    core144.groupby("window_s", group_keys=False)["p.value"]
    .apply(bh_adjust)
)
core144["q_joint_144_recomputed"] = bh_adjust(core144["p.value"])
```

### 4. Codex输出表

同一份输出保存于两个位置，SHA256完全相同：

```text
C:\Users\PCI\Documents\论文分析\analysis_workspace\audit_intermediates\analysis_eeg_core_condition_144.csv
```

```text
C:\Users\PCI\Documents\论文分析\Codex重分析并重写_Results3.2_3.3_20260809_0805主数据复核版_v2\analysis_eeg_core_condition_144.csv
```

SHA256：

```text
35364DE30609A024DDF68A841B025091A2EAAF875515331FD15635468858B253
```

该表为144行，包含学生原始β、SE、df和CR2 p，并新增：

- `q_within_window_recomputed`；
- `q_joint_144_recomputed`；
- 未校正及校正后阈值标记。

## 四、144项BH校正的数值结果

学生原始CR2 p中有三个小于0.05，均为frontal theta relative power的WWR45 × high-complexity condition (C1)项：

| onset-trim variant | β | CR2 SE | df | unadjusted CR2 p | variant内BH-adjusted q（36项） | 联合BH-adjusted q（144项） |
|---|---:|---:|---:|---:|---:|---:|
| 0 s | 0.0075658 | 0.0033269 | 37.5959 | 0.0287559 | 0.6502314 | 0.6684067 |
| 5 s | 0.0085610 | 0.0032905 | 37.5961 | 0.0131938 | 0.4749766 | 0.6684067 |
| 10 s | 0.0074981 | 0.0033953 | 37.5961 | 0.0333903 | 0.5243488 | 0.6684067 |

15 s的同一系数为：

| onset-trim variant | β | CR2 SE | df | unadjusted CR2 p | variant内BH-adjusted q（36项） | 联合BH-adjusted q（144项） |
|---|---:|---:|---:|---:|---:|---:|
| 15 s | 0.0047530 | 0.0034003 | 37.5962 | 0.1703561 | 0.7214136 | 0.6976589 |

总体计数：

```text
unadjusted CR2 p < 0.05：3/144
variant内BH-adjusted q < 0.05：0/144
联合144项BH-adjusted q < 0.05：0/144
```

所有144项中：

```text
最小variant内BH-adjusted q = 0.4749766
最小联合BH-adjusted q = 0.6684067
```

所以，“没有任何系数在variant内36项校正或联合144项校正后达到0.05”在数学上是可以复算并得到相同结果的。问题不在计算是否存在，而在于这一BH校正是后续Codex审计，不是学生0805原始输出。

## 五、Codex重新计算的q到底重不重要

### 重要之处

它对论文结论等级很重要。一次检查144个系数时，即使所有零假设均成立，也可能偶然出现若干unadjusted CR2 p < 0.05。当前恰有三个这样的p值；BH校正后，其q值均远高于0.05。因此这些结果不能作为经多重比较控制后成立的EEG condition-related finding，也不宜进入Abstract、Conclusion或headline/highlight。

如果正文要报告这三个unadjusted CR2 p < 0.05，建议同时报告校正结论。否则读者容易误以为它们是可靠的阳性发现。

### 限制之处

BH结果是否可被称为“primary”取决于检验family是否在查看结果前被确定。当前可以确认：

- 144个底层Model 1系数均来自学生0805原始表；
- BH算法和输出可复现；
- 但学生0805包没有保存36/144专属BH脚本或q结果表；
- 当前证据不足以证明“4 outcomes × 9 terms × 4 variants”在查看结果前已被指定为primary multiplicity family。

因此，q值得保留，但身份应定为“post hoc multiplicity audit”。这既不否定计算，也不把后续校正伪装成预设分析。

### 建议的投稿策略

优先建议：保留这项BH审计，将脚本、四张原始表的哈希和144项输出表一并归档，并在Methods/Results中明确为post hoc multiplicity audit。其价值是防止把三个孤立的unadjusted CR2 p误写为确定发现。

另一种更保守的方案：如果作者不希望在正式稿中引入任何后续校正，则不报告144项q，也不要突出三个未校正小p值；只说明没有保留可供验证的原始multiplicity-adjusted output。这个方案会丢失一层有用的误报控制信息。

## 六、建议写入Methods和Results的文字

### Methods英文建议

> As a post hoc multiplicity audit, the archived CR2 p values for four core EEG outcomes and nine Model 1 condition-related terms were extracted from each of the 0-, 5-, 10-, and 15-s onset-trim variants (36 coefficients per variant; 144 coefficients in total). The Benjamini–Hochberg false discovery rate procedure was applied separately within each variant and jointly across all 144 coefficients. This adjustment was reconstructed from the archived 0805 CR2 coefficient tables and was not part of the retained student-generated output.

### Methods中文对照

> 作为一项事后多重比较审计，从0、5、10和15 s onset-trim variant的归档CR2结果表中提取四个核心EEG outcome和九个Model 1条件相关项，每个variant包含36个系数，共144个系数。Benjamini–Hochberg false discovery rate procedure分别应用于每个variant内的36个系数以及全部144个系数的联合family。该校正由归档的0805 CR2系数表重建，并非学生原始管线中保留的输出。

### Results英文建议

> Across the 144 archived Model 1 condition-related coefficients, three had unadjusted CR2 p < 0.05, all for the WWR45 × high-complexity condition (C1) term in frontal theta relative power at the 0-, 5-, and 10-s onset-trim variants. In the post hoc multiplicity audit, none met the CR2 BH-FDR criterion either within the corresponding 36-coefficient variant or jointly across all 144 coefficients (minimum within-variant BH-adjusted q = 0.475; minimum joint BH-adjusted q = 0.668). These isolated unadjusted coefficients were therefore not treated as corrected evidence of a condition-related EEG effect.

### Results中文对照

> 在归档的144个Model 1条件相关系数中，有3个系数的unadjusted CR2 p < 0.05，均对应0、5和10 s onset-trim variant中frontal theta relative power的WWR45 × high-complexity condition（C1）项。在事后多重比较审计中，没有任何系数在相应variant内的36项校正或全部144项联合校正后达到CR2 BH-FDR criterion（最小variant内BH-adjusted q = 0.475；最小联合BH-adjusted q = 0.668）。因此，这些孤立的未校正系数不被视为condition-related EEG效应的校正后证据。

### 不建议继续使用的写法

在缺乏运行前分析计划的情况下，不建议写：

> The primary multiplicity family comprised 144 coefficients.

也不建议将这组q描述为：

> the BH-adjusted q values generated by the original 0805 student pipeline

## 七、temporal q与144项q不是同一套结果

### 1. 144项q

- 底层模型系数：学生0805四张CR2表；
- 后续操作：2026-08-09 Codex仅对已保存CR2 p进行BH调整；
- 不需要重新拟合LMM；
- 输出：`analysis_eeg_core_condition_144.csv`。

### 2. temporal q

- 学生0805四张表不能提供完整的18-outcome temporal factor-level结果；
- 2026-08-18另行从0805 common-QC输入拟合/汇总temporal adjustment coefficients；
- 上游R脚本：

```text
C:\Users\PCI\Documents\论文分析\work\eeg_audit\reanalyse_factor_tests.R
```

- BH汇总脚本：

```text
C:\Users\PCI\Documents\论文分析\work\eeg_audit\summarize_temporal.py
```

- 结果表：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\EEG再发现\reanalysis_out\temporal_CR2_tests.csv
```

- 结果表SHA256：

```text
ACAB6CEB51D763DF0737FEB67D11B132429283850E18BC923E366A4046DB8A0B
```

对于viewing round与frontal、parietal和occipital ROI theta relative power的12项组合，联合BH-adjusted q的正确范围是：

```text
0.004466...–0.022387...
```

按五位小数报告为：

```text
0.00447–0.02239
```

2026-09-06双语正文生成脚本中的`0.00461–0.02239`遗漏了更小的`0.004466...`，属于范围汇总/抄写错误，不是新的分析结果。若保留temporal段落，应改为`0.00447–0.02239`，并明确其为2026-08-18的post hoc complementary reanalysis；若仅接受学生0805原始输出，则应删除完整temporal q段落。

## 八、为什么后续正文会出现这些q

### 144项BH

2026-08-09的Codex复核先生成了144项结果表，随后报告生成脚本将“3个unadjusted CR2 p < 0.05、校正后0项”写入Results 3.3。相关正文生成位置为：

```text
C:\Users\PCI\Documents\论文分析\analysis_workspace\generate_reports.py
```

关键位置约为第192–196行和第749–752行。问题在于当时正文把后续审计写成了“primary multiplicity family”，超过了现有溯源证据。数值本身可复算，分析身份措辞需要降级。

### temporal q

`q = 0.00447–0.0224`首先出现在2026-08-18的重写脚本中：

```text
C:\Users\PCI\Documents\论文分析\work\eeg_audit\build_revised_33.py
```

关键位置约为第147–150行。随后2026-09-06双语生成脚本将下限误写为0.00461：

```text
C:\Users\PCI\Documents\论文分析\build_eeg_33_bilingual.py
```

关键位置约为第157–158行。

因此，两组q均有后续计算或结果表来源，并非完全虚构；但二者都不是学生0805包内已经存在的BH q，且必须区分“后续复核结果”和“原始学生输出”。

## 八-A、从原始材料到正文结论的完整证据链

本节是后续复核时应优先读取的“source-of-truth”说明。材料分为三层，不能混称。

### 第一层：学生0805原始分析材料

#### A. 用于144项BH审计的直接输入

直接输入就是第二节列出的四张`09_eeg_order_CR2.csv`。它们已经完成LMM的CR2 inference，保存了：

```text
β（estimate）
CR2 SE（std.error）
Satterthwaite df（df）
CR2 p（p.value）
```

这四张表是144项BH审计的最上游统计输入。Codex没有重新估计这四列，也没有改写学生模型系数；后续只对`p.value`列进行筛选和BH调整。

#### B. 用于2026-08-18模型重拟合的直接输入

8月18日factor-level和temporal complementary reanalysis使用的不是四张CR2表，而是0805包内四张participant/trial-level common-QC模型输入：

| variant | 学生0805原始输入文件 | n | SHA256 |
|---|---|---:|---|
| 0 s | `SRC0303__06_eeg_primary_onset_window_models_trim_0s__eeg_onset_order_model_input.csv` | 42 participants / 461 trials | `42B2BDF3D2B6289269C9761503D65BE748183D5DFE7E3F1E12EC98D7BC22285C` |
| 5 s | `SRC0369__06_eeg_primary_onset_window_models_trim_5s__eeg_onset_order_model_input.csv` | 42 participants / 461 trials | `E25F7F960B1E2C4232083DE54408265A73023F2E1C257EA484733A5167DF9D18` |
| 10 s | `SRC0325__06_eeg_primary_onset_window_models_trim_10s__eeg_onset_order_model_input.csv` | 42 participants / 461 trials | `B08C0C2308E698FA274DEB510681D7276C28DBE845F405FCD0462978F51E363B` |
| 15 s | `SRC0347__06_eeg_primary_onset_window_models_trim_15s__eeg_onset_order_model_input.csv` | 42 participants / 461 trials | `AB31595E65D1D118A881EAE83052DC7B2349C44BEA0C9F8D1AE45FD0625ED4EE` |

四张表的共同目录仍为：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat
```

它们是已经完成EEG频谱提取、条件合并和common-QC筛选后的模型输入，不是原始连续EEG `.set/.fdt`数据。它们足以复现8月18日的统计模型，但不能单独追溯最上游EEGLAB filtering、notch、re-reference和ICA操作。

### 第二层：Codex后期计算及其算法

#### A. 2026-08-09：144项BH审计

计算性质：不重新拟合模型，只读取四张学生CR2表，提取4 × 9 × 4 = 144个Model 1系数，并对原始`p.value`执行BH调整。

两种family：

```text
variant内family：每个variant 36项，分别执行BH
联合family：四个variant合计144项，共同执行BH
```

原始实现：

```text
C:\Users\PCI\Documents\论文分析\analysis_workspace\reanalyze_results.py
```

为避免以后必须从大型历史脚本中再次拆解，现已另存一个独立、只处理本问题的复现脚本：

```text
C:\Users\PCI\Documents\论文分析\recompute_eeg_core144_bh.py
```

SHA256：

```text
BF319870D12A6EFD9140F663C7AAD2AB0E69EF848725D2ABAD369B102DDD449F
```

运行方式：

```bash
python recompute_eeg_core144_bh.py \
  "D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat" \
  "EEG_core144_BH_recomputed.csv"
```

独立脚本会自动：

1. 按`SRC0297`、`SRC0363`、`SRC0319`和`SRC0341`定位四张canonical CR2表；
2. 核验七个必需列；
3. 仅筛选4个核心outcome、`Model1`和9个条件相关项；
4. 强制核验每个variant恰有36行、总计144行；
5. 计算variant内36项BH-adjusted q；
6. 计算联合144项BH-adjusted q；
7. 在输出旁生成manifest，记录输入绝对路径、SHA256、行数、显著性计数和最小q。

本次重新运行生成：

```text
C:\Users\PCI\Documents\论文分析\EEG_core144_BH_recomputed_20260907.csv
C:\Users\PCI\Documents\论文分析\EEG_core144_BH_recomputed_20260907.manifest.json
```

对应SHA256：

```text
CSV      54FBC5753B454DE05F31A98843DAA212BB8F7F2C6F54E04AEE82DE88F091FACA
manifest BF6CCE8C78249F91C93210117432B1D95A26038AB1718307EC84885AD649F86E
```

将本次独立脚本输出与2026-08-09历史输出按`window_s + outcome + model + term`对齐后，原始CR2 p、variant内q和联合144项q的差异行数为0。因此，144项q结果已被第二种独立入口完整复现。

#### B. 2026-08-18：factor-level与temporal complementary reanalysis

此步骤与144项BH审计不同：它从四张participant/trial-level模型输入重新拟合LMM，而不是读取四张CR2系数表。

R脚本：

```text
C:\Users\PCI\Documents\论文分析\work\eeg_audit\reanalyse_factor_tests.R
```

SHA256：

```text
2F4877508E384AD272B8BA221D51DA6454776D3BF37235616B19A86AAC5D2DF2
```

脚本将四张模型输入分别命名为`input0.csv`、`input5.csv`、`input10.csv`和`input15.csv`。对每个outcome拟合：

```text
outcome ~ WWR * Complexity
        + WWR * exercise-frequency group
        + Complexity * exercise-frequency group
        + Gender
        + viewing round
        + within-round presentation position
        + OrderGroup
        + (1 | Participant)
```

具体计算为：

- `lme4::lmer(..., REML = TRUE)`拟合participant随机截距LMM；
- `clubSandwich::vcovCR(..., cluster = Participant, type = "CR2")`计算participant聚类CR2协方差；
- `clubSandwich::coef_test(..., test = "Satterthwaite")`输出β、CR2 SE、df和CR2 p；
- factor-level检验使用`clubSandwich::Wald_test(..., test = "HTZ")`；
- WWR、visual complexity及exercise frequency的边际主效应由`emmeans(..., weights = "equal")`构造；
- 18个outcome × 4个variant共拟合72个模型。

R脚本输出：

```text
coefficient_CR2_crosscheck.csv
factor_level_CR2_tests.csv
factor_level_CR2_signals.csv
model_diagnostics.csv
relative_power_simple_CR2_contrasts.csv
```

随后Python脚本：

```text
C:\Users\PCI\Documents\论文分析\work\eeg_audit\summarize_temporal.py
```

SHA256：

```text
8BCBBB44CEC189E9C6C1E4B0FD5E5EC142296C078F736F29C3B049DEEE5D208B
```

从`coefficient_CR2_crosscheck.csv`中选择viewing round和within-round presentation position两个temporal adjustment variable，并分别构建core/broader、relative/log10 absolute BH family。正文所用的三ROI theta temporal q来自`broader_temporal_72`，即：

```text
9 broader relative-power outcomes
× 2 temporal adjustment variables
× 4 onset-trim variants
= 72 tests
```

其BH调整包括每个variant内18项和四variant联合72项。最终写出：

```text
temporal_CR2_tests.csv
```

### 第三层：Codex后期输出与正文

#### 144项BH输出

```text
analysis_eeg_core_condition_144.csv
```

它是“学生CR2 p + Codex后期BH列”的混合来源表。表内β、SE、df和p来自学生0805；两列q及阈值标记来自Codex 8月9日计算。

#### 8月18日输出

目录：

```text
D:\投稿desk\2026sci\260419投稿材料\260722\EEG再发现\reanalysis_out
```

这些文件全部属于Codex 8月18日post hoc complementary reanalysis，不能标为学生0805原始输出。

### 2026-09-07实际端到端复现结果

本次以0805四张common-QC模型输入作为唯一数据输入，重新运行保存的8月18日R脚本。以下五个新生成文件与`reanalysis_out`归档文件的SHA256逐一完全相同：

| 输出 | SHA256 |
|---|---|
| `coefficient_CR2_crosscheck.csv` | `35986A9890F74E25A0539139F13B3B4E3CD90CEDEE4D2CE6D27F0474D86FAAEC` |
| `factor_level_CR2_tests.csv` | `D7691526035B552600E05FE5E308CC8DB819FDE124250B6AF293C59933C11553` |
| `factor_level_CR2_signals.csv` | `E4C1B98E770F2DA488DBDFE33C07ED576D9C5793D200943C710F75FD0B5DC70E` |
| `model_diagnostics.csv` | `682A309210AB8376290106BC9FA0AED791B3044A03E021F912CB86558F4B837A` |
| `relative_power_simple_CR2_contrasts.csv` | `9AC2D6F2C073F3DE3D321B89C5CABB4ECEF5C32BF56A8279F5E879036092DA7F` |

再以新生成的`coefficient_CR2_crosscheck.csv`运行`summarize_temporal.py`，所得文件与归档`temporal_CR2_tests.csv`的SHA256也完全相同：

```text
ACAB6CEB51D763DF0737FEB67D11B132429283850E18BC923E366A4046DB8A0B
```

这次端到端复现消除了“8月18日输入究竟是不是0805模型输入”的疑问。可以确认：8月18日统计结果由上述四张0805 common-QC模型输入、保存的R脚本及Python BH汇总脚本生成。

R运行时反复出现的`Results may be misleading due to involvement in interactions`是`emmeans`在模型含交互项时对边际主效应发出的通用提示，不是模型报错。边际主效应必须继续写成在其他因子上等权平均的marginal contrast；不能将其误写为不受交互影响的简单主效应。

## 八-B、以后重新拿到材料时的一次性核验清单

### 若只核验144项BH结论

必须同时具备：

1. 四张`09_eeg_order_CR2.csv`；
2. 每张表的SHA256与本说明第二节一致；
3. `recompute_eeg_core144_bh.py`；
4. 运行后生成的CSV和manifest；
5. 核验manifest显示`36 × 4 = 144`、计数为`3/0/0`、最小q为`0.4749766/0.6684067`。

具备这些材料后，不需要原始`.set/.fdt`即可核验144项BH，因为此步骤只对已经生成的CR2 p进行多重比较调整，不重新拟合模型。

### 若核验8月18日factor-level或temporal结论

必须同时具备：

1. `SRC0303`、`SRC0369`、`SRC0325`和`SRC0347`四张common-QC模型输入；
2. 四张输入的SHA256与本说明一致；
3. `reanalyse_factor_tests.R`；
4. `summarize_temporal.py`；
5. R包`lme4`、`emmeans`、`clubSandwich`和`readr`；
6. 重新生成的六个输出与本说明所列SHA256一致。

具备这些材料后，不需要回查8月18日Word正文来判断数值；应以脚本和CSV为准。若正文与CSV冲突，正文必须修改。

### 若核验EEG频谱值本身或上游预处理

上述材料仍然不够。此时还需要：

- 原始及预处理后的`.set/.fdt`；
- EEGLAB `EEG.history`或人工操作日志；
- filtering、notch、average re-referencing和ICA参数；
- ICA算法、成分删除记录及ICLabel/人工判定证据；
- 从预处理EEG到trial-level band-power表的MATLAB/Python脚本；
- relative power分母频率范围的实际代码；
- 各级文件哈希和软件版本。

这一区分很重要：四张CR2表足以核验BH；四张common-QC模型输入足以核验8月18日统计重拟合；只有`.set/.fdt`及频谱提取管线才能核验更上游的EEG预处理和功率计算。

## 九、最终来源等级

| 内容 | 底层数据/结果是否存在 | 原始学生输出是否含q | 后续计算是否可复现 | 建议身份 |
|---|---|---|---|---|
| 四窗口β、SE、df、CR2 p | 是，0805四张CR2表 | 不适用 | 是 | 学生0805原始结果 |
| 144项variant内及联合BH-adjusted q | 是，基于上述CR2 p | 否 | 是，脚本和144项表均在 | post hoc multiplicity audit |
| temporal q | 是，基于0805 common-QC输入后续重拟合 | 否 | 是，R/Python脚本和结果表均在 | post hoc complementary reanalysis |
| `0.00461–0.02239`范围 | 个别0.00461值存在，但不是正确最小值 | 否 | 否，不能复现为完整theta范围 | 更正为`0.00447–0.02239`或删除 |

## 十、后续归档建议

建议在GitHub或正式分析归档中同时保存：

1. 本说明文件；
2. 四张`09_eeg_order_CR2.csv`及其SHA256；
3. `recompute_eeg_core144_bh.py`；
4. `EEG_core144_BH_recomputed_20260907.csv`及manifest；
5. 历史`reanalyze_results.py`和`analysis_eeg_core_condition_144.csv`；
6. 若保留factor-level或temporal结果，保存四张common-QC模型输入及其SHA256；
7. `reanalyse_factor_tests.R`、`summarize_temporal.py`及`reanalysis_out`中的六个机器输出；
8. 一个README，明确“0805 student output”“2026-08-09 post hoc multiplicity audit”和“2026-08-18 post hoc complementary reanalysis”三个层级。

这能保证后续GPT、合作者或审稿人不会再次把学生原始输出、Codex后续BH校正和8月18日的重拟合结果混为一谈。

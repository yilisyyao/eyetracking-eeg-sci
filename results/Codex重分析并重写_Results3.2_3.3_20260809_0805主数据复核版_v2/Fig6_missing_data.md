# Fig. 6 missing data

Fig. 6（六场景眼动热图）当前**不能绘制**。底层 fixation 与 trial-QC 文件齐全，但 0803/0805 包中只有 12 张 `*_ValidScene.png` 二值/有效场景掩膜，没有六张正式 VR 场景底图。掩膜不能替代场景底图。

## 已有文件

- `SRC0049__02_eye_stage2__01_fixation_event_level_data.xlsx`  
  完整路径：`D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0049__02_eye_stage2__01_fixation_event_level_data.xlsx`  
  关键字段：Participant、GlobalTrialOrder、FixationIndex、FixationX、FixationY、FixationDuration、ValidSceneHit、SceneID、WWR、Complexity。
- `SRC0050__02_eye_stage2__02_trial_quality_control.xlsx`  
  完整路径：`D:\投稿desk\2026sci\260419投稿材料\260722\数据分析结果包-0805（对齐眼动eeg）\filesource_flat\SRC0050__02_eye_stage2__02_trial_quality_control.xlsx`  
  关键字段：Participant、GlobalTrialOrder、SceneID、WWR、Complexity、ValidTrackingRatio、TrackingPassPrimary、ValidSceneTFD、ConservationPass。

## 缺失的六个逻辑文件

原始包未保留精确原文件名；因此以下为必须补交的**条件级文件标识**，不能臆造原名：

1. `FORMAL_VR_BACKDROP_C0_WWR15.<png|jpg|tif>`
2. `FORMAL_VR_BACKDROP_C0_WWR45.<png|jpg|tif>`
3. `FORMAL_VR_BACKDROP_C0_WWR75.<png|jpg|tif>`
4. `FORMAL_VR_BACKDROP_C1_WWR15.<png|jpg|tif>`
5. `FORMAL_VR_BACKDROP_C1_WWR45.<png|jpg|tif>`
6. `FORMAL_VR_BACKDROP_C1_WWR75.<png|jpg|tif>`

每张底图还需提供：SceneID/条件映射、原始像素宽高、是否裁切/缩放、与 FixationX/FixationY 坐标系的对应关系。补齐后应只用 `TrackingPassPrimary==TRUE` 的 60% 主 QC 试次，并对六场景使用相同核带宽和同一色阶。

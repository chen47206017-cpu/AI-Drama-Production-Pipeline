# AI Drama Production Pipeline

AI短剧全流程生产系统。包含通用制作流程与独立剧本项目。

> **外部AI阅读入口：** [AI_START_HERE.md](AI_START_HERE.md)。请先确定项目分支与正文版本；GitHub仓库主页的默认分支不一定包含最新工作稿。

## 核心模块

- Canon一致性管理
- 人物资产管理
- 场景资产管理
- 分镜规划
- Prompt工程
- ComfyUI工作流
- Seedance / Wan模型生产
- 视频质量检查

## 项目案例

- 《楼上是25岁的我，楼下是未来女儿》（既有项目记录）
- [《双姝商途》](projects/shuangshu-shangtu/README.md) — 已导入V23.33R1全64集正文与外部AI审稿规范（PGS30 HOLD）。
  - [AI专用读取指南](projects/shuangshu-shangtu/AI_ACCESS_GUIDE.md)
  - [64集分集导航](projects/shuangshu-shangtu/EPISODE_INDEX.md)
  - [可复制全文审稿提示词](projects/shuangshu-shangtu/EXTERNAL_AI_REVIEW_PROMPT.md)

## 目标

建立可复制的AI短剧工业化生产流程。通用模块与各项目独立Canon/剧本数据分离，防止旧版设定交叉污染。

## 版本与权限须知

《双姝商途》V23.33R1已导入独立分支，并关联[PR #1](https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/pull/1)。在PR合并前，`main`仍然是旧版内容，请外部AI直接使用PR分支的固定commit母稿链接，**不要把GitHub代码搜索无结果当作文件未上传**。

项目文档中的“禁止修改”是协作约定，不代表GitHub强制访问控制；仓库公开状态、协作者、分支保护需以GitHub实时权限设置为准。

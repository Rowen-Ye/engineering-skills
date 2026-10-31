# 性能工程 Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 发布可安装、可验证的中文性能工程 skill。
**Architecture:** 独立 skill 目录，八阶段按需加载，标准库分析脚本。
**Tech Stack:** Markdown、Python 3.10+、GitHub Actions。
**Spec:** docs/superpowers/specs/2026-10-31-performance-engineering-design.md

## Global Constraints
中文文档；MIT；不可编造实测；安装不得覆盖；实验数据留在项目内。

## Review Focus
空样本、非有限数值、元数据不匹配、零基线、已有安装目录。

### Task 1: 方法与资料
- [x] 编写 SKILL.md、八阶段 workflows、理论/工具/领域参考、模板与 LLM 案例。
- [x] 检查所有内部链接和证据边界。

### Task 2: 数据与安装工具
- [x] tests/test_tools.py 先覆盖统计、比较、异常数据及覆盖保护，运行确认失败。
- [x] scripts 提供 analyze-benchmark.py、compare-results.py、visualize-performance.py；根 scripts/install.py 安装独立 skill。
- [x] 统一 JSON：context 对象、metrics 映射，每项 unit/direction/samples。
- [x] 运行 unittest 与临时目录安装验证。

### Task 3: 发布
- [x] README、MIT、贡献说明、CI；执行格式检查、单测和完整示例。
- [ ] 独立评审后修复重要问题，再创建公开仓库、推送并验证远端。

## 验证记录
2026-10-31：独立评审无阻断问题；补充 JSON 顶层校验，六项测试通过；官方 quick_validate 通过，内部链接检查无失效。安装在临时目录验证，未修改使用者已有安装。

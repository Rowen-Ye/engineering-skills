# 工程技能集 · engineering-skills

源于实际工作的 AI 工程技能集，将理论分析、工程实践与实验验证沉淀为可安装、可复用的 Agent Skills。

本仓库按独立 skill 维护方法与工具，面向希望把工程经验用于 AI 协作的开发者。文档使用中文；采用 MIT 许可证，欢迎贡献脱敏案例与改进。

## 当前技能

| 技能 | 用途 | 状态 |
|---|---|---|
| [performance-engineering](skills/performance-engineering/SKILL.md) | 以理论建模、业界研究和可复现实验定位性能瓶颈，验证优化收益 | 首版；LLM 推理提供完整演示，跨领域入口尚未逐设备实测 |

覆盖 CPU、GPU/NPU、LLM 推理、内存/NUMA、虚拟化/容器、网络/RDMA、分布式系统、存储/I/O。支持从简短分析到八阶段完整攻关，按需读取资料。

## 下载安装

需要 Git（或下载 ZIP）与 Python 3.10+。仅 skill 文档可手动安装，不需要 Python；运行数据工具才需要 Python。

```sh
git clone https://github.com/Rowen-Ye/engineering-skills.git
cd engineering-skills
python3 scripts/install.py
```

默认安装至 `${CODEX_HOME:-~/.codex}/skills/performance-engineering`，已有目录会拒绝覆盖。更新前自行备份并移走旧目录，再运行安装；脚本不会自动修改已有配置或下载依赖。

[下载源码 ZIP](https://github.com/Rowen-Ye/engineering-skills/archive/refs/heads/main.zip) 后，解压并运行同一安装命令。也可手动将 `skills/performance-engineering` 整个文件夹复制到 Codex 的 skills 目录。

自定义安装位置：
```sh
python3 scripts/install.py --dest /你的路径/skills
```

重新打开 Codex 会话，确认可以发现 `performance-engineering`，随后调用：
```text
$performance-engineering 分析当前 LLM 推理服务的 TTFT 问题。先检查工作负载和现有证据，调研适用理论与业界方案，再设计可证伪实验。没有实测数据时不要声称定位了瓶颈。
```

其他支持目录式 Agent Skills 的工具可尝试手动安装；尚未逐一验证兼容性。

## 使用与验证

- [八阶段入口](skills/performance-engineering/SKILL.md)
- [LLM 完整演示与复现命令](skills/performance-engineering/examples/llm-inference/README.md)
- [基准数据格式](skills/performance-engineering/references/benchmark-format.md)
- [报告模板](skills/performance-engineering/templates/report.md)

```sh
python3 -m unittest discover -s tests -v
```

数据脚本只做描述统计，不自动证明因果或显著性。示例全部使用明确标注的人工构造数据。真实研究需要联网工具，真实 Profiling 需要匹配的设备、工具和权限；缺失时应交付方案与未验证项。

分析产物与知识积累写入使用者项目，不写入安装目录，不自动上传。生产变更及高风险操作需要对应授权。

## 贡献与授权

参见 [贡献指南](CONTRIBUTING.md) 和 [MIT 许可证](LICENSE)。新增 skill 应有清晰触发边界、渐进式资料、可复现示例，并说明验证范围。

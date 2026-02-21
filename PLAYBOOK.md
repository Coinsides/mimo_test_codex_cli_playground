# PLAYBOOK（Codex CLI 任务执行手册）

## 1) 目的与范围
- 本仓库是长期使用的 Codex CLI playground，用于反复演练任务规范化、执行、验证与交付。
- 目标是稳定复用同一套最小闭环：`TaskSpec -> codex exec -> 测试/校验 -> 提交`。
- 本文聚焦仓库内日常执行；复杂并行场景仅给出扩展入口（线程/工作树）。

## 2) 角色分工
### Zero（Codex）可以做什么
- 读取指定 `tasks/*.task_spec.json`，按要求修改代码/文档。
- 运行项目内命令（测试、校验、静态检查）。
- 产出符合 schema 的 `TaskResult JSON`。
- 汇总变更与测试结果，供人工决策是否合并。

### Human（你）必须做什么
- 定义目标与验收标准（TaskSpec）。
- 审核 Zero 的改动是否符合真实业务意图。
- 执行最终 Git 动作：`commit` / `push` / 发起 PR。
- 在多任务并行时决定分支策略、冲突处理与合并顺序。

## 3) 标准工作流（最小闭环）
1. 编写 TaskSpec：在 `tasks/` 下创建 `*.task_spec.json`，写清输入、步骤、验收、输出路径。
2. 执行任务：用 `codex exec` 指向该 TaskSpec。
3. 运行测试：至少执行 `pytest`（或任务要求的测试命令）。
4. 校验结果：用 schema 校验 `TaskResult JSON`。
5. 提交交付：人工审阅后 `git add/commit/push`。

## 4) PowerShell 命令模板
### 4.1 创建虚拟环境并安装依赖
```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\pip install -r requirements.txt
```

### 4.2 运行测试（pytest）
```powershell
.\.venv\Scripts\pytest -q
```

### 4.3 校验 TaskResult JSON
```powershell
.\.venv\Scripts\python tools\validate_task_result.py <task_result.json> docs\contracts\task_result_v0_1.schema.json
```

## 5) codex exec 提示词模板
```text
Read tasks/<TASK_FILE>.task_spec.json, implement exactly what it asks (no extra changes), and output ONLY a TaskResult JSON that matches docs/contracts/task_result_v0_1.schema.json.
```

- 关键约束：
- 明确输入是某个 TaskSpec 文件。
- 明确“只做任务要求，不做额外改动”。
- 明确“输出仅为 TaskResult JSON（无额外文本）”。

## 6) 扩展到线程与 worktree
- `/new`：开启新会话处理新主题，避免上下文污染。
- `/fork`：基于当前上下文分叉方案，适合并行试验同一任务不同实现。
- `/resume`：恢复历史会话，继续未完成任务。
- 何时使用 `git worktree`：
- 需要并行处理多个独立任务，且每个任务要有隔离代码目录时。
- 需要长时间保留多个分支工作区，减少频繁切分支带来的干扰时。
- 轻量任务或一次性小改动，优先单工作区即可。

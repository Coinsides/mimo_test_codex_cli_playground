# Examples（示例与模板）

本目录提供两类东西：
- **模板**：复制后改字段即可用
- **示例**：用于验证工具链（schema 校验）是否正常

## 1) 你应该从哪里开始？
- 写任务：从 `tasks/TEMPLATE.task_spec.json` 复制一份，改成 `tasks/TASK-YYYYMMDD-XXX_xxx.task_spec.json`
- 输出结果：让 Codex 输出一个 TaskResult JSON（建议写到 `logs/task_results/`）

## 2) 用 codex exec 跑一个任务（PowerShell 模板）
> 说明：把 `<TASK_FILE>` 换成你实际的 TaskSpec 文件名。

```powershell
codex exec --full-auto --sandbox workspace-write `
  --output-schema .\docs\contracts\task_result_v0_1.schema.json `
  -o .\logs\task_results\<TASK_ID>.task_result.json `
  "Read tasks/<TASK_FILE>, implement exactly what it asks (no extra changes), and output ONLY a TaskResult JSON that matches the schema."
```

## 3) 校验 TaskResult（必须）
> 先安装依赖：`pip install -r requirements.txt`

```powershell
.\.venv\Scripts\python tools\validate_task_result.py docs\examples\TEMPLATE.task_result.json docs\contracts\task_result_v0_1.schema.json
```

## 4) 小提示
- **TaskSpec 写得越具体，越容易验收。**
- **TaskResult 只输出 JSON**：避免额外文本污染自动解析。

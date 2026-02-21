import json
import sys
from pathlib import Path

import jsonschema


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python tools/validate_task_result.py <task_result.json> <schema.json>")
        return 2

    result_path = Path(sys.argv[1])
    schema_path = Path(sys.argv[2])

    result = json.loads(result_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    jsonschema.validate(instance=result, schema=schema)
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

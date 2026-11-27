from __future__ import annotations

import json
from typing import Any

# The schema the application actually needs
REQUIRED_KEYS = ("order_id", "amount", "status")


def build_extraction_prompt(text: str) -> str:
    """Prompt that locks the output shape to a known JSON schema."""
    return (
        "Extract the order fields from the text.\n"
        "Reply with ONLY a JSON object - no prose, no markdown fences.\n"
        f"Required keys: {', '.join(REQUIRED_KEYS)}. "
        "Use null when a field is missing.\n\n"
        f"TEXT:\n{text}"
    )


def parse_structured(response: str) -> tuple[dict[str, Any] | None, str]:
    cleaned = response.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.removeprefix("json").strip()

    try:
        data  = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        return None, (f"Invalid JSON ({exc})"
                      f"Reply with ONLY the object keys:"
                      f"{', '.join(REQUIRED_KEYS)}")
    if not isinstance(data,dict):
        return None, "Response must be a JSON Object, not a list."

    missing = [k for k in REQUIRED_KEYS if k not in data] 
    if missing:
        return None, f"Missing keys {', '.join(missing)}"

    extra = [k for k in data if k not in REQUIRED_KEYS] 
    if extra:
            return None, f"Unexpected keys {', '.join(extra)}"

    return data, ""


if __name__ == "__main__":
    text = "Order ORD-7782 for Rs.1499 was shipped on 12 Nov."

    print(build_extraction_prompt(text))
    good = '{"order_id": "ORD-7782", "amount": 1499, "status": "shipped"}'
    data, err = parse_structured(good)
    print("parsed:", data, "| error:", err or "none")

    print("\n--- fenced response with missing keys ---")
    drifted = '```json\n{"order_id": "ORD-7782"}\n```'
    data, err = parse_structured(drifted)
    print("parsed:", data, "| error:", err)
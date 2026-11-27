# Training\Day6\D6P5.py
from __future__ import annotations

# Required sections of a production system prompt
REQUIRED_SECTIONS = ("OBJECTIVE", "RULES", "BOUNDARIES", "OUTPUT")


def build_system_prompt(objective: str, rules: list[str],
                        boundaries: list[str], output: str) -> str:
    """Compose a system prompt with the four required sections."""
    rule_block = "\n".join(f"{i}. {r}" for i, r in enumerate(rules, 1))
    boundary_block = "\n".join(f"- {b}" for b in boundaries)
    return (
        f"OBJECTIVE:\n{objective}\n\n"
        f"RULES:\n{rule_block}\n\n"
        f"BOUNDARIES:\n{boundary_block}\n\n"
        f"OUTPUT:\n{output}"
    )


def audit_system_prompt(system_prompt: str) -> list[str]:
    """Return the required sections missing from a system prompt."""
    upper = system_prompt.upper()
    return [s for s in REQUIRED_SECTIONS if f"{s}:" not in upper]


def build_messages(system_prompt: str, user_input: str) -> list[dict]:
    """Assemble the messages payload for a chat completions call."""
    if audit_system_prompt(system_prompt):
        raise ValueError(
            "System prompt incomplete: missing "
            f"{audit_system_prompt(system_prompt)}"
        )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]


if __name__ == "__main__":
    system = build_system_prompt(
        objective="Answer billing questions for a telecom provider.",
        rules=[
            "Never quote a refund amount not present in the account data.",
            "Ask for the account number before any account-specific answer.",
        ],
        boundaries=[
            "Do not discuss competitors.",
            "Do not give legal or tax advice.",
        ],
        output="Plain text, maximum 5 sentences, one next step.",
    )
    print(system)

    print("\nAudit (complete system):", audit_system_prompt(system) or "PASS")

    partial = "OBJECTIVE: help users\nRULES: be nice"
    print("Audit (partial system) :", audit_system_prompt(partial))

    messages = build_messages(system, "Why was I charged Rs.99 extra?")
    print("\nMessages payload roles:", [m["role"] for m in messages])
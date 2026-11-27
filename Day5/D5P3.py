from __future__ import annotations

def improve_prompt(vague:str, task:str, audience:str,output_format:str)->str:
    return (
        f"TASK:{task}\n"
        f"AUDIENCE: {audience}\n"
        f"INSTRUCTIONS:\n{vague.strip()}\n"
        "CONSTRAINTS:\n"
        "- Do not invent facts that are not provided.\n"
        "- Keep the answer under 150 words.\n"
        f"OUTPUT FORMAT:{output_format}"
    )

def audit_prompt(prompt:str)->list[str]:
    suggestions: list[str] = [] 
    lowered = prompt.lower()

    if len(prompt.split()) < 15:
        suggestions.append("Too short: add context and constraints.")

    if "output format" not in lowered and "reply with" not in lowered:
        suggestions.append("No output format specified")

    if not any(word in lowered for word in ("must","do not","never","only","constraint")):
        suggestions.append("No constraints - add hard limits.")
    
    if "you are" not in lowered and "role" not in lowered:
        suggestions.append("No role given - assign a persona.")

    return suggestions

if __name__ == "__main__":
    vague = "Write something about our new return policy."

    improved = improve_prompt(
        vague=vague,
        task="Announce the new 30-day return policy to customers",
        audience="existing e-commerce customers",
        output_format="one email subject line + a 3-sentence body",
    )
    print("=== IMPROVED PROMPT ===")
    print(improved)

    print("\n=== AUDIT OF ORIGINAL ===")
    issues = audit_prompt(vague)
    for issue in issues:
        print(f"  - {issue}")
    print(f"({len(issues)} issue(s) found)")

    print("\n=== AUDIT OF IMPROVED ===")
    issues = audit_prompt(improved)
    print(f"({len(issues)} issue(s) found)")
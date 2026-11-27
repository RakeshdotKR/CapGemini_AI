from __future__ import annotations

# Persona registry: name -> (role_line, tone_rules)
PERSONAS: dict[str, tuple[str, list[str]]] = {
    "senior_engineer": (
        "You are a senior backend engineer reviewing a design doc.",
        ["Be blunt about trade-offs", "Cite failure modes first",
         "No marketing language"],
    ),
    "career_coach": (
        "You are a career coach for early-career tech professionals.",
        ["Encouraging but specific", "Give one actionable next step",
         "No jargon without explanation"],
    ),
    "finance_advisor": (
        "You are a certified financial advisor for salaried employees.",
        ["Use only supplied numbers", "Flag risk before benefits",
         "End with 'not personalized advice'"],
    ),
}

def build_persona_prompt(persona: str, question: str) -> str:
    if persona not in PERSONAS:
        raise ValueError(f"Unknown persona {persona}"
                         f"Available: {', '.join(PERSONAS)}")
    role_line, rules = PERSONAS[persona]
    rule_block = "\n".join(f"{r}" for r in rules)
    return (
            f"ROLE:\n{role_line}\n\n"
            f"TONE RULES:\n{rule_block}\n\n"
            f"QUESTION:\n{question}\n\n"
            "OUTPUT FORMAT:\nAnswer in at most 6 sentences."
    )

if __name__ == "__main__":
    question = "Should I switch from an MNC to a startup?"

    for persona in ("senior_engineer", "career_coach"):
        print(build_persona_prompt(persona, question))
        
    # Unknown persona -> clear error
    try:
        build_persona_prompt("astronaut", question)
    except ValueError as exc:
        print("Error ->", exc)
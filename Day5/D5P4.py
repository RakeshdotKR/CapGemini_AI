from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class PromptDraft:
    """One of the version of a prompt under test."""
    version: float
    text: str
    score: int = 0
    notes: list[str] = field(default_factory=list)

# LLM judge
def score_draft(draft: PromptDraft) -> PromptDraft:
    text = draft.text.lower()
    checks = {
        "specific task named": any(k in text for k in ("write","summarize","classify","extract")),
        "output format stated": any(k in text for k in ("format","json","bullet","exactly","reply with")),
        "constraint present": any(k in text for k in ("do not","must","only","under","max")),
        "role assigned": any(k in text for k in ("you are","act as","role")),
    }
    draft.score = sum(checks.values())
    draft.notes = [name for name, passed in checks.items() if not passed]
    return draft

def refine(intial_ideas:list[str]) -> PromptDraft:
    best = PromptDraft(version=0,text="")
    for index, idea in enumerate(intial_ideas, start=1):
        draft = score_draft(PromptDraft(version=index, text=idea))
        print(f"{draft.version}:score={draft.score}/4"
              f" missing={draft.notes or 'none'}")
        if draft.score > best.score:
            best = draft
    return best

if __name__ == "__main__":
    drafts = [
        #v1: vague - no format, no constaints, no role
        "Tell the customer about delayed orders.",
        #v2: add format, add constaints, no role
        "Explain delayed orders. Reply in exactly 2 sentences."
        "Do not promise a delivery date",
        #v3: add format, add constaints, add role
        "You are a logistics support agent. Explain why an order is delayed"
        "in exactly 2 sentences. Do not promise a delivery date. Reply in plain text only.",
    ]

    print("Scoring drafts:")
    winner = refine(drafts)

    print(f"\nWinner: v{winner.version} with score {winner.score}/4")
    print(winner.text)
from __future__ import annotations
LABELS = ["billing", "bug","how_to","other"]

def zero_shot_prompt(ticket:str)->str:
    return (
        "Classify the support ticket into exactly one label:"
        f"{', '.join(LABELS)}.\n"
        "Reply with ONLY the label, nothing else.\n"
        f"Ticket:{ticket}"
    )

def few_shot_prompt(ticket:str,examples:list[tuple[str,str]])->str:
    header = (
        "Classify the support ticket into exactly one label:"
        f"{', '.join(LABELS)}.\n"
        "Reply with ONLY the label, nothing else.\n"
    )
    rendered = [f"Ticket: {text}\nLabel: {label}" for text, label in examples]
    body = "\n\n".join(rendered+[f"Ticket: {ticket}\nLabel:"])
    return f"{header}\n{body}"

if __name__ == "__main__":
    train_examples = [
        {"I was charged twice for the same order.","billing"},
        {"The app crashes when I open settings.","bug"},
        {"How do I reset Password?","how_to"},
    ]

    new_ticket = "Where can I download my monthly invoice?"

    print(zero_shot_prompt(new_ticket))
    print(few_shot_prompt(new_ticket,train_examples))
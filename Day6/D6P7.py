# Training\Day6\D6P7.py
from __future__ import annotations

import re
from dataclasses import dataclass, field

@dataclass
class PromptTemplate:
    """A reusable prompt with named placeholders.

    Placeholders use {name} syntax. Rendering fails loudly when a
    required placeholder has no value - silent blank sections in
    prompts are a top cause of bad model output.
    """

    name: str
    template: str
    version: str = "1.0"
    required: tuple[str, ...] = field(default_factory=tuple)

    def placeholders(self) -> list[str]:
        """Return every {placeholder} name found in the template."""
        return sorted(set(re.findall(r"\{(\w+)\}", self.template)))

    def render(self, **kwargs: object) -> str:
        """Fill placeholders; raise listing every missing required key."""
        missing = [k for k in self.required if k not in kwargs]
        if missing:
            raise ValueError(
                f"Template '{self.name}' v{self.version} missing: "
                f"{', '.join(missing)}"
            )
        try:
            return self.template.format(**kwargs)
        except KeyError as exc:
            raise ValueError(f"Missing value for {exc}") from exc


# The library: name -> template (single source of truth)
LIBRARY: dict[str, PromptTemplate] = {
    "ticket_triage": PromptTemplate(
        name="ticket_triage",
        template=(
            "Classify this ticket into: {labels}.\n"
            "Reply with ONLY the label.\n\n"
            "Ticket: {ticket}"
        ),
        version="2.1",
        required=("labels", "ticket"),
    ),
    "exec_summary": PromptTemplate(
        name="exec_summary",
        template=(
            "You are a strategy analyst. Summarize for a {audience} "
            "in {max_sentences} sentences, no jargon.\n\n{text}"
        ),
        version="1.3",
        required=("audience", "max_sentences", "text"),
    ),
}


def list_templates() -> list[tuple[str, str]]:
    """Return (name, version) for every template in the library."""
    return [(t.name, t.version) for t in sorted(LIBRARY.values(),
                                                key=lambda t: t.name)]


if __name__ == "__main__":
    print("Library:", list_templates())

    triage = LIBRARY["ticket_triage"]
    print("\nPlaceholders:", triage.placeholders())
    print(triage.render(labels="billing, bug, how_to",
                        ticket="Double charged!"))

    try:
        triage.render(ticket="no labels given")
    except ValueError as exc:
        print("\nError ->", exc)
# Training\Day6\D6P6.py
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Step:
    """One stage of a decomposed task."""

    name: str
    prompt: str
    depends_on: str | None = None   # name of the previous step

def decompose_goal(goal: str, source_text: str) -> list[Step]:
    """Split a listing-creation goal into ordered single-task prompts.

    Each step does exactly ONE job - the core rule of decomposition.
    """
    return [
        Step(
            name="extract_facts",
            prompt=(f"Extract bullet facts (features, price, material) from "
                    f"the text. No commentary.\n\nTEXT:\n{source_text}"),
        ),
        Step(
            name="write_title",
            prompt=("Write one product title under 60 characters using only "
                    "the facts above. Output the title only."),
            depends_on="extract_facts",
        ),
        Step(
            name="write_description",
            prompt=("Write a 3-sentence description using only the facts "
                    "and title above. No new claims."),
            depends_on="write_title",
        ),
        Step(
            name="qc_check",
            prompt=("List any claim in the description that is NOT supported "
                    "by the facts. Output 'PASS' when none."),
            depends_on="write_description",
        ),
    ]


def run_chain(steps: list[Step], stage_outputs: dict[str, str]) -> dict[str, str]:
    """Execute the chain: each step's prompt includes prior outputs.

    Args:
        steps: Ordered steps from decompose_goal().
        stage_outputs: Canned model output per step name (demo stand-in).

    Returns:
        Mapping of step name -> final output.
    """
    results: dict[str, str] = {}
    for step in steps:
        if step.depends_on and step.depends_on not in results:
            raise ValueError(
                f"Step '{step.name}' needs '{step.depends_on}' first."
            )
        # Feed upstream output into the prompt (context threading)
        prompt = step.prompt
        if step.depends_on:
            prompt = f"PRIOR STEP ({step.depends_on}):\n" \
                     f"{results[step.depends_on]}\n\n{prompt}"
        results[step.name] = stage_outputs[step.name]
        print(f"[{step.name}] prompt chars: {len(prompt)}")
    return results


if __name__ == "__main__":
    source = ("Eco-friendly bamboo toothbrush, pack of 4, soft bristles, "
              "plastic-free packaging, Rs.299")

    steps = decompose_goal("Create a Flipkart-style listing", source)

    # Canned outputs a real model would produce per stage
    canned = {
        "extract_facts": "- bamboo toothbrush\n- pack of 4\n- soft bristles\n"
                         "- plastic-free packaging\n- Rs.299",
        "write_title": "Bamboo Toothbrush Pack of 4 - Soft Bristles",
        "write_description": "Switch to a plastic-free routine with this "
                             "4-pack of soft-bristle bamboo toothbrushes. "
                             "Packaging is fully plastic-free. Priced at "
                             "Rs.299 for the set.",
        "qc_check": "PASS",
    }

    results = run_chain(steps, canned)
    print("\nFinal QC:", results["qc_check"])
    print("Title    :", results["write_title"])
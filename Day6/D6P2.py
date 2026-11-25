from __future__ import annotations

import re

def build_cot_prompt(question: str, facts: list[str]) -> str:
    fact_block = "\n".join(f"{f} for f in facts")
    return(
        "Answer the question step by step. \n"
        "Format:\n"
        "Step 1: ...\n"
        "Step 2: ...\n"
        "Final answer: <short answer>\n\n"
        "FACTS:\n{fact_block}\n\n"
        f"QUESTION: {question}"
    )

def parse_final_answer(response:str)->str:
    match = re.search(r"Final answer:\s*(.+)", response,re.IGNORECASE)
    if not match:
        raise ValueError("No. Final Answer found. CoT format drift.")
    return match.group(1).strip()

# A canned CoT response (what a real model would return)
SAMPLE_RESPONSE = (
    "Step 1: Wallet balance is Rs.5000 as stated in the facts.\n"
    "Step 2: The pending payment is Rs.1200.\n"
    "Step 3: 5000 - 1200 = 3800.\n"
    "Final answer: Rs.3800 will remain after the payment settles."
)


if __name__ == "__main__":
    facts = [
        "Wallet balance: Rs.5000",
        "Pending payment: Rs.1200",
    ]
    question = "How much balance remains after the pending payment settles?"

    print(build_cot_prompt(question, facts))
    print("\n--- model response ---")
    print(SAMPLE_RESPONSE)
    print("Parsed:", parse_final_answer(SAMPLE_RESPONSE))

    # Format-drift protection
    try:
        parse_final_answer("The answer is about 3800 rupees.")
    except ValueError as exc:
        print("Drift caught ->", exc)
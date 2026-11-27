from __future__ import annotations

def build_prompt(
        role:str,
        context:str,
        instructions:str,
        input_data:str,
        output_format:str,
)-> str: #prompt string with the clearly labelled sections
    parts = {
        "ROLE":role,
        "CONTEXT":context,
        "INSTRUCTIONS":instructions,
        "INPUT":input_data,
        "OUTPUT FORMAT":output_format,
    }
    missing = [name for name, value in parts.items() if not value.strip()]
    if missing:
        raise ValueError(f"Prompt section empty for: {', '.join(missing)}")

    return "\n\n".join(f"{name}:\n{value}" for name, value in parts.items())

if __name__ == "__main__":
    prompt = build_prompt(
        role="Customer support agent for a mobile banking app",
        context="The customer reports a failed UPI transfer that still debited their account.",
        instructions=(
            "1. Acknowledge the issue empathetically.\n"
            "2. Ask for the UPI refernce number.\n"
            "3. Explain what happens next in two sentences."
        ),
        input_data=(
            "Hi, I sent Rs. 5000 to pay the bill and the app says failed."
            "Before the transaction I had Rs. 50000 in my account now I've Rs.45000"
        ),
        output_format="Exactly four short sentences, numbered 1-4.",
    )
    # print(prompt)
try:
    build_prompt(
            role="Customer support agent for a mobile banking app",
            context="",
            instructions=(
                "1. Acknowledge the issue empathetically.\n"
                "2. Ask for the UPI refernce number.\n"
                "3. Explain what happens next in two sentences."
            ),
            input_data=(
                "Hi, I sent Rs. 5000 to pay the bill and the app says failed."
                "Before the transaction I had Rs. 50000 in my account now I've Rs.45000"
            ),
            output_format="",
        ) 
except ValueError as exc:
    print("\nValidation: ",exc)

    
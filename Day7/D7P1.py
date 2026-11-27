"""Multi-turn conversation design and memory

A ConversationManager that tracks turns, extracts remembered facts,
and builds the messages payload within a turn limit.
"""
from __future__ import annotations
import re

from dataclasses import dataclass, field

@dataclass
class Conversation:
    """ Turn store with fact memory & payload building"""
    system_prompt: str
    max_turns: int = 6
    # A dataclasses.field() parameter that takes a zero-argument function (like list or dict) 
    # to generate a fresh default value for each new instance.
    turns: list[dict] = field(default_factory=list)
    memory: dict[str,str] = field(default_factory=dict)

    def add(self,role:str, content:str) -> None:
        self.turns.append({"role":role,"content":content})
        if role == "user":
            self._remember(content)

    def _remember(self,text:str)->None:
        match = re.search(r"\bmy ([\w ]+?) is ([\w ]+?)[.!]?\s*$", text,
                          re.IGNORECASE)

        if match:
            key = match.group(1).strip().lower()
            value = match.group(2).strip()
            self.memory[key] = value

    def _trim(self)->list[dict]:
        """keep only the most recent max_turns (oldest becomes summary)."""
        if len(self.turns) <= self.max_turns:
            return self.turns
        dropped = len(self.turns) - self.max_turns
        summary = {"role":"system",
                   "content":f"[{dropped} earlier turns summarized]"}
        return [summary]+self.turns[-self.max_turns:]

    # Must be inside class Conversation
    def build_messages(self) -> list[dict]:
        """Assemble system + memory + trimmed history payload."""
        memory_block = ""
        if self.memory:
            facts = "\n".join(f"- {k}: {v}" for k, v in self.memory.items())
            memory_block = f"\n\nREMEMBERED FACTS:\n{facts}"
        return [
            {"role": "system",
             "content": self.system_prompt + memory_block},
            *self._trim(),
        ]


if __name__ == "__main__":
    chat = Conversation(system_prompt="You are a banking assistant.",
                        max_turns=3)

    chat.add("user", "Hi, my name is Priya.")
    chat.add("assistant", "Hello Priya, how can I help?")
    chat.add("user", "My account number is 445566.")
    chat.add("assistant", "Noted. What do you need today?")
    chat.add("user", "Check my balance please.")

    print("Memory:", chat.memory)
    print("\nMessages payload:")
    for message in chat.build_messages():
        head = message["content"].splitlines()[0]
        print(f"  [{message['role']}] {head[:70]}")
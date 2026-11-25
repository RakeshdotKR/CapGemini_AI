# Task specific prompt builder
from __future__ import annotations

BUILDERS: dict[str,object] = {}

def register(task: str):
    def decorator(func):
        BUILDERS[task] = func
        return func
    return decorator

@register("summarize")
def summarize_prompt(text:str, max_sentences:int = 3)->str:
    return(
        f"Summarize the text below in at most {max_sentences} sentences."
        "Keep every proper noun. Do not add opinions.\n\n"
        f"TEXT:\n{text}"
    )

@register("extract")
def extract_prompt(text:str,fields:list[str])->str:
    schema = ", ".join(f'"{f}"' for f in fields)
    return(
        "Extract the listed fields from the text."
        f"Reply with ONLY a JSON object with keys: {schema}."
        "Use null when a field is missing.\n\n"
        f"TEXT:\n{text}"
    )

@register("classify")
def classify_prompt(text:str,labels:list[str])->str:
    return(
        f"Classify the text into exactly one of: {','.join(labels)}.\n"
        "Reply with ONLY the label.\n\n"
        f"TEXT:\n{text}"
    )

@register("generate")
def generate_prompt(topic:str,audience:str,style:str)->str:
    return(
        f"Write a {style} piece about: {topic}\n"
        f"Audience: {audience}\n"
        "Rules: under 120 words, don't use emojis, and end with one call to action."
    )

@register("reason")
def reason_prompt(question:str,facts:list[str])->str:
    fact_block = "\n".join(f"{f} for f in facts")
    return(
        "Answer the question using ONLY the facts below."
        "Think step by step, then give a one-line final answer. \n\n"
        f"Facts: \n{fact_block}\n\nQuestion:{question}"
    )

def build(task:str,**kwargs)->str:
    if task not in BUILDERS:
        raise ValueError(f"Unknown task :'{task}'.")
    return BUILDERS[task](**kwargs)

if __name__ == "__main__":
    print(build("summarize",
          text="Python is popular in AI. It has huge ecosystem."
                "Companies ship GenAI products with it daily."
          ,max_sentences=2))

# Calling other functions


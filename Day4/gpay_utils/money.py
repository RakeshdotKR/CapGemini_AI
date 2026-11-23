from __future__ import annotations 
def format_inr(paisa:int)->str:
    if paisa < 0:
        raise ValueError("Amount cannot be negative")
    return f"INR {paisa/100:,.2f}"

def parse_inr(text:str)->int:
    """ INR 1234: Integer 1234"""
    cleaned = text.replace("INR", "").replace(",","").strip()

    return round(float(cleaned)*100)
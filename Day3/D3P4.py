# Higher order function
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def process_text(func,text): 
    return func(text)

print(process_text(shout,"hello"))
print(process_text(whisper,"HI"))
funcs = [shout,whisper]
print([f("Hi") for f in funcs])


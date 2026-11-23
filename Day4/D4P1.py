# File I/O : is a process of reading bytes from a file on disk into our program and writing
# bytes from our program back to the disk.

# Context Manager: set up resources before the code runs and automatically rears it down 
# afterwards - file handle closes and buffer data is flushed.

# Syntax: 
# Read:
# with open("/path/example.txt",mode="r",encoding="utf-8") as file_obj:
#     content = file_obj.read()
    
# # Write:
# with open("/path/example.txt",mode="w",encoding="utf-8") as file_obj:
#     file_obj.write("Text")
# **************************************************************************

from pathlib import Path
MY_FILE = Path("day4_1.txt")

def save_note(text:str)->None:
    with MY_FILE.open(mode="w",encoding="utf-8") as handle:
        handle.write(text.rstrip()+"\n")

def read_note()->list[str]:
    if not MY_FILE.exists():
        return [] #guard clause
    with MY_FILE.open("r",encoding="utf-8") as handle:
        return [line.strip() for line in handle if line.strip()]

if __name__ == "__main__": #import as a module 
    save_note("Hello from Capgemini")
    save_note("My name is Rakesh")
    for index,note in enumerate(read_note(),start=1):
        print(f"{index}. {note}")

                 
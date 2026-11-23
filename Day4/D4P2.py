# JSON: json module converts betweeen python objects (dict, list, str, int, float, bool, None) 
# and their JSON string represenatation.

# import json
# # Write
# json_str = json.dumps(python_obj,indent=2,ensure_ascii=False)
# # Read
# python_obj = json.loads(json_str)

# # Read
# with open("data.json","r",encoding="utf-8") as f:
#     obj = json.load(f)

# #write
# with open("data.json","w",encoding="utf-8") as f:
#     json.dump(obj,f,indent=2,ensure_ascii=False)


import json
from pathlib import Path

CONFIG_PATH = Path("app_config.json")

def build_config()->dict:
    return{
        "app_name":"CapgeminiAI",
        "model":"gpt-4o-mini",
        "temperature":0.7,
        "features":{"rag_enabled":True,"Streaming":True},
    }

def save_config(config:dict,path:Path = CONFIG_PATH)-> None:
    with path.open("w",encoding="utf-8") as handle:
        json.dump(config,handle,indent=2,ensure_ascii=False)

def load_config(path: Path = CONFIG_PATH)->dict:
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")

    with path.open("r",encoding="utf-8") as handle:
        return json.load(handle)

if __name__ == "__main__":
    save_config(build_config())
    cfg = load_config()
    print(f"Model: {cfg['model']}")
    print(f"Temperature: {cfg['temperature']}")
    print(f"RAG on?: {cfg['features']['rag_enabled']}")
    print(json.dumps(
        {"messages":[{"role":"user","content":"Hello"}],
         "model": cfg["model"]},
         indent=2,
    ))
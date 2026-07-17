import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(filename):
    file_path = os.path.join(BASE_DIR, "knowledge", filename)

  

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_knowledge():
    return load_json("knowledge_base.json")
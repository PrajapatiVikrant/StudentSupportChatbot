import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(filename):
    file_path = os.path.join(BASE_DIR, "knowledge", filename)

    print("BASE_DIR :", BASE_DIR)
    print("FILE_PATH:", file_path)
    print("Exists   :", os.path.exists(file_path))

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_knowledge():
    return load_json("knowledge_base.json")
import json, os

ARQ = "discos.json"

def load():
    if not os.path.exists(ARQ):
        with open(ARQ, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
    with open(ARQ, "r", encoding="utf-8") as f:
        return json.load(f)

def save(dados):
    with open(ARQ, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
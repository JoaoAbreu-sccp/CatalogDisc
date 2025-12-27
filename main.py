import json, os

ARQ = "discos.json"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Load():
    if not os.path.exists(ARQ):
        with open(ARQ, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    with open(ARQ, "r", encoding="utf-8") as f:
        return json.load(f)

def Save(dados):
    with open(ARQ, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def DiscRegister():
    dados = Load()

    nome = str(input("Nome do disco: "))
    autor = str(input("Artista/Banda: "))
    ano = int(input("Ano de lançamento: "))
    print("DIgite abaixo a sua critica:")
    critica = str(input("-> "))

    disco = {
        'nome': nome,
        'autor': autor,
        'ano': ano,
        'critica': critica
    }
    dados.append(disco)
    Save(dados)
    print("Disco catalogado com sucesso.")


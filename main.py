import json, os

ARQ = "discos.json"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Load():
    if not os.path.exists(ARQ):
        with open(ARQ, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=5)

    with open(ARQ, "r", encoding="utf-8") as f:
        return json.load(f)

def Save(dados):
    with open(ARQ, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=5)

def DiscRegister():
    dados = Load()

    nome = str(input("Nome do disco: "))
    autor = str(input("Artista/Banda: "))
    ano = int(input("Ano de lançamento: "))
    nota = int(input("Quantas estrelas deseja dar[0 a 5]: "))
    if nota < 0 or nota > 5:
        print("nota inválida!")
        return
    nota = "★" * nota + "☆" * (5 - nota)

    print("DIgite abaixo a sua critica:")
    critica = str(input("-> "))

    disco = {
        'nome': nome,
        'autor': autor,
        'ano': ano,
        'nota': nota,
        'critica': critica
    }
    dados.append(disco)
    Save(dados)
    print("Disco catalogado com sucesso.")

def List():
    dados = Load()
    if not dados:
        print("Nenhum disco cadastrado")
        return
    

    for index, disco in enumerate(dados):
        print(f"\n{index} - ")
        print(f"Nome: {disco['nome']}")
        print(f"Autor: {disco['autor']}")
        print(f"Ano de Lançamento: {disco['ano']}")
        print(f"Nota: {disco['nota']}")
        print(f"Crítica: {disco['critica']}")

def Edit():
    dados = Load()
    List()

    index = int(input("Digite o indice do disco que deseja editar: "))

    if index < 0 or index >= len(dados):
        print("indice inválido")
        return
    
    disco = dados[index]

    disco['nome'] = input("Nome: ")
    disco['autor'] = input("Autor: ")
    disco['ano'] = int(input("Ano de lançamento: "))
    nota = int(input("Quantas estrelas deseja dar[0 a 5]: "))
    if nota < 0 or nota > 5:
        print("nota inválida!")
        return
    disco['nota'] = "★" * nota + "☆" * (5 - nota)
    disco['critica'] = input("Crítica: ")

    Save(dados)

def Delete():
    dados = Load()
    List()

    index = int(input("Digite o indice do disco que deseja editar: "))

    if index < 0 or index >= len(dados):
        print("indice inválido")
        return
    
    dados.pop(index)
    Save(dados)
    print("Disco Excluído com sucesso.")

while True:
    clear()
    print('''
=== CatalogDisc ===
[1] Listar discos
[2] Adicionar disco
[3] Editar disco
[4] Excluir disco
[0] Sair''')
    opc = int(input("opc= "))
    if opc == 1:
        clear()
        List()
        sair = int(input("[0] para voltar: "))
        if sair == 0:
            continue
    elif opc == 2:
        clear()
        DiscRegister()
    elif opc == 3:
        clear()
        Edit()
    elif opc == 4:
        clear()
        Delete()
    elif opc == 0:
        break
    else:
        print("Opção inválida!...")
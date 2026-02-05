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

def NextID(dados):
    if not dados:
        return 0
    return max(disco['id'] for disco in dados) + 1


def DiscRegister():
    dados = Load()

    nome = input("Nome do disco: ")
    autor = input("Artista/Banda: ")
    ano = int(input("Ano de lançamento: "))
    nota = int(input("Quantas estrelas deseja dar[0 a 5]: "))

    if nota < 0 or nota > 5:
        print("nota inválida!")
        return

    nota = "★" * nota + "☆" * (5 - nota)

    print("Digite abaixo a sua critica:")
    critica = input("-> ")

    disco = {
        'id': NextID(dados),
        'nome': nome,
        'autor': autor,
        'ano': ano,
        'nota': nota,
        'critica': critica
    }

    dados.append(disco)
    Save(dados)
    print(f"Disco catalogado com sucesso. ID: {disco['id']}")


def List():
    dados = Load()
    if not dados:
        print("Nenhum disco cadastrado")
        return

    for disco in dados:
        print(f"\nID: {disco['id']}")
        print(f"Nome: {disco['nome']}")
        print(f"Autor: {disco['autor']}")
        print(f"Ano de Lançamento: {disco['ano']}")
        print(f"Nota: {disco['nota']}")
        print(f"Crítica: {disco['critica']}")

def FindID(dados, id_busca):
    for index, disco in enumerate(dados):
        if disco['id'] == id_busca:
            return index, disco
    return None, None


def Edit():
    dados = Load()
    List()

    try:
        id_busca = int(input("\nDigite o ID do disco que deseja editar[Enter para voltar]: "))
    except (ValueError):
        return
    index, disco = FindID(dados, id_busca)

    if disco is None:
        print("ID não encontrado")
        return

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
    print("Disco editado com sucesso.")


def Delete():
    dados = Load()
    List()

    try:
        id_busca = int(input("Digite o ID do disco: "))
    except ValueError:
        return
    index, disco = FindID(dados, id_busca)

    if disco is None:
        print("ID não encontrado")
        return

    dados.pop(index)
    Save(dados)
    print("Disco excluído com sucesso.")

def SearchID():
    dados = Load()

    try:
        id_busca = int(input("Digite o ID do disco: "))
    except ValueError:
        return
    _, disco = FindID(dados, id_busca)

    if disco is None:
        print("Disco não encontrado")
        return

    print("\n=== Disco encontrado ===")
    print(f"ID: {disco['id']}")
    print(f"Nome: {disco['nome']}")
    print(f"Autor: {disco['autor']}")
    print(f"Ano: {disco['ano']}")
    print(f"Nota: {disco['nota']}")
    print(f"Crítica: {disco['critica']}")



while True:
    clear()
    print('''
=== CatalogDisc ===
[1] Listar discos
[2] Buscar por ID
[3] Adicionar disco
[4] Editar disco
[5] Excluir disco
[0] Sair''')
    opc = int(input("opc= "))
    if opc == 1:
        clear()
        List()
        input("\nEnter para voltar...")
    elif opc == 2:
        clear()
        SearchID()
        input("\nEnter para voltar...")
    elif opc == 3:
        clear()
        DiscRegister()
    elif opc == 4:
        clear()
        Edit()
    elif opc == 5:
        clear()
        Delete()
    elif opc == 0:
        break
    else:
        print("Opção inválida!...")
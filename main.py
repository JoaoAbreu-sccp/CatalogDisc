import json, os
from time import sleep

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
    while True:
        nome = input("Nome do disco: ").strip()
        if nome:
            break
        print("Nome é obrigatório.")

    while True:
        autor = input("Artista/Banda: ").strip()
        if autor:
            break
        print("Artista/Banda é obrigatório")
        
    while True:
        try:
            ano = int(input("Ano de lançamento: "))
            if ano < 1800 or ano > 2100:
                print("Ano inválido.")
                continue
            break
        except ValueError:
            print("Digite um ano válido.")

    while True:
        try:
            nota = int(input("Nota [0 a 5]: "))
            if 0 <= nota <= 5:
                break
            print("Nota deve estar entre 0 e 5.")
        except ValueError:
            print("Digite um número.")

    nota = "★" * nota + "☆" * (5 - nota)

    print("Digite abaixo a sua critica:")
    while True:
        critica = input("-> ").strip()
        if critica:
            break
        print("Crítica é obrigatória.")


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
        id_busca = int(input("\nDigite o ID do disco que deseja editar [Enter para voltar]: "))
    except ValueError:
        return

    index, disco = FindID(dados, id_busca)

    if disco is None:
        print("ID não encontrado")
        return

    while True:
        nome = input("Nome: ").strip()
        if nome:
            disco['nome'] = nome
            break
        print("Nome é obrigatório.")

    while True:
        autor = input("Autor: ").strip()
        if autor:
            disco['autor'] = autor
            break
        print("Autor é obrigatório.")

    while True:
        try:
            ano = int(input("Ano de lançamento: "))
            if 1800 <= ano <= 2100:
                disco['ano'] = ano
                break
            print("Ano inválido.")
        except ValueError:
            print("Digite um ano válido.")

    while True:
        try:
            nota = int(input("Quantas estrelas [0 a 5]: "))
            if 0 <= nota <= 5:
                disco['nota'] = "★" * nota + "☆" * (5 - nota)
                break
            print("Nota deve estar entre 0 e 5.")
        except ValueError:
            print("Digite um número.")

    while True:
        critica = input("Crítica: ").strip()
        if critica:
            disco['critica'] = critica
            break
        print("Crítica é obrigatória.")

    Save(dados)
    print("Disco editado com sucesso.")



def Delete():
    dados = Load()
    List()

    try:
        id_busca = int(input("Digite o ID do disco[Enter para voltar]: "))
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
    try:
        opc = int(input("opc= "))
    except ValueError:
        continue
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
        sleep(1)
    elif opc == 5:
        clear()
        Delete()
        sleep(1)
    elif opc == 0:
        break
    else:
        print("Opção inválida!...")
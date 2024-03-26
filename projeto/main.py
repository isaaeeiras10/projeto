from database import atualizar_equipamento, atualizar_sala, deletar_equipamento, deletar_sala
from dados import equipamentos, salas

def main():
    
    while True:
        print('''
        [ 1 ] Criar equipamentos e salas 
        [ 2 ] Ler equipamentos e salas 
        [ 3 ] Atualizar equipamentos e salas
        [ 4 ] Excluir equipamentos e salas
        [ 5 ] Sair 
    ''')
        op = int(input(': '))
        if op == '1':
            print()
def voltarMenu():
    vtMenu = input("\nPressione ENTER para voltar... ")
    if len(vtMenu) >= 0:
        menu()

def menu():
    indiceMenu = int(input("""
-----------------------
O que deseja gerenciar?
[1] Equipamentos
[2] Salas
[3] Sair    
-----------------------
"""))
    if indiceMenu == 1:
        menuEquipamentos()
    elif indiceMenu == 2:
        menuSalas()
    elif indiceMenu == 3:
        print("\nSaindo...")
    else:
        print("Valor inserido inválido.")
        menu()

def menuEquipamentos():
    indiceMenuEquipamentos = int(input("""
---------Equipamentos---------
[1] Visualizar
[2] Cadastrar
[3] Atualizar
[4] Deletar
[5] Voltar
-------------------------------
"""))
    if indiceMenuEquipamentos == 1:
        listarEquipamentos()
    elif indiceMenuEquipamentos == 2:
        cadastrarEquipamento()
    elif indiceMenuEquipamentos == 3:
        atualizarEquipamento()
    elif indiceMenuEquipamentos == 4:
        deletarEquipamento()
    elif indiceMenuEquipamentos == 5:
        menu()
    else:
        print("Valor inserido inválido.")
        menuEquipamentos()

def menuSalas():
    indiceMenuSalas = int(input("""
---------Salas---------
[1] Visualizar
[2] Cadastrar
[3] Atualizar
[4] Deletar
[5] Voltar
------------------------
"""))
    if indiceMenuSalas == 1:
        listarSalas()
    elif indiceMenuSalas == 2:
        cadastrarSala()
    elif indiceMenuSalas == 3:
        atualizarSala()
    elif indiceMenuSalas == 4:
        deletarSala()
    elif indiceMenuSalas == 5:
        menu()
    else:
        print("Valor inserido inválido.")
        menuSalas()

def listarEquipamentos():
    for equipamento in equipamentos:
        print(f'Tombamento: {equipamento["tombamento"]} - Descrição: {equipamento["descricao"]}')
    voltarMenu()

def cadastrarEquipamento():
    tombamento = input("Digite o número de tombamento do equipamento: ")
    descricao = input("Digite a descrição do equipamento: ")
    # Adicione a lógica para cadastrar o equipamento no banco de dados
    voltarMenu()

def atualizarEquipamento():
    tombamento = input("Digite o número de tombamento do equipamento que deseja atualizar: ")
    # Adicione a lógica para atualizar o equipamento no banco de dados
    voltarMenu()

def deletarEquipamento():
    tombamento = input("Digite o número de tombamento do equipamento que deseja deletar: ")
    # Adicione a lógica para deletar o equipamento do banco de dados
    voltarMenu()

def listarSalas():
    for sala in salas:
        print(f'Número: {sala["numero"]} - Descrição: {sala["descricao"]}')
    voltarMenu()

def cadastrarSala():
    numero = input("Digite o número da sala: ")
    descricao = input("Digite a descrição da sala: ")
    # Adicione a lógica para cadastrar a sala no banco de dados
    voltarMenu()

def atualizarSala():
    numero = input("Digite o número da sala que deseja atualizar: ")
    # Adicione a lógica para atualizar a sala no banco de dados
    voltarMenu()

def deletarSala():
    numero = input("Digite o número da sala que deseja deletar: ")
    # Adicione a lógica para deletar a sala do banco de dados
    voltarMenu()

menu()

         



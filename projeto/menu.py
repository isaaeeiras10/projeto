from database import *

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
[4] Voltar
-------------------------------
"""))
    if indiceMenuEquipamentos == 1:
        for equipamento in equipamentos:
            print(f'Tombamento: {equipamento["tombamento"]} - Descrição: {equipamento["descricao"]}')
        voltarMenu()
    # elif indiceMenuEquipamentos == 2:
    # elif indiceMenuEquipamentos == 3:
    elif indiceMenuEquipamentos == 4:
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
[4] Voltar
------------------------
"""))
    if indiceMenuSalas == 1:
        for sala in salas:
            print(f'Número: {sala["numero"]} - Descrição: {sala["descricao"]}')
        voltarMenu()
    # elif indiceMenuSalas == 2:
    # elif indiceMenuSalas == 3:
    elif indiceMenuSalas == 4:
        menu()
    else:
        print("Valor inserido inválido.")
        menuSalas()

menu()


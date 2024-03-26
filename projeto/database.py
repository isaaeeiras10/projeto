class Equipamento:
    def __init__(self, tombamento, descricao):
        self.tombamento = tombamento
        self.descricao = descricao

class Sala:
    def __init__(self, numero, descricao):
        self.numero = numero
        self.descricao = descricao

# Listas globais para armazenar equipamentos e salas
equipamentos = []
salas = []

def criar_equipamento(tombamento, descricao):
    equipamento = Equipamento(tombamento, descricao)
    equipamentos.append(equipamento)
    return equipamento

def ler_equipamento(tombamento):
    for equipamento in equipamentos:
        if equipamento.tombamento == tombamento:
            return equipamento
    return None

def atualizar_equipamento(tombamento, nova_descricao):
    equipamento = ler_equipamento(tombamento)
    if equipamento:
        equipamento.descricao = nova_descricao
        return True
    return False

def deletar_equipamento(tombamento):
    equipamento = ler_equipamento(tombamento)
    if equipamento:
        equipamentos.remove(equipamento)
        return True
    return False

def criar_sala(numero, descricao):
    sala = Sala(numero, descricao)
    salas.append(sala)
    return sala

def ler_sala(numero):
    for sala in salas:
        if sala.numero == numero:
            return sala
    return None

def atualizar_sala(numero, nova_descricao):
    sala = ler_sala(numero)
    if sala:
        sala.descricao = nova_descricao
        return True
    return False

def deletar_sala(numero):
    sala = ler_sala(numero)
    if sala:
        salas.remove(sala)
        return True
    return False

# Exemplo de uso:
equipamento1 = criar_equipamento("EQP001", "Computador")
equipamento2 = criar_equipamento("EQP002", "Notebook")

print("Equipamentos:")
for equipamento in equipamentos:
    print(f"Tombamento: {equipamento.tombamento}, Descrição: {equipamento.descricao}")

sala1 = criar_sala("Sala A", "Sala de Reuniões")
sala2 = criar_sala("Sala B", "Sala de Treinamento")

print("\nSalas:")
for sala in salas:
    print(f"Número: {sala.numero}, Descrição: {sala.descricao}")

atualizar_equipamento("EQP001", "Laptop")

print("\nEquipamentos após atualização:")
for equipamento in equipamentos:
    print(f"Tombamento: {equipamento.tombamento}, Descrição: {equipamento.descricao}")

deletar_sala("Sala B")

print("\nSalas após deleção:")
for sala in salas:
    print(f"Número: {sala.numero}, Descrição: {sala.descricao}")

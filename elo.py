import time

# Lista de idosos cadastrados por CEP
lista_idosos = [
    {"nome": "Dona Maria", "rua": "Rua das Flores, 42", "cep": "04551-000"},
    {"nome": "Seu João", "rua": "Av. Principal, 105", "cep": "04551-000"},
    {"nome": "Dona Francisca", "rua": "Rua da Ponte, 12", "cep": "01310-000"}
]

# Lista de vizinhos voluntários cadastrados por CEP (Os "Guardiões")
lista_vizinhos  = [
    {"nome": "Carlos (Guardião)", "rua": "Jardim Salete 451", "cep": "06787-390"},
    {"nome": "Rafael Antonucci (Guardião)", "rua": "Rua Teodro Sampaio 417", "cep": "05405-000"},
    {"nome": "Paulo Sobreira (Guardião)", "rua": "Rua Francisco Comino 249", "cep": "02303-322"}
]

# Função para monitoramento
def simular_sensor(distancia_agua):
    """
    Calcula o nível de água baseado na distância lida pelo sensor ultrassônico. 
    Quanto menor a distância do sensor até a água, mais alto está o nível 
    """
    if distancia_agua <= 30:
        return "CRÍTICO"
    elif distancia_agua <= 70:
        return "ATENÇÃO"
    else:
        return "NORMAL"

 

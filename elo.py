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

 #Loop principal do sistema

while True:
    print("\n" + "="*45)
    print("      SISTEMA ELO      ")
    print("="*45)
    print("1 - Iniciar Monitoramento Automatizado (Sensor)")
    print("2 - Ver Idosos Vulneráveis Cadastrados")
    print("3 - Ver Vizinhos Voluntários por CEP")
    print("4 - Sair do Sistema")
    print("="*45)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- INICIANDO MONITORAMENTO EM TEMPO REAL ---")
        cep_analise = input("Digite o CEP da região para monitorar (Ex: 04551-000)")

        #Simulação de leitura de sensor 
        for i in range(3):
            #Simulando a água subindo a cada leitura
            distancia_simulada = 100 - (i * 35)
            status = simular_sensor(distancia_simulada)

            #Saída formatada
            print(f"[Leitura {i+1}] Distância da água até o sensor: {distancia_simulada}cm | Status: {status}")
            break

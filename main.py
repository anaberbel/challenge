# Inicialize o status das opções
opcoes = {
    1: {"nome": "Libras (Língua Brasileira de Sinais)", "descricao_curta": "Libras", "status": "desativado"},
    2: {"nome": "Alto Contraste", "descricao_curta": "Alto Contraste", "status": "desativado"},
    3: {"nome": "Selecionar modo para daltonismo", "descricao_curta": "Alto Contraste", "status": "desativado", "modo_daltonismo": None},
    4: {"nome": "Aumentar tamanho da fonte", "descricao_curta": "Aumentar Tamanho da Fonte", "status": "desativado"},
    5: {"nome": "Diminuir tamanho da fonte", "descricao_curta": "Diminuir Tamanho da Fonte", "status": "desativado"},
}

modos_daltonismo = {
    1: {"nome": "Deuteranopia"},
    2: {"nome": "Protanopia"},
    3: {"nome": "Tritanopia"},
}

# Função para alternar o status de uma opção
def alternar_opcao(opcao):

    #ativa tudo menos daltonismo
    if opcoes[opcao]["status"] == "desativado" and opcao:
        opcoes[opcao]["status"] = "ativado"
        print(f"{opcoes[opcao]['descricao_curta']} agora está ativado")
     #desativa tudo menos daltonismo        
    elif opcoes[opcao]["status"] == "ativado":
        opcoes[opcao]["status"] = "desativado"
        print(f"Opção {opcao} agora está desativada")


# Função para selecionar o modo para daltonismo
def selecionar_modo_daltonismo():
    print("\nSelecione um modo para daltonismo:")
    print("1. Deuteranopia")
    print("2. Protanopia")
    print("3. Tritanopia")
    print("4. Desativar modo para daltonismo")
    modo = int(input("\nInforme o valor numérico do modo: "))
    if modo == 4:
        opcoes[3]["modo_daltonismo"] = None
        opcoes[3]["status"] = "desativado"
        print("Modo daltonismo agora está desativado")
    else:
        opcoes[3]["modo_daltonismo"] = modos_daltonismo[modo]["nome"]
        opcoes[3]["status"] = "ativado"
        print(f"\nModo para daltonismo ativado: {modos_daltonismo[modo]['nome']}")



# Loop principal do programa
while True:
    print("\nOpções de acessibilidade:\n")
    for opcao, dados in opcoes.items():
        print(f"{opcao}. {dados['nome']} ({dados['status']}) {dados['modo_daltonismo'] if 'modo_daltonismo' in dados and dados['modo_daltonismo'] is not None else ''}")
    print("6. Fechar menu\n")

    escolha = int(input("Informe o valor numérico da sua escolha: "))
    if escolha == 6:
        break
    elif escolha == 3:
        selecionar_modo_daltonismo()

    if escolha != 3:
        alternar_opcao(escolha)
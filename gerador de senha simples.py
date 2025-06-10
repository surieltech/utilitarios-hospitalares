senha_geral = 0
senha_preferencial = 0

def gerar_senha(tipo):
    global senha_geral, senha_preferencial

    if tipo == 'G':
        senha_geral += 1
        return f"G{senha_geral:03d}"
    elif tipo == 'P':
        senha_preferencial += 1
        return f"P{senha_preferencial:03d}"
    else:
        return "Tipo de senha inválido."

while True:
    print("\n=== Gerador de Senhas ===")
    print("1 - Gerar senha geral")
    print("2 - Gerar senha preferencial")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print(f"Sua senha é: {gerar_senha('G')}")
    elif opcao == '2':
        print(f"Sua senha é: {gerar_senha('P')}")
    elif opcao == '0':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
senha_atual = 0

while True:
    entrada = input("\nPressione ENTER para gerar uma nova senha ou digite 'sair' para encerrar: ")

    if entrada.lower() == 'sair':
        print("Sistema encerrado.")
        break

    senha_atual += 1
    print(f"Sua senha é: {senha_atual:03d}")
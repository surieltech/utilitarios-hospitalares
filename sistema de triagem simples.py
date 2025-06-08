def exibir_menu():
    print("\n=== SISTEMA DE TRIAGEM ===")
    print("1 - Dor no peito")
    print("2 - Dificuldade para respirar")
    print("3 - Hemorragia")
    print("4 - Febre alta (acima de 39°C)")
    print("5 - Dor moderada/leve")
    print("6 - Mal-estar geral")
    print("0 - Sair")

def classificar_sintoma(opcao):
    if opcao in ["1", "2", "3"]:
        return "🔴 Emergência - procure socorro imediato!"
    elif opcao == "4":
        return "🟠 Urgência - busque atendimento logo quanto antes)"
    elif opcao == "5":
        return "🟡 Prioridade média "
    elif opcao == "6":
        return "🟢 Baixa prioridade"
    else:
        return None

def triagem():
    print("\n--- Nova Triagem ---")
    nome = input("Nome do paciente: ").strip()
    while True:
        exibir_menu()
        opcao = input("Escolha o sintoma principal (0 para sair): ").strip()
        if opcao == "0":
            print("Encerrando triagem para este paciente.\n")
            break
        categoria = classificar_sintoma(opcao)
        if categoria:
            print(f"\nPaciente: {nome}\nClassificação: {categoria}\n")
            # Após classificar, encerramos para este paciente
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    print("=== Bem-vindo ao Sistema de Triagem ===")
    while True:
        triagem()
        cont = input("Deseja triar outro paciente? (s/n): ").strip().lower()
        if cont != "s":
            print("Encerrando o sistema de triagem.")
            break
    
main()
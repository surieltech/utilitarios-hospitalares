pacientes = []

print("=== Cadastro de Pacientes ===")

while True:
    nome = input("Nome do paciente: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!\n")

    continuar = input("Deseja cadastrar outro paciente? (s/n): ").lower()
    if continuar == "n":
        break
    if continuar != "s":
        break

# Exibir pacientes cadastrados
print("\n=== Lista de Pacientes Cadastrados ===")
for i, p in enumerate(pacientes, start=1):
    print(f"\nPaciente {i}:")
    print(f"Nome: {p['nome']}")
    print(f"Idade: {p['idade']}")
    print(f"CPF: {p['cpf']}")

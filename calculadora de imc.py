
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Entrada de dados do usuário
    
peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

# Resultado
print(f"\nSeu IMC é: {imc:.3f}")
print(f"Classificação: {classificacao}")
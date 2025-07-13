import time

input ("pressione enter para iniciar a cronometragem do atendimento.")
inicio = time.time()

input ("pressione enter para finalizar a contagem após o atendimento.")
fim = time.time()

duracao = fim - inicio
minutos = int(duracao // 60)
segundos = int(duracao % 60)

print(f"Tempo total de atendimento: {minutos} min e {segundos} s.")




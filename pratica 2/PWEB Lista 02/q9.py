numeros = []
while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == "fim":
        break
    numeros.append(float(numero))
if len(numeros) == 0:
    print("A lista está vazia.")
else:
    media = sum(numeros) / len(numeros)
    print("Média dos números:", media)
numeros = []
while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == "fim":
        break
    numeros.append(int(numero))
numeros.sort(reverse=True)
print("A lista de números em ordem decrescente é:")
for numero in numeros:
    print(numero)
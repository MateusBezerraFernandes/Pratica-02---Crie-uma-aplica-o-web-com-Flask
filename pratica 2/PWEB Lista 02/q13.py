numeros = []
while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == "fim":
        break
    numeros.append(int(numero))
numeros.sort()
print("A lista de números em ordem crescente é:")
for numero in numeros:
    print(numero)
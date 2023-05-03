numeros = []
while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == "fim":
        break
    numeros.append(int(numero))
print("Números pares da lista:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
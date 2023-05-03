numeros = []
while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == "fim":
        break
    numeros.append(int(numero))

if len(numeros) == 0:
    print("A lista vazia.")
else:
    maximo = numeros[0]
    minimo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    print("Maior número da lista:", maximo)
    print("Menor número da lista:", minimo)
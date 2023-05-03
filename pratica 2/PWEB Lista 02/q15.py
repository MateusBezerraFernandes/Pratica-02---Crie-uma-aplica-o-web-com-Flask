numeros = []
while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == "fim":
        break
    numeros.append(int(numero))
x = int(input("Digite o número a ser procurado: "))
if x in numeros:
    print(f"O número {x} está na lista.")
else:
    print(f"O número {x} não está na lista.")
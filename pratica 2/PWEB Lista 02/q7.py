num = int(input("Digite um número: "))
termo1, termo2 = 0, 1

if num <= 0:
    print("Por favor, digite um número positivo.")
else:
    print("Sequência de Fibonacci até o número", num, ":")
    while termo1 <= num:
        print(termo1, end=" ")
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
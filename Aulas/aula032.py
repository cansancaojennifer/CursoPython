numero = input('Digite um numero inteiro: ')


if int(numero) % 2 == 0:
        print("Número par")
else:
        print("Número ímpar")

if numero.isdigit():
        numero = int(numero)
else:
        print("Você não digitou um número inteiro")

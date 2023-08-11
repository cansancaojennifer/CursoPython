valor_1 = input('Digite o primeiro valor: ')
valor_2 = input('Digite o segundo valor: ')

if valor_1 > valor_2:
    print(f'O valor "{valor_1}" é maior que o valor "{valor_2}".')
elif valor_1 < valor_2:
    print(f'O valor "{valor_1}" é menor que o valor "{valor_2}".')
elif valor_1 == valor_2:
    print('Os valores são iguais.')
else:
    print('Ocorreu um erro, tente novamente.')
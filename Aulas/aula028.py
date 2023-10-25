# Exercicio

nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

    if ' ' in nome:
        print('Seu nome contem espacos.')

    else:
        print('Seu nome nao contem espacos.')

else:
    print ('Desculpe voce deixou os campos vazios.')

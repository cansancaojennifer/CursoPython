nome = 'Nicolas'
print(nome[2])
print(nome[-4])
print('Nico' in nome)
print('zero' in nome)
print(10 * '-')
print('Nico' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
   print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
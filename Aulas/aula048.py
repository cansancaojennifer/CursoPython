string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Nicolas',  1.2, []]
lista[-3] = 'Joao'
print(lista)
print(lista[2], type(lista[2]))
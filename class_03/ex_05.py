def multiplicar_por_dois(x):
    return x * 2     
def multiplica_tudo_por_dois(lista):
    return list (map(multiplica_tudo_por_dois, lista))

lista_1 = [ 1, 2, 3, 4, 5 ]

print(lista_1)
lista_2 = multiplica_tudo_por_dois(lista_1)
print(lista_2)


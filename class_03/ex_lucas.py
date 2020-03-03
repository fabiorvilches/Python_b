def calcular_media(lista):
    return sum(lista) / len(lista)

def encontrar_maior_numero(lista):
    return max(lista)

def multiplicar_tudo_por_dois(lista):
    return list(map(lambda x: x * 2, lista))

lista_1 = [ 1, 2, 3, 4, 5 ]

print(lista_1)
lista_2 = multiplicar_tudo_por_dois(lista_1)
print(lista_2)
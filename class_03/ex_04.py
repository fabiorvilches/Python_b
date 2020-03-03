
mail = input ('Digite um mail')

def valida_email(mail):
    contador = 0 
    for letra in mail:
        if letra  == "@":
            contador = contador + 1 
    return True if contador == 1 else False

  
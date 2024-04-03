def mostraPares(lista):
    for x in lista:
        if x % 2 == 0:
            print(x)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares na lista:")
mostraPares(lista)

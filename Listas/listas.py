def compara_listas(lista1, lista2):
    # Lista com os valores que aparecem em ambas as listas
    valores_comuns = list(set(lista1) & set(lista2))
    
    # Lista com os valores que aparecem na primeira lista mas não na segunda
    valores_apenas_lista1 = list(set(lista1) - set(lista2))
    
    # Lista com os valores que aparecem na segunda lista mas não na primeira
    valores_apenas_lista2 = list(set(lista2) - set(lista1))
    
    return valores_comuns, valores_apenas_lista1, valores_apenas_lista2

# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

valores_comuns, valores_apenas_lista1, valores_apenas_lista2 = compara_listas(lista1, lista2)

print("Valores que aparecem nas duas listas:", valores_comuns)
print("Valores que aparecem apenas na primeira lista:", valores_apenas_lista1)
print("Valores que aparecem apenas na segunda lista:", valores_apenas_lista2)

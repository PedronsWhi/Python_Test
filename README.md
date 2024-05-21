Comparação de Listas
Este repositório contém uma função em Python para comparar duas listas e identificar:

Os valores que aparecem em ambas as listas.
Os valores que aparecem apenas na primeira lista.
Os valores que aparecem apenas na segunda lista.
Função compara_listas
Descrição
A função compara_listas recebe duas listas como entrada e retorna três listas como saída:

valores_comuns: uma lista com os valores que aparecem em ambas as listas.
valores_apenas_lista1: uma lista com os valores que aparecem apenas na primeira lista.
valores_apenas_lista2: uma lista com os valores que aparecem apenas na segunda lista.
Implementação
A implementação da função utiliza conjuntos (sets) para identificar facilmente os elementos comuns e os elementos exclusivos de cada lista.

Código
python
Copiar código
def compara_listas(lista1, lista2):
    # Lista com os valores que aparecem em ambas as listas
    valores_comuns = list(set(lista1) & set(lista2))
    
    # Lista com os valores que aparecem na primeira lista mas não na segunda
    valores_apenas_lista1 = list(set(lista1) - set(lista2))
    
    # Lista com os valores que aparecem na segunda lista mas não na primeira
    valores_apenas_lista2 = list(set(lista2) - set(lista1))
    
    return valores_comuns, valores_apenas_lista1, valores_apenas_lista2
Explicação
Conversão para Conjuntos:

set(lista1): Converte lista1 em um conjunto, eliminando duplicatas.
set(lista2): Converte lista2 em um conjunto, eliminando duplicatas.
Interseção de Conjuntos:

set(lista1) & set(lista2): Calcula a interseção dos dois conjuntos, resultando nos valores que aparecem em ambas as listas.
Diferença de Conjuntos:

set(lista1) - set(lista2): Calcula a diferença entre os conjuntos, resultando nos valores que aparecem apenas na primeira lista.
set(lista2) - set(lista1): Calcula a diferença entre os conjuntos, resultando nos valores que aparecem apenas na segunda lista.
Conversão de Volta para Listas:

list(set(lista1) & set(lista2)): Converte a interseção dos conjuntos de volta para uma lista.
list(set(lista1) - set(lista2)): Converte a diferença do primeiro conjunto em relação ao segundo de volta para uma lista.
list(set(lista2) - set(lista1)): Converte a diferença do segundo conjunto em relação ao primeiro de volta para uma lista.
Exemplo de Uso
python
Copiar código
# Listas de exemplo
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Chamando a função
valores_comuns, valores_apenas_lista1, valores_apenas_lista2 = compara_listas(lista1, lista2)

# Exibindo os resultados
print("Valores que aparecem nas duas listas:", valores_comuns)
print("Valores que aparecem apenas na primeira lista:", valores_apenas_lista1)
print("Valores que aparecem apenas na segunda lista:", valores_apenas_lista2)
Resultado Esperado
less
Copiar código
Valores que aparecem nas duas listas: [4, 5]
Valores que aparecem apenas na primeira lista: [1, 2, 3]
Valores que aparecem apenas na segunda lista: [6, 7, 8]

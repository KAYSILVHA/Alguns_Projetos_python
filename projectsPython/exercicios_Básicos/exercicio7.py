def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item


print(maior([1, 2, 3, 4, 5, 6, 7, 8, 35, 0, 7880, 45, 7890, 3]))


def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item


print(menor([1, 2, 3, 4, 5, 6, 7, 8, 35, 0, 7880, 45, 7890, -7, 3]))

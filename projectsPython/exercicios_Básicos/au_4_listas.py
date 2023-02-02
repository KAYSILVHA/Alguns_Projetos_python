# pop , append , count, lower , remove , split

frase = "OI, tudo bem?"
print(frase)
print("---" * 10)

print(frase[0])
print("---" * 10)

print(frase[0:5])
print("---" * 10)

print(frase[0:13:2])
print("---" * 10)

print(frase[::-1])
print("---" * 10)

print(len(frase))
print("---" * 10)

print(frase.lower())
print("---" * 10)

print(str.lower(frase))
print("---" * 10)

frase_separada = frase.split(',')
print(frase_separada)
print("---" * 10)

frase_nova = frase + ' Como você está?'
print(frase_nova)
print("---" * 10)
print("---" * 10)

lista_nomes = ['Ana', 'Gaby', 'Jotinha', 'Bianca', 'Malu']

print(lista_nomes[0])
print("---" * 10)

print(lista_nomes[-1])
print("---" * 10)

print(lista_nomes[-1:-6:-1])
print("---" * 10)

lista_nomes.append('Catarina')
print(lista_nomes)
print("---" * 10)

lista_nomes.remove('Catarina')
print(lista_nomes)
print("---" * 10)

lista_nomes.insert(1, 'Alice')
print(lista_nomes)
print("---" * 10)

lista_nomes[0] = 'Amalia'
print(lista_nomes)
print("---" * 10)

contar = lista_nomes.count('Amalia')
print(contar)
print("---" * 10)

print(len(lista_nomes))
print("---" * 10)

print(lista_nomes.pop())
print(lista_nomes)
print("---" * 10)

lista_nomes.clear()
print(lista_nomes)

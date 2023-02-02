'''
open('arquivo.txt, 'r') abre o arquivo no modo leitura
open('arquivo.txt, 'w') cria ou sobescreve um arquivo no modo escrita
open('arquivo.txt, 'r+') abre um arquivo no modo leitura e escrita
open('arquivo.txt, 'a') abre o arquivo no modo append(nao vai sumir)


arquivo = open('arquivo.txt', 'w')
for i in range(1, 1001):
    arquivo.write(str(i) + "\n")

# arquivo.write('Eai, pessoal')



arquivo = open('arquivo.txt', 'r')
print(arquivo.read())

'''
arquivo = open('arquivo.txt', 'r')
for linha in arquivo:
    print((linha))
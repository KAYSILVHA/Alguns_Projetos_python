print("-----Controle de festinhas-----")

numero_de_convidados = int(input("Qual o numero de pessoas que você irá convidar: "))
lista_de_convidados = []

i = 1
while i <= numero_de_convidados:
    nome_do_convidado = input("Adicione o nome do convidado " + str(i) + ": ")
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print("\nSerão", numero_de_convidados, "convidados!")

print("\nLISTA DE CONVIDADOS")
for convidado in lista_de_convidados:
    print(convidado)

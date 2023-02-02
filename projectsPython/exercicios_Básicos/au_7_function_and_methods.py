# sempre que se passa parametros é uma função
#Função= voce passa o x e recebe o resultado y
#metodo= nao tem retorno
# Definindo uma função

def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp


retorno = soma(75, 1289)
print(retorno)


# funcoes nao precisam ter argumentos e nem return obrigatoriamente

def imprime_oi():
    print('Oi')

imprime_oi()


def tem_sete_itens(argumento):
     if len(argumento) == 7:
      return True
     else:
         return False

print(tem_sete_itens('1234567'))
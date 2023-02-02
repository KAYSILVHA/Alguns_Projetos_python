# comparações: ==  !==  >  <  >=  <=
# comparações: and  or not


print("-----RESPONDA AS PERGUNTAS-----")
print("Você já pode entrar no exército?")
print("--"*10)
idade = int(input("Qual a sua idade? "))
peso = float(input("Quantos quilos você pesa? "))
altura = float(input("Qual a sua altura? "))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print("Você pode se alistar no exército!")
else:
    print("Você não tem os pré-requesitos para se alistar! ")
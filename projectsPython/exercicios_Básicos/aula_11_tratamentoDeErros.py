try:
    a = 1200 / 0

except ZeroDivisionError:
    print('Não da para fazer divisão por zero!')

except NameError:
    print('Você digitou algo errado')

except Exception as erro:
    print("aconteceu um erro: ", erro)



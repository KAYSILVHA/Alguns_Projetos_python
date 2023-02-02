from veiculo import Veiculo
from carro import  Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)


print("CAMINHÃO ROSA")
print('Cor:', caminhao_rosa.cor)
print('Marca:', caminhao_rosa.marca)
print('Tanque:', caminhao_rosa.tanque, 'litros')

print('')

print("CARRO AZUL")
carro_azul = Carro('azul', 'bmw', 30)
print('Cor:', carro_azul.cor)
print('Marca:', carro_azul.marca)
print('Tanque:', carro_azul.tanque, 'litros')

print('')

carro_azul.abaster(35)
print('Tanque:', carro_azul.tanque, 'litros')
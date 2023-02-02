# herança
from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)
    def abaster(self, litros):
        if self.tanque + litros > 50:
            print("Tanque cheio!")
        else:
            self.tanque += litros

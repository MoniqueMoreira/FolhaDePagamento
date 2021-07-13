from _typeshed import Self
from datetime import datetime

class CartaoPonto():
    def __init__(self,id_emp="-------", entrada = "-------",saida = "-------", hora = "---------",min = "---------",seg = "---------"):
        self.id_emp = id_emp
        self.ponto = entrada
        self.saida =saida
        self.hora = hora
        self.min = min
        self.seg = seg
    
    def setEntrada(self, id_emp):
        self.id_emp = id_emp
        self.entrada = datetime.now()
        print("Ponto Batido com sucesso:")
        CartaoPonto.toPonto(self)
        h = input("ENTER")

    def setSaida(self):
        self.saida = datetime.now()
        self.hora = int(self.saida.hour)- int(self.entrada.hour)
        self.min = int(self.saida.minute)- int(self.entrada.minute)
        self.seg = int(self.saida.second)- int(self.entrada.second)
        print("Ponto Batido com sucesso:")
        CartaoPonto.toPonto(self)
        h = input("ENTER")

    def getHoras(self):
        return self.hora


    def toPonto(self):
        print("ENTRADA : {}\nSAÍDA: {}\nHORAS TRABALHADAS: {}:{}:{}".format(self.entrada,self.saida,self.hora,self.min,self.seg))
        
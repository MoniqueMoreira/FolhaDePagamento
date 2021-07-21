from datetime import datetime

class CartaoPonto():
    def __init__(self,id_emp="-------",data = "--------", hora = "---------"):
        self.id_emp = id_emp
        self.data =data
        self.hora = hora

    def setpPonto(self):
        self.data = input("Digite a Data:\n>>>")
        self.hora = float(input("Digite a quantidade de Horas.minutos trabalhados:\n>>>"))
        print("Ponto Batido com sucesso:")
        CartaoPonto.toPonto(self)
        

    def toPonto(self):
        print("Data: {}\nHORAS TRABALHADAS: {}".format(self.data,self.hora))
        h = input("ENTER")
   
        
from datetime import datetime

class Vendas():
    def __init__(self,id_emp = "-------", venda = "--------", data = "-------"):
        self.id_emp = id_emp
        self.venda = venda
        self.data = data

    def cadrastra(self, id_emp):

        venda = float(input("Digite o VAlOR da venda:\n>>>"))
        self.venda = venda
        self.data = input("Digite o Dia:\n>>>")
        print("Venda cadrastada com sucesso!!")
        Vendas.toVenda(self)
        


    def toVenda(self):
        print("ID do empregado: {}\nValor da venda: {}\nData: {}".format(self.id_emp,self.venda,self.data))
        h = input("ENTER")
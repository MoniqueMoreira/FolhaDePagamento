from datetime import datetime

class Vendas():
    def __init__(self,id_emp = "-------", venda = "--------", data = "-------"):
        self.id_emp = id_emp
        self.venda = venda
        self.data = data

    def cadrastra(self, id_emp):
        self.id_emp =id_emp
        venda = float(input("Digite o VAlOR da venda:\n>>>"))
        self.venda = venda
        self.data = datetime.now()
        print("Venda cadrastada com sucesso!!")
        Vendas.toVenda(self)
        h= input("ENTER")


    def toVenda(self):
        print("ID do empregado: {}\nValor da venda: {}\nData: {}".format(self.id_emp,self.venda,self.data))
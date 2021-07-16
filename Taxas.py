from datetime import datetime

class Taxas():
    def __init__(self,id_emp="--------", taxa ="-------", motivo = "--------", data = "--------" ):
        self.id_emp = id_emp
        self.taxa = taxa
        self.motivo = motivo
        self.data = data

    def cadastrar(self,id_emp):
        self.id_emp = id_emp
        motivo  = input("Motivo da taxa:\n>>>")
        self.motivo =motivo
        taxa = float(input("Valor da TAXA:\n>>>"))
        self.taxa = taxa
        self.data = datetime.now()
        print("Venda cadrastada com sucesso!!")
        Taxas.toTaxa(self)
        h= input("ENTER")

    def toTaxa(self):
        print("Motivo da taxa: {}\nValor da taxa: {}\nData: {}".format(self.motivo,self.taxa,self.data))
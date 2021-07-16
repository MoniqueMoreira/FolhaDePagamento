class Sindicato():

    def __init__(self,id_emp="-------",id_sind="-------",taxa="-------",adicionais=None):
        self.id_emp = id_emp
        self.id_sind = id_sind
        self.taxa = taxa
        self.adicionais = adicionais

    def cadrastra_emp(self, id_emp):
        self.id_emp = id_emp
        self.id_sind = id_emp + 1000
        taxa = float(input("Digite a TAXA MENSAL do sindicato:\n>>>"))
        self.taxa = taxa

    def setTaxa(self):
        taxa = float(input("Digite a TAXA MENSAL do sindicato:\n>>>"))
        self.taxa = taxa

    def getTaxa(self):
        return self.taxa

    def setAdicionais(self):
        adicionais = float(input("Digite as TAXA ADICIONAL do sindicato:\n>>>"))
        self.adicionais = adicionais

    def getAdicionais(self):
        return self.adicionais

    def toEmp_sind(self):
        print("ID do Sindicato: {}\n Taxas Mensal: {}".format(self.id_sind,self.taxa))

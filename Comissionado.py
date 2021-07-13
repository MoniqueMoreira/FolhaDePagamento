from Empregados import Empregados

class Comissionado(Empregados):

    def __init__(self,nome ="--------",endereco="--------",id_emp = "--------",tipo = "--------",sindicato = "--------", pagamento = "--------", salario = "--------",percentual = "--------"):
        super().__init__(nome=nome, endereco=endereco, id_emp=id_emp, tipo=tipo, sindicato=sindicato, pagamento=pagamento)
        self.salario = salario
        self.percentual = percentual

    def setcadrasta (self,id_emp):
        self.tipo = "Comissionado"
        super().cadrastra(id_emp)
        Comissionado.setSalario(self)
        Comissionado.setPercentual(self)

    def modificar_cadrastro(self):
        i=0
        while(i!=1):
            k=int(input("Deseja ALTERA qual dados do empregado:\n1-Nome\n2-Endereço\n3-Forma de Pagamento\n4-Sindicato\n5-Valor Salário\n>>>"))
            if k == 1:
                super().setNome()
                i=1
            elif k==2:
                super().setEndereco()
                i=1
            elif k==3:
                super().setPagamento()
                i=1
            elif k==4:
                super().setSindicato()
                i=1
            elif k==5:
                Comissionado.setSalario()
                Comissionado.setPercentual()
                i=1
            else:
                print("Opção Inválida")

    def setSalario(self):
        salario = float(input("Digite SALÁRIO do empregado\n>>>"))
        self.salario = salario

    def setPercentual(self):
        percentual =float(input("Digite PERCENTUAL DA COMISSÃO do empregado\n>>>"))
        self.percentual =percentual
    
    def toEmpregado(self):
        print("ID: {}\nNome: {}\nEndereço: {}\nTipo: {}\nSalario: {}\nPercentual: {}\nTipo de Pagamento: {}\nSindicato: {}".format(self.id_emp,self.nome,self.endereco,self.tipo,self.salario,self.percentual,self.pagamento,self.sindicato))

    
from Empregados import Empregados
from datetime import datetime


class Comissionado(Empregados):

    def __init__(self,id_emp = "--------",data_cad = "---------",nome ="--------",endereco="--------",tipo = "--------",pagamento = "--------",agenda_emp = "-----------",dia = "------------",mes= "-------------",sindicato = "------------",salario ="------------", percentual = "---------------"):
        super().__init__(id_emp=id_emp, data_cad=data_cad, nome=nome, endereco=endereco, tipo=tipo, pagamento=pagamento, agenda_emp=agenda_emp, dia=dia, mes=mes, sindicato=sindicato)
        self.salario = salario
        self.percentual = percentual


    def setcadrasta (self,id_emp):
        self.tipo = "Comissionado"
        self.agenda_emp = "Bi-Semanalmente"
        super().cadrastra(id_emp)
        Comissionado.setSalario(self)
        Comissionado.setPercentual(self)
        Comissionado.setData(self)
    
    def setData(self):
        self.data_cad = datetime.now()
        self.dia = "Sexta-feira"

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
        super().toEmpregados()
        print("Salario: {}\nPercentual: {}".format(self.salario,self.percentual))
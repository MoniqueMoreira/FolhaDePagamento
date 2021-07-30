from Empregados import Empregados
from datetime import datetime

class Horista(Empregados):

    def __init__(self,id_emp = "--------",data_cad = "---------",nome ="--------",endereco="--------",tipo = "--------",pagamento = "--------",agenda_emp = "-----------",dia = "------------",mes= "-------------",sindicato = "------------",hora ="------------" ):
        super().__init__(id_emp=id_emp, data_cad=data_cad, nome=nome, endereco=endereco, tipo=tipo, pagamento=pagamento, agenda_emp=agenda_emp, dia=dia, mes=mes, sindicato=sindicato)
        self.hora = hora 

    def setcadrasta (self,id_emp):
        self.tipo = "Horista"
        self.agenda_emp = "Semanalmente"
        super().cadrastra(id_emp)
        Horista.setHora(self)
        Horista.setData(self)

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
                Horista.setHora()
                i=1
            else:
                print("Opção Inválida")

    def setHora(self):
        hora = float(input("Digite VALOR/HORA do empregado\n>>>"))
        self.hora = hora
    
    def toEmpregado(self):
        super().toEmpregados()
        print("Valor/Hora: {}".format(self.hora))

    
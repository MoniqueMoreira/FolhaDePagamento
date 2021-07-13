from Empregados import Empregados

class Horista(Empregados):

    def __init__(self,nome ="--------",endereco="--------",id_emp = "--------",tipo = "--------",sindicato = "--------", pagamento = "--------", hora = "--------"):
        super().__init__(nome=nome, endereco=endereco, id_emp=id_emp, tipo=tipo, sindicato=sindicato, pagamento=pagamento)
        self.hora = hora

    def setcadrasta (self,id_emp):
        self.tipo = "Horista"
        super().cadrastra(id_emp)
        Horista.setHora(self)

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
        print("ID: {}\nNome: {}\nEndereço: {}\nTipo: {}\nValor/Hora: {}\nTipo de Pagamento: {}\nSindicato: {}".format(self.id_emp,self.nome,self.endereco,self.tipo,self.hora,self.pagamento,self.sindicato))

    
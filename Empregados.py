from datetime import datetime
from Sindicato import Sindicato
from Banco import Banco

class Empregados(Sindicato,Banco):
    def __init__(self,id_emp = "--------",data_cad = "---------",nome ="--------",endereco="--------",tipo = "--------",pagamento = "--------",agenda_emp = "-----------",dia = "------------",mes= "-------------",ult_salario= "-------------",sindicato = "--------"):
        self.id_emp = id_emp
        self.data_cad= data_cad
        self.nome = nome
        self.endereco= endereco
        self.tipo = tipo
        self.pagamento = pagamento
        self.agenda_emp = agenda_emp
        self.dia = dia
        self.mes = mes
        self.ult_salario = ult_salario
        self.sindicato = sindicato
        self.pontos= []
        self.vendas = []
        self.taxas = []
        
    def cadrastra(self, id_emp):
        print("Cadrastra NOVO funcinario")
        self.id_emp = id_emp
        Empregados.setNome(self)
        Empregados.setEndereco(self)
        Empregados.setPagamento(self)
        Empregados.setSindicato(self)
       
    def setNome(self):
        nome = str(input("Digite o NOME do empregado\n>>>"))
        self.nome = nome.capitalize()

    def setEndereco(self):
        endereco = str(input("Digite o ENDEREÇO do empregado\n>>>"))
        self.endereco = endereco.capitalize()
    
    def setSindicato(self):
        i=0
        while(i!=1):
            k = int(input("O empregado PERTENCE AO SINDICATO?\n1-Sim\n2-Não\n>>>"))
            if k != 1 and k != 2:
                print("DADO INVÁLIDO")
            else:
                if k == 1:
                    self.sindicato = "Sim"
                    Sindicato.cadrastra_emp(self,self.id_emp)
                    i=1
                elif k==2:
                    self.sindicato = "Não"
                    i=1
                else:
                    print("DADO INVÁLIDO")

    def setPagamento(self):
        i=0
        while(i!=1):
            k = int(input("Digite o TIPO DE PAGAMENTO\n1-Correios\n2-Em Mãos\n3-Conta bancária\n>>>"))
            if k != 1 and k !=2  and k != 3:
                print("FORMA DE PAGAMNTO INVÁLIDA")
            else:
                if k==1:
                    self.pagamento = "Correios"
                    i=1
                elif k==2:
                    self.pagamento = "Em Mãos"
                    i=1
                elif k==3:
                    self.pagamento = "Conta bancária"
                    Banco.cadrastra(self)
                    i=1
                else:
                    print("FORMA DE PAGAMNTO INVÁLIDA")

    def toEmpregados(self):
        print("ID: {}\nNome: {}\nEndereço: {}\nTipo: {}\nData de Cadrstro: {}\nDia: {}\nTipo de Pagamento: {}\nSindicato: {}\nTipo de Agenda: {}".format(self.id_emp,self.nome,self.endereco,self.tipo,self.data_cad,self.dia,self.pagamento,self.sindicato, self.agenda_emp))
        if self.sindicato == "Sim":
            Sindicato.toEmp_sind(self)
        if self.pagamento == "Conta bancária":
            Banco.toBanco(self)

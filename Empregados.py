class Empregados():
    def __init__(self,nome ="--------",endereco="--------",id_emp = "--------",tipo = "--------",sindicato = "--------", pagamento = "--------"):
        self.nome = nome
        self.endereco= endereco
        self.id_emp = id_emp
        self.tipo = tipo
        self.sindicato = sindicato
        self.pagamento = pagamento

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
                    i=1
                else:
                    print("FORMA DE PAGAMNTO INVÁLIDA")
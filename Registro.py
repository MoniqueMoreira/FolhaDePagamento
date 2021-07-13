'''
1 Adição de um empregado Um novo empregado é adicionado ao sistema. 
2 Remoção de um empregado.
3 Lançar um Cartão de Ponto.
4 Lançar um Resultado Venda. 
5 Lançar uma taxa de serviço.
6 Alterar detalhes de um empregado. 
7 Rodar a folha de pagamento para hoje.
8 Undo/redo.
9 Agenda de Pagamento.
10 Criação de Novas Agendas de Pagamento
'''

from Comissionado import Comissionado
from Horista import Horista
from Empregados import Empregados
from Assalariado import Assalariado
import random
import os
clear = lambda: os.system('cls')


class Registro(Empregados):

    emp_cadrastados = []
    num_emp = len(emp_cadrastados)

    def mostra_emp():
        clear()
        print("Funcionarios Disponíveis:\n")
        for i in Registro.emp_cadrastados:
            i.toEmpregado()
            print("\n")
        h=input("ENTER")

    def add_empregado():
        clear()
        id_emp=Registro.gera_id()
        i=0
        while(i!=1):

            k= int(input("Digite TIPO\n1-Horista\n2-Assalariado\n3-Comissionado\n>>>"))
            if k == 1:
                new = Horista()
                new.setcadrasta(id_emp)
                i=1
            elif k==2:
                new = Assalariado()
                new.setcadrasta(id_emp)
                i=1

            elif k==3:
                new = Comissionado()
                new.setcadrasta(id_emp)
                i=1

            else:
                print("TIPO INVÁLIDO")

        Registro.emp_cadrastados.append(new)
        clear()
        print("Empregado cadrastadro com  sucesso!!!")
        new.toEmpregado()
        h=input("ENTER")

    def gera_id():
        k=0
        while(k!=1):
            x = random.randrange(1,1000)
            for i in range(Registro.num_emp):
                if i==x or i==Registro.num_emp:
                    break
            return x


    def remover_empregado():
        #ERRO
        k=int(input("Sabe o ID do funcionario?\n1-Sim\n2-Não\n>>>"))
        if k==1:
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    Registro.emp_cadrastados.remove(i)
                else:
                    print("Empregado Nâo Cadrastado")
        else:
            Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    Registro.emp_cadrastados.remove(i)
                else:
                    print("Empregado Nâo Cadrastado")

    def cartao_ponto():
        pass
    
    def lanca_vendas():
        pass
    
    def lanca_taxa():
        pass
    
    def altera_dados():
        k=int(input("Sabe o ID do funcionario?\n1-Sim\n2-Não\n>>>"))
        if k==1:
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                   i.modificar_cadrastro()
                else:
                    print("Empregado Nâo Cadrastado")
        else:
            Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                   i.modificar_cadrastro()
                else:
                    print("Empregado Nâo Cadrastado")
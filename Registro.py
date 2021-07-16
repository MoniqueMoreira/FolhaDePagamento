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

from Taxas import Taxas
from Vendas import Vendas
from CartaoPonto import CartaoPonto
from Comissionado import Comissionado
from Horista import Horista
from Empregados import Empregados
from Assalariado import Assalariado
import random
import os
clear = lambda: os.system('cls')


class Registro():

    emp_cadrastados = []
    ponto = []
    vendas = []
    taxas = []
    num_emp = len(emp_cadrastados)

    def mostra_emp():
        clear()
        print("Funcionarios Disponíveis:\n")
        for i in Registro.emp_cadrastados:
            i.toEmpregado()
            print("\n")
        h=input("ENTER")

    def gera_id():
        k=0
        while(k!=1):
            x = random.randrange(1,1000)
            for i in range(Registro.num_emp):
                if i==x or i==Registro.num_emp:
                    break
            return x

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

    def remover_empregado():
        k=int(input("Sabe o ID do funcionario?\n1-Sim\n2-Não\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    Registro.emp_cadrastados.remove(i)
                    return
            print("Empregado Não Cadrastado")
        else:
            print("OPÇÃO INVÁLIDA")
        
    def altera_dados():
        k=int(input("Sabe o ID do Empregado:\n1-Sim\n2-Não\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp = int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                   i.modificar_cadrastro()
                   return
            print("Empregado Não Cadrastado")
        else:
            print("OPÇÃO INVÁLIDA")
        
    def cartao_ponto():
        k = int(input("Sabe o ID do Empregado:\n1-SIM\n2-NÃO\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    k = int(input("Deseja BATER PONTO:\n1-ENTRADA\n2-SAÍDA\n>>>"))
                    if k==1:
                        novo_ponto = CartaoPonto()
                        novo_ponto.setEntrada(emp)
                        Registro.ponto.append(novo_ponto)
                        return
                    elif k==2:
                        for g in Registro.ponto:
                            if emp == g.id_emp and g.saida == "-------" :
                                g.setSaida()
                                return
                        print("Ponto indisponivel ou já foi batido ")
                    else:
                        print("OPÇÃO INVÁLIDA")
                        return
            print("Empregado Não Cadrastado")
        else:
            print("OPÇÃO INVÁLIDA")

    def ver_cartao_ponto():
        k = int(input("Sabe o ID do Empregado:\n1-SIM\n2-NÃO\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.ponto:
                if emp == i.id_emp:
                    i.toPonto()
                    return
            print("Empregado Não Cadrastado")
        else:
            print("OPÇÃO INVÁLIDA")

    def ver_vendas():
        k = int(input("Sabe o ID do Empregado:\n1-SIM\n2-NÃO\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.vendas:
                if emp == i.id_emp:
                    i.toVenda()
                    return
            print("Empregado Não Cadrastado")
            k = input("ENTER")
        else:
            print("OPÇÃO INVÁLIDA")
            k = input("ENTER")
    
    def lanca_vendas():
        k=int(input("Sabe o ID do Empregado:\n1-Sim\n2-Não\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp = int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    new_venda = Vendas()
                    new_venda.cadrastra(emp)
                    Registro.vendas.append(new_venda)
                    return
            print("Empregado Não Cadrastado")
            h = input("ENTER")
        else:
            print("OPÇÃO INVÁLIDA")
            h = input("ENTER")


    def ver_taxas():
        k = int(input("Sabe o ID do Empregado:\n1-SIM\n2-NÃO\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.vendas:
                if emp == i.id_emp:
                    i.toTaxa()
                    return
            print("Empregado Não Cadrastado")
            k = input("ENTER")
        else:
            print("OPÇÃO INVÁLIDA")
            k = input("ENTER")

    def lanca_taxa():
        k=int(input("Sabe o ID do Empregado:\n1-Sim\n2-Não\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp = int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    new_taxa = Taxas()
                    new_taxa.cadastrar(emp)
                    Registro.taxas.append(new_taxa)
                    return
            print("Empregado Não Cadrastado")
            h = input("ENTER")
        else:
            print("OPÇÃO INVÁLIDA")
            h = input("ENTER")
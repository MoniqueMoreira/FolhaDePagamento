from Agenda import Agenda
from datetime import datetime
import pickle
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

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

class Registro():

    emp_cadrastados =  pickle.load(open( "emp_cadrastados.pickls", "rb" ))
    agenda_disp =  pickle.load(open( "agendas_disp.pickls", "rb" ))
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
        pickle.dump( Registro.emp_cadrastados, open( "emp_cadrastados.pickls", "wb" ) )
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
                    pickle.dump( Registro.emp_cadrastados, open( "emp_cadrastados.pickls", "wb" ) )
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
                   pickle.dump( Registro.emp_cadrastados, open( "emp_cadrastados.pickls", "wb" ) )
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
                    novo_ponto = CartaoPonto()
                    novo_ponto.setpPonto()
                    i.pontos.append(novo_ponto)
            print("Empregado Não Cadrastado")
        else:
            print("OPÇÃO INVÁLIDA")

    def ver_cartao_ponto():
        k = int(input("Sabe o ID do Empregado:\n1-SIM\n2-NÃO\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    for d in i.pontos:
                        d.toPonto()
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
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    for d in i.vendas:
                        d.toVenda()
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
                    i.vendas.append(new_venda)
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
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    for d in i.taxas:
                        d.toTaxa()
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
                    i.taxas.append(new_taxa)
                    return
            print("Empregado Não Cadrastado")
            h = input("ENTER")
        else:
            print("OPÇÃO INVÁLIDA")
            h = input("ENTER")

    def criar_agenda():
        nAgenda =[]
        print("Nova Agenda:")
        i = 0
        while(i!=1):
            nAgenda = Agenda()
            nAgenda.criar_agenda()
            k = int(input("Deseja Adicionar outra opção?\n1-Sim\n2-Não\n>>>"))
            if k == 2:
                Registro.agenda_disp.append(nAgenda)
                pickle.dump( Registro.agenda_disp, open( "agendas_disp.pickls", "wb" ) )
                i = 1
        print("Nova agenda foi cria com Sucesso!!!")

    def mostra_agendas():
        print("Agendas Disponiveis:")
        for x in Registro.agenda_disp:
            x.toAgenda()
        f = input("ENTER")

    def muda_agenda_emp():
        k = int(input("Sabe o ID do Empregado:\n1-SIM\n2-NÃO\n>>>"))
        if k==1 or k==2:
            if k==2:
                Registro.mostra_emp()
            emp= int(input("Digite o ID do empregado:\n>>>"))
            for i in Registro.emp_cadrastados:
                if emp == i.id_emp:
                    Registro.mostra_agendas()
                    ag = input("Digite a Agenda Desejada:\n>>>")
                    i.agenda_emp = ag
                    if ag == "Semanalmente"  or ag == "Bi-Semanalmente":
                        i.dia = int(input("Digite o Dia da Semana escolhido da agenda"))
                    elif ag == "Mensalmente":
                        i.dia = int(input("Digite o Dia do Mês escolhido da agenda"))
                    else:
                        i.dia = int(input("Digite o Dia do Mês escolhido da agenda"))
                        i.mes = int(input("Digite o Mês do Ano escolhido da agenda"))
                    pickle.dump( Registro.emp_cadrastados, open( "emp_cadrastados.pickls", "wb" ) )
                    k = input("ENTER")
                    return
            print("Empregado Não Cadrastado")
            k = input("ENTER")
        else:
            print("OPÇÃO INVÁLIDA")
            k = input("ENTER")

    def folha():
        dia, mes,ano = input("Digite o Dia/Mês/Ano respectivamente(Ex. 23/07/2021):\n>>>").split('/')
        ano = int(ano)
        dia = int(dia)
        mes = int(mes)
        data=datetime(year=ano,month=mes,day=dia)
        indice_da_semana = data.weekday()
        dia_da_semana = DIAS[indice_da_semana]
        for x in Registro.emp_cadrastados:
            if x.agenda_emp == "Semanalmente":
                if x.dia == dia_da_semana:
                    x.toEmpregado()
            elif x.agenda_emp == "Bi-Semanalmente":
                if x.dia == dia_da_semana:
                    if x.ult_salario == "-------------":
                        x.ult_salario = dia
                        x.toEmpregado()
                    else:
                        print(x.ult_salario)
                        print((x.ult_salario + 14)%31)
                        if ((x.ult_salario + 14)%31) == dia:
                            x.ult_salario = dia
                            x.toEmpregado()
            elif x.agenda_emp == "Mensalmente":
                if mes == 1 or mes ==3 or mes == 5 or mes==7 or mes==8 or mes==10 or mes==12:
                    ult_dia = 31
                elif mes == 2:
                    ult_dia = 29
                elif mes == 4 or mes == 6 or mes ==9 or mes == 11:
                    ult_dia = 30

                if x.dia == dia or (x.dia == "$" and dia == ult_dia):
                    x.toEmpregado()
            else:
                if x.dia == dia and x.mes == mes:
                    x.toEmpregado()
        k = input("ENTER")
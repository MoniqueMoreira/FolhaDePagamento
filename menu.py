import os
from Registro import Registro
clear = lambda: os.system('cls')

def menu():
    
    i=0
    while(i!=1):
        clear()
        print("Bem-Vindo ao menu Principal")
        z= int(input("1-Adicionar Novo Empregado\n2-Remover Empregado\n3-Mostra Empregados\n4-Cartão de Ponto\n5-Vendas\n6-Taxas\n7-Altera Dados\n8-Agenda\n9-Folha\n10-Sair\n"))
        if z==1:
            Registro.add_empregado()
        elif z==2:
            Registro.remover_empregado()
        elif z==3:
            Registro.mostra_emp()
        elif z==4:
            k= int(input("Deseja:\n1-Bater Ponto\n2-Ver Ponto\n>>>"))
            if k==1:
                Registro.cartao_ponto()
            elif k==2:
                Registro.ver_cartao_ponto()
            else:
                print("OPÇÃO INVÁLIDA")
                h = input("ENTER")
        elif z==5:
            k= int(input("Deseja:\n1-Lança Venda\n2-Ver Vendas\n>>>"))
            if k==1:
                Registro.lanca_vendas()
            elif k==2:
                Registro.ver_vendas()
            else:
                print("OPÇÃO INVÁLIDA")
                h = input("ENTER")
        elif z==6:
            k= int(input("Deseja:\n1-Lança Taxa\n2-Ver Taxas\n>>>"))
            if k==1:
                Registro.lanca_taxa()
            elif k==2:
                Registro.ver_taxas()
            else:
                print("OPÇÃO INVÁLIDA")
                h = input("ENTER")
        elif z==7:
            Registro.altera_dados()
        elif z==8:
            k= int(input("Deseja:\n1-Ver Agendas Disponiveis\n2-Cria Nova Agenda\n3-Mudar Agenda de pagamento de um empregado\n>>>"))
            if k==1:
                Registro.mostra_agendas()
            elif k==2:
                Registro.criar_agenda()
            elif k==3:
                Registro.muda_agenda_emp()
            else:
                print("OPÇÃO INVÁLIDA")
                h = input("ENTER")
        elif z==9:
            Registro.folha()
        elif z==10:
            break 
        else:
            print("Opção Inválida")
        
menu()
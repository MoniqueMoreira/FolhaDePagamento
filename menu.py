import os
from Registro import Registro
clear = lambda: os.system('cls')

def menu():
    
    i=0
    while(i!=1):
        clear()
        print("Bem-Vindo ao menu Principal")

        z= int(input("1-Adicionar Novo Empregado\n2-Remover Empregado\n3-Mostra Empregados\n4-Cartão de Ponto\n5-Lança Vendas\n6-Lança Taxas\n7-Altera Dados\n8-Sair\n"))
        if z==1:
            Registro.add_empregado()
        elif z==2:
            Registro.remover_empregado()
        elif z==3:
            Registro.mostra_emp()
        elif z==4:
            Registro.cartao_ponto()
        elif z==5:
            Registro.lanca_vendas()
        elif z==6:
            Registro.lanca_taxa()
        elif z==7:
            Registro.altera_dados()
        elif z==8:
            break
        else:
            print("Opção Inválida")
        
menu()
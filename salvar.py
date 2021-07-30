'''
    MUITO CUIDADO ESCUTAR ESTÁ FUNÇÃO, ELA REDEFINE TODAS AS LISTA USADAS NO PROGRAMAR
'''

from Agenda import Agenda
import pickle
emp_cadrastados=[]
pickle.dump( emp_cadrastados, open( "emp_cadrastados.pickls", "wb" ) )

agenda_disp = []
sem_pad = Agenda()
sem_pad.setSemanalmente()
agenda_disp.append(sem_pad)
men_pad = Agenda()
men_pad.setMensalmente()
agenda_disp.append(men_pad)
bi_pad = Agenda()
bi_pad.setBiSemanalmente()
agenda_disp.append(bi_pad)
pickle.dump( agenda_disp, open( "agendas_disp.pickls", "wb" ) )
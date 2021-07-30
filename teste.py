from datetime import datetime

data_cad = datetime.now()
mes = data_cad.month
if mes == 1:
    dia = 31
elif mes == 2:
    dia = 29
elif mes == 3:
    dia = 31
elif mes == 4:
    dia = 30
elif mes == 5:
    dia = 31
elif mes == 6:
    dia = 30
elif mes == 7:
    dia = 31
elif mes == 8:
    dia = 31
elif mes == 9:
    dia = 30 
elif mes == 10:
    dia = 31
elif mes == 11:
    dia = 30
else:
    dia = 31

print(dia)
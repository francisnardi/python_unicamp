import sys

x = []

z = sys.stdin.readlines()

for item in z:
    x.append(item.strip())

#print(x)

y = ['SIM!!!',
     'NAO. As notas da Carla nao foram suficientes.',
     'NAO. O casal nao esta de ferias.',
     'NAO. Nenhum 13o salario foi liberado a tempo.',
     'NAO. O valor total e muito alto.']

def notas_ok(x):
    if float(x[0]) >=7 and float(x[1]) >=7 and float(x[2]) >=7:
        return True
    else:
        return False

def ferias_ok(x):
    if (x[3]) == "Sim" and (x[4]) == "Sim":
        return True
    else:
        return False

def decimo_terceiro_ok(x):
    if int(x[5]) < 11 or int(x[6]) < 11:
        return True
    else:
        return False

def reserva_total_ok(x):
    a = float(x[7]) + float(x[8])
    if a <= 10000.00:
        return True
    else:
        return False

def decisao(x):
    if not reserva_total_ok(x):
        message = y[4]
    if not decimo_terceiro_ok(x):
        message = y[3]
    if not ferias_ok(x):
        message = y[2]
    if not notas_ok(x):
        message = y[1]
    if (notas_ok(x) and ferias_ok(x) and decimo_terceiro_ok(x) and reserva_total_ok(x)):
        message = y[0]
    return message

print(decisao(x))

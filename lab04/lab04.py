cortes = []
notas = []

for i in range(0,3):
    corte = float(input())
    cortes.append(corte)

nota = float(input())
while nota != -1:
    notas.append(nota)
    nota = float(input())
notas.append(nota)

def numero_medalhas(notas, cortes):
    num_medalhas = []
    for i in range(0,3):
        count = 0
        for item in notas:
            if i == 0 and item >= cortes[i] and item < cortes[i] + 1:
                count = count + 1
            elif item >= cortes[i] and item < cortes[i-1]:
                count = count + 1
        num_medalhas.append(count)
    return num_medalhas

def print_medalhas(qtd_medalhas, notas):
    tipo_medalhas = ["ouro", "prata", "bronze"]
    for i in range(0,len(qtd_medalhas)):
        if qtd_medalhas[i] == 0:
            print("Nenhum participante recebeu medalha de " + str(tipo_medalhas[i]) + "!")
        else:
            print("Medalha(s) de " + str(tipo_medalhas[i]) + ": " + str(qtd_medalhas[i]))
    print("Maior nota: " + str(max(notas)))
    
qtd_medalhas = numero_medalhas(notas,cortes)
print_medalhas(qtd_medalhas, notas)

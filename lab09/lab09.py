bingo = {}
bingo["B"] = 0
bingo["I"] = 1
bingo["N"] = 2
bingo["G"] = 3
bingo["O"] = 4

"""
cartela = [
    ['12', '24', '43', '49', '72'],
    ['07', '23', '31', '57', '62'],
    ['04', '20', 'XX', '51', '73'],
    ['08', '21', '38', '50', '61'],
    ['05', '27', '40', '54', '63']]
"""

"""
texto_linhas = [
    '12 24 43 49 72',
    '07 23 31 57 62',
    '04 20 XX 51 73',
    '08 21 38 50 61',
    '05 27 40 54 63']
"""

cartela = []
texto_linhas = []

for i in range(5):
    linha_cartela = input()
    texto_linhas.append(linha_cartela)
    dados_linha = linha_cartela.split()
    cartela.append(dados_linha)

def imprime_cartela(texto_linhas):
    cartela_modelo = [
    ["+----------------+"],
    ["| B  I  N  G  O  |"],
    ["+================+"],
    [f"| {texto_linhas[0]} |"],
    [f"| {texto_linhas[1]} |"],
    [f"| {texto_linhas[2]} |"],
    [f"| {texto_linhas[3]} |"],
    [f"| {texto_linhas[4]} |"],
    ["+----------------+"]]

    for i in range(9):
        print(', '.join(cartela_modelo[i]))

def bateu(contador, cont_dprinc, cont_dsec):
    if contador[1] == 5 or contador[2] == 5 or \
       contador[3] == 4 or contador[4] == 5 or contador[5] == 5 or \
       contador["B"] == 5 or contador["I"] == 5 or \
       contador["G"] == 5 or contador["O"] == 5 or \
       contador["N"] == 4 or cont_dprinc == 4 or cont_dsec == 4:
        return True
    else:
        return False

contador = {}
contador["B"] = 0
contador["I"] = 0
contador["N"] = 0
contador["G"] = 0
contador["O"] = 0

contador[1] = 0
contador[2] = 0
contador[3] = 0
contador[4] = 0
contador[5] = 0

cont_dprinc = 0
cont_dsec = 0

texto_sorteados = []
dados_sorteados = []
numeros_sortedos = []

imprime_cartela(texto_linhas)

n = int(input())

for i in range(n):
    sorteado = input()
    texto_sorteados.append(sorteado)
    dados_sorteados = sorteado.split("-")
    numeros_sortedos.append(dados_sorteados)
    letra = dados_sorteados[0]
    numero = dados_sorteados[1]
    esta = False
    print(sorteado)

    if numero in cartela[0]:
        contador[1] += 1
        posicao = 0
        esta = True

    if numero in cartela[1]:
        contador[2] += 1
        posicao = 1
        esta = True

    if numero in cartela[2]:
        contador[3] += 1
        posicao = 2
        esta = True

    if numero in cartela[3]:
        contador[4] += 1
        posicao = 3
        esta = True

    if numero in cartela[4]:
        contador[5] += 1
        posicao = 4
        esta = True

    if numero == cartela[0][0]:
        cont_dprinc += 1

    if numero == cartela[1][1]:
        cont_dprinc += 1

    if numero == cartela[2][2]:
        cont_dprinc += 1

    if numero == cartela[3][3]:
        cont_dprinc += 1

    if numero == cartela[4][4]:
        cont_dprinc += 1

    if numero == cartela[0][4]:
        cont_dsec += 1

    if numero == cartela[1][3]:
        cont_dsec += 1

    if numero == cartela[3][1]:
        cont_dsec += 1

    if numero == cartela[4][0]:
        cont_dsec += 1

    if numero in (row[bingo[letra]] for row in cartela):
        contador[letra] += 1

    if esta:
        cartela[posicao][bingo[letra]] = 'XX'
        x = list(texto_linhas[posicao])
        x[(bingo[letra]*3)] = 'X'
        x[(bingo[letra]*3)+1] = 'X'
        texto_linhas[posicao] = "".join(x)

        imprime_cartela(texto_linhas)

    if bateu(contador, cont_dprinc, cont_dsec):
        print("BINGO!")
        break

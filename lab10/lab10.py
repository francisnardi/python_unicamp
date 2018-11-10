n = int(input())

cartelas = [[['' for _ in range(5)] for _ in range(5)] for _ in range(n)]

for i in range(n):
    for j in range(5):
        linha_cartela = (input()).split()
        for k in range(5):
            cartelas[i][j][k] = linha_cartela[k]

#cartelas = [[['11', '25', '33', '49', '69'],
#  ['08', '23', '44', '55', '67'],
#  ['01', '20', 'XX', '50', '64'],
#  ['02', '17', '35', '57', '66'],
#  ['09', '18', '39', '60', '68']],
# [['11', '23', '33', '54', '72'],
#  ['09', '26', '41', '51', '75'],
#  ['10', '21', 'XX', '59', '71'],
#  ['13', '22', '38', '52', '66'],
#  ['01', '19', '44', '46', '61']]]

texto = [[['' for _ in range(1)] for _ in range(5)] for _ in range(n)]
texto_linhas = [['' for _ in range(n)] for _ in range(5)]

def refaca_cartela(cartelas):
    for a in range(n):
        s = ""
        for b in range(5):
            t = ""
            for c in range(5):
                t += str(cartelas[a][b][c] + " ")
            texto[a][b] = t[:-1]
    for e in range(5):
        for d in range(n):
            r = ""
            for f in range(5):
                r += cartelas[d][e][f] + " "
            texto_linhas[e][d] = r[:-1]
    return

def imprime_cartela(texto_linhas, n):
    j = n * "+----------------+ "
    k = n * "| B  I  N  G  O  | "
    l = n * "+================+ "
    m = n * "+----------------+ "

    o = p = q = w = y = ""

    for g in range(n):
        o += f"| {texto_linhas[0][g]} | "
        p += f"| {texto_linhas[1][g]} | "
        q += f"| {texto_linhas[2][g]} | "
        w += f"| {texto_linhas[3][g]} | "
        y += f"| {texto_linhas[4][g]} | "

    j = j[:-1]
    k = k[:-1]
    l = l[:-1]
    m = m[:-1]
    o = o[:-1]
    p = p[:-1]
    q = q[:-1]
    w = w[:-1]
    y = y[:-1]

    cartela_impressao = [[j],
                         [k],
                         [l],
                         [o],
                         [p],
                         [q],
                         [w],
                         [y],
                         [m]]

    for h in range(9):
        print(', '.join(cartela_impressao[h]))

bingo = {}
bingo["B"] = 0
bingo["I"] = 1
bingo["N"] = 2
bingo["G"] = 3
bingo["O"] = 4

def bateu(contador, cont_dprinc, cont_dsec):
    if 5 in contador.values() or \
       5 in cont_dprinc.values() or \
       5 in cont_dsec.values():
        return True
    else:
        return False

sorteio = int(input())

contador = {}
cont_dprinc = {}
cont_dsec = {}

for z in range(n):
    contador["B", z] = 0
    contador["I", z] = 0
    contador["N", z] = 1
    contador["G", z] = 0
    contador["O", z] = 0

    contador[1, z] = 0
    contador[2, z] = 0
    contador[3, z] = 1
    contador[4, z] = 0
    contador[5, z] = 0

    cont_dprinc[z] = 1
    cont_dsec[z] = 1

texto_sorteados = []
dados_sorteados = []
numeros_sortedos = []

cont = 0
esta = False
refaca_cartela(cartelas)
imprime_cartela(texto_linhas, n)

for i in range(sorteio):
    sorteado = input()
    texto_sorteados.append(sorteado)
    dados_sorteados = sorteado.split("-")
    numeros_sortedos.append(dados_sorteados)
    letra = dados_sorteados[0]
    numero = dados_sorteados[1]
    print(sorteado)

    for j in range(n):

        if numero in cartelas[j][0]:
            contador[(1,j)] += 1
            posicao = 0
            esta = True

        if numero in cartelas[j][1]:
            contador[(2,j)] += 1
            posicao = 1
            esta = True

        if numero in cartelas[j][2]:
            contador[(3,j)] += 1
            posicao = 2
            esta = True

        if numero in cartelas[j][3]:
            contador[(4,j)] += 1
            posicao = 3
            esta = True

        if numero in cartelas[j][4]:
            contador[(5,j)] += 1
            posicao = 4
            esta = True

        if numero == cartelas[j][0][0]:
            cont_dprinc[j] += 1

        if numero == cartelas[j][1][1]:
            cont_dprinc[j] += 1

        if numero == cartelas[j][3][3]:
            cont_dprinc[j] += 1

        if numero == cartelas[j][4][4]:
            cont_dprinc[j] += 1

        if numero == cartelas[j][0][4]:
            cont_dsec[j] += 1

        if numero == cartelas[j][1][3]:
            cont_dsec[j] += 1

        if numero == cartelas[j][3][1]:
            cont_dsec[j] += 1

        if numero == cartelas[j][4][0]:
            cont_dsec[j] += 1

        if numero in (row[bingo[letra]] for row in cartelas[j]):
            contador[(letra, j)] += 1

        if esta:
            cartelas[j][posicao][bingo[letra]] = 'XX'
            refaca_cartela(cartelas)
            cont += 1
            esta = False

    if cont >= 1:
        imprime_cartela(texto_linhas, n)
        cont = 0

    if bateu(contador, cont_dprinc, cont_dsec):
        print("BINGO!")
        break

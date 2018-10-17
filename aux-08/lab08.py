def imprime_cena():
    x = ""
    z = ""
    print(cenas_forca[n_tentativas_incorretas])
    print("Palavra:", end='')
    for j in range(len(lista_palavras[n])):
        x = x + " " + campos[j] + " "
    x=x[:-1]
    print(x, end="")
    if tentativa_incorreta == True:
        print("\nTentativa(s) incorreta(s): ", end='')
        for i in range(len(letras_incorretas)):
            z = z + letras_incorretas[i] + " "
            if letras_incorretas[i] not in letras_incorretas_repetidas:
                letras_incorretas_repetidas.append(letras_incorretas[i])
        z=z[:-1]
        print(z, end="")
    return

def proxima_letra(palavra_escolhida):
    print("\nProxima letra: ", end="")
    proxima = input()
    encontre = re.search(proxima, palavra_escolhida)
    if encontre:
        if proxima not in campos:
            letras_corretas.append(proxima)
            for match in re.finditer(proxima, palavra_escolhida):
                campos[match.start()] = proxima
            print()
            imprime_cena()
        elif proxima in campos:
            print("Voce jah escolheu esta letra.")
            print()
            imprime_cena()
    elif not encontre:
        if proxima not in letras_incorretas:
            letras_incorretas.append(proxima)
            global tentativa_incorreta
            tentativa_incorreta = True
            global n_tentativas_incorretas
            n_tentativas_incorretas += 1
            print()
            imprime_cena()
        else:
            print("Voce jah escolheu esta letra.")
            print()
            imprime_cena()
    return

from forca import lista_palavras, cenas_forca
import re

letras_corretas = []
letras_incorretas = []
letras_incorretas_repetidas = []
incorreta_repetida = False
tentativa_incorreta = False
n_tentativas_incorretas = 0

#print("Escolha um numero entre 0 e 49: ", end='')
n = int(input("Escolha um numero entre 0 e 49: "))
if n < 0 or n > 49:
    print("Numero invalido.")
else:
    print()
    palavra_escolhida = lista_palavras[n]
    campos = ["_" for i in range(len(lista_palavras[n]))]
    print(cenas_forca[0])
    print("Palavra:", end='')
    y = ""
    for j in range(len(lista_palavras[n])):
        y = y + " " + campos[j] + " "
    y=y[:-1]
    print(y, end="")
    while "_" in campos:
        if len(letras_incorretas) == 6:
            print("\nPalavra oculta:", lista_palavras[n])
            break
        proxima_letra(palavra_escolhida)
    if "_" not in campos:
        print("\nPalavra encontrada!")


# coding: utf-8

# In[4]:


tipo_do_objeto = input()
caractere = input()
tipo_ok = True                     # verifica se é um dos tipos esperados (Q,L,C,R,P)
dimensao_ok = True                 # verifica se a dimensão é pelo menos 3
lados_diferentes = True            # verifica se possui lado (Q,L,C) ou lados (R,P)



if tipo_do_objeto == "R" or tipo_do_objeto == "P":
    medida_da_largura = int(input())
    medida_da_altura = int(input())
    if medida_da_largura < 3 or medida_da_altura < 3:
        dimensao_ok = False
        print("Dimensao incorreta.")
elif tipo_do_objeto == "Q" or tipo_do_objeto == "L" or tipo_do_objeto == "C":
    medida_do_lado = int(input())
    lados_diferentes = False       # objeto pode ter lados iguais
    if medida_do_lado < 3:
        dimensao_ok = False
        print("Dimensao incorreta.")
else:
    tipo_ok = False
    print("Objeto incorreto.")



def print_quadrado(caract, lado):
    internos = (lado-2) * " "
    print(lado * caract)
    for i in range(1, lado-1):
        print(caract, caract, sep = internos)
    print(lado * caract)
    
def print_retangulo(caract, largura, altura):
    internos = (largura-2) * " "
    print(largura * caract)
    for i in range(1, altura-1):
        print(caract, caract, sep = internos)
    print(largura * caract)
    
def print_paralelogramo(caract, largura, altura):
    internos = (largura-2) * " "
    print(largura * caract)
    for i in range(1, altura-1):
        print(i * " " + caract, caract, sep = internos)
    print((altura-1) * " " + largura * caract)

def print_losango(caract, lado):
    referencia = []
    print((lado-1) * " " + caract)
    for i in range(1, (2*lado)-2):
        if i < lado:
            print((lado-i-1) * " " + caract, caract, sep = ((2*i-1) * " "))
            referencia.append(2*i-1)
        else:
            if i == lado:
                j = len(referencia) - 2
            print((i-lado+1) * " " + caract, caract, sep = (referencia[j] * " "))
            j = j - 1
    print((lado-1) * " " + caract)
#   print(referencia)
#   print(len(referencia))

def print_cruz(caract, lado):
    vazio = (lado * " ")
    cheio = (lado * caract)
    internos = (lado-2) * " "
    int_int = caract + internos + caract
    print(vazio, cheio, sep='')
    for i in range(1, lado-1):
        print(lado * " " + caract, caract, sep = internos)
    print(cheio, cheio, cheio, sep='')
    for i in range(1, lado-1):
        print(int_int, int_int, int_int, sep="")
    print(cheio, cheio, cheio, sep='')
    for i in range(1, lado-1):
        print(lado * " " + caract, caract, sep = internos)
    print(vazio, cheio, sep='')


    
if tipo_ok and dimensao_ok:
    if lados_diferentes:
        if tipo_do_objeto == "R":
            print_retangulo(caractere, medida_da_largura, medida_da_altura)
        elif tipo_do_objeto == "P":
            print_paralelogramo(caractere, medida_da_largura, medida_da_altura)
    else:
        if tipo_do_objeto == "Q":
            print_quadrado(caractere, medida_do_lado)
        elif tipo_do_objeto == "L":
            print_losango(caractere, medida_do_lado)
        elif tipo_do_objeto == "C":
            print_cruz(caractere, medida_do_lado)


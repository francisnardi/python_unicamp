import sys
def lista_ordenada(data):
  ordenado = data.copy()
  ordenado.sort()
  for x, y in zip(data, ordenado):
    if x != y:
      return False
  return True

x = int(input())
elements = [int(x) for x in input().split()]
n = len(elements)
l = 0
r = n
print("Elemento procurado: " + str(x).zfill(3))
print ("+"+("-----+"*n))
for i in range(n):
    print('| '+ str(elements[i]).zfill(3), end = ' ')
print("|")
print ("+"+("-----+"*n))

if not lista_ordenada(elements):
  print("Vetor nao estah ordenado")
  sys.exit()

found = False
while r - l >= 1:
    meio = (r + l - 1)//2
    sup_sub = ""
    meio_str = ""
    for i in range(n):
        if i >= l and i < r:
            if i == meio:
                sup_sub += "+====="
                meio_str += "||"+str(elements[i]).zfill(3) + "|"
            else:
                sup_sub += "+-----"
                meio_str += "| "+str(elements[i]).zfill(3) + " "
        elif i < l:
            sup_sub += "      "
            meio_str += "      "
        if i == r - 1:
          sup_sub += "+"
          meio_str += "|"
    if sup_sub[-1] == ' ':
        sup_sub = sup_sub[:-1]
        meio_str = meio_str[:-1]
    print(sup_sub)
    print(meio_str)
    print(sup_sub)
    if elements[meio] > x:
        r = meio
    elif elements[meio] < x:
        l = meio + 1
    else:
        found = True
        break
if found:
  print("O elemento estah na posicao", meio)
else:
  print("O elemento nao foi encontrado")

dic = {}                 # times
pt = {}                  # número de pontos
vit = {}                 # número de vitórias
dic_gpro = {}            # gols pró
dic_gsofrido = {}        # gols sofridos
dic_saldo_de_gols = {}   # saldo de gols

n = int(input())

def add_time_dic(time):
    dic[time] = 0                     
    dic_gpro[time] = 0              # gols pró zerados
    dic_gsofrido[time] = 0          # gols sofridos zerados
    dic_saldo_de_gols[time] = 0     # saldo de gols zerado
    pt[time] = 0                    # número de pontos zerado
    vit[time] = 0                   # número de vitórias zerado

def comp_gols_part(mandante, visitante, gols_mandante, gols_visitante):   
    dic_gpro[mandante] += int(gols_mandante)
    dic_gsofrido[mandante] += int(gols_visitante)
    dic_saldo_de_gols[mandante] += int(gols_mandante) - int(gols_visitante)
    dic_gpro[visitante] += int(gols_visitante)
    dic_gsofrido[visitante] += int(gols_mandante)
    dic_saldo_de_gols[visitante] += int(gols_visitante) - int(gols_mandante)

def comp_pt_part(mandante, visitante, gols_mandante, gols_visitante):  
    if int(gols_mandante) > int(gols_visitante):
        pt[mandante] += 3
        vit[mandante] += 1
    elif int(gols_visitante) > int(gols_mandante):
        pt[visitante] += 3
        vit[visitante] += 1
    else:
        pt[mandante] += 1
        pt[visitante] += 1

for i in range(n**2-n):
    resultados = input()
    dados_ptd = resultados.split()
    
    mandante = dados_ptd[0]
    gols_mandante = dados_ptd[1]
    visitante = dados_ptd[3]
    gols_visitante = dados_ptd[4]
    
    if mandante not in dic:
        add_time_dic(mandante)

    if visitante not in dic:
        add_time_dic(visitante)
        
    comp_gols_part(mandante, visitante, gols_mandante, gols_visitante)
    comp_pt_part(mandante, visitante, gols_mandante, gols_visitante)

for t in sorted(pt):
    print(t, pt[t], vit[t], dic_saldo_de_gols[t], dic_gpro[t])

def calc_vencedor(pt, vit, dic_saldo_de_gols, dic_gpro):
    cont_pt = 0
    cont_vit = 0
    cont_saldo_de_gols = 0
    cont_gpro = 0

    maior_pt_chave = max(pt, key=pt.get)
    maior_vit_chave = max(vit, key=vit.get)
    maior_saldo_de_gchave = max(dic_saldo_de_gols, key=dic_saldo_de_gols.get)
    maior_gpro_chave = max(dic_gpro, key=dic_gpro.get)

    maior_pt = pt[maior_pt_chave]
    maior_vit = vit[maior_vit_chave]
    maior_saldo_de_gols = dic_saldo_de_gols[maior_saldo_de_gchave]
    maior_gpro = dic_gpro[maior_gpro_chave]

    for t in sorted(pt):
        if pt[t] == maior_pt:
            cont_pt += 1
        if vit[t] == maior_vit:
            cont_vit += 1
        if dic_saldo_de_gols[t] == maior_saldo_de_gols:
            cont_saldo_de_gols += 1
        if dic_gpro[t] == maior_gpro:
            cont_gpro += 1

    if (cont_pt == 1):
        print("Vencedor:", maior_pt_chave)
    elif (cont_vit == 1):
        print("Vencedor:", maior_vit_chave)
    elif (cont_saldo_de_gols == 1):
        print("Vencedor:", maior_saldo_de_gchave)
    elif (cont_gpro == 1):
        print("Vencedor:", maior_gpro_chave)

calc_vencedor(pt, vit, dic_saldo_de_gols, dic_gpro)


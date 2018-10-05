#!/usr/bin/env python
# coding: utf-8

# # Tarefa de laboratório 06
# ### Campeonato de futebol

# * Em um campeonato de futebol, todos os times inscritos se enfrentam duas vezes: uma em seu estádio e outra no estádio adversário. O principal elemento para classificação é a pontuação acumulada: cada time recebe três pontos por vitória, um ponto por empate e zero ponto por derrota. 
# 
# * Em caso de empate, o desempate é feito por **número de vitórias**, **saldo de gols** (diferença entre o número de gols pró marcados e os gols sofridos por cada time) e **número de gols pró**. Caso os times permaneçam empatados em todos estes itens, ocupariam a mesma posição no campeonato. Nesta tarefa, no entanto, todos os testes levarão a um único vencedor.

# ### Inicializando os diferentes dicionários:

# In[1]:


dic = {}                 # times
pt = {}                  # número de pontos
vit = {}                 # número de vitórias
dic_gpro = {}            # gols pró
dic_gsofrido = {}        # gols sofridos
dic_saldo_de_gols = {}   # saldo de gols


# ### Recebendo o número de times do campeonato:

# In[2]:


n = int(input())


# ### Função que adiciona o time ao dicionário:

# In[3]:


def add_time_dic(time):
    dic[time] = 0                     
    dic_gpro[time] = 0              # gols pró zerados
    dic_gsofrido[time] = 0          # gols sofridos zerados
    dic_saldo_de_gols[time] = 0     # saldo de gols zerado
    pt[time] = 0                    # número de pontos zerado
    vit[time] = 0                   # número de vitórias zerado


# ### Função que computa os gols da partida:

# In[4]:


def comp_gols_part(mandante, visitante, gols_mandante, gols_visitante):
    
    dic_gpro[mandante] += int(gols_mandante)
    dic_gsofrido[mandante] += int(gols_visitante)
    dic_saldo_de_gols[mandante] += int(gols_mandante) - int(gols_visitante)

    dic_gpro[visitante] += int(gols_visitante)
    dic_gsofrido[visitante] += int(gols_mandante)
    dic_saldo_de_gols[visitante] += int(gols_visitante) - int(gols_mandante)


# ### Função que distribui os pontos obtidos pelo time na partida:

# In[5]:


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


# ### Código para calcular a classificação dos times no campeonato:

# In[6]:


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


# ### Código para exibir a classificação dos times no campeonato:

# In[7]:


for t in sorted(pt):
    print(t, pt[t], vit[t], dic_saldo_de_gols[t], dic_gpro[t])


# ### Função para calcular o time vencedor do campeonato:

# In[8]:


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


# ### Código para mostrar o time vencedor do campeonato:

# In[9]:


calc_vencedor(pt, vit, dic_saldo_de_gols, dic_gpro)


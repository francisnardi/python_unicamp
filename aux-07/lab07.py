#!/usr/bin/env python
# coding: utf-8

# # Tarefa de laboratório 07
# ### Avaliação de MC102

# * **Atividades conceituais**: são os questionários que podem ser respondidos via Moodle. A nota atribuída a cada uma destas atividades é uma nota de participação, calculada de maneira proporcional ao número de questões respondidas pelo(a) aluno(a), independentemente do fato de estarem corretas ou não. A média das atividades conceituais **MAC** será dada pela média aritmética simples das notas das atividades.
# 
# * **Tarefas de laboratório**: são os programas desenvolvidos e entregues para correção automática no SuSy. Para compor a média dos laboratórios **ML**, cada tarefa tem um peso indicado no enunciado do laboratório.
# 
# * **Provas teóricas**: são as avaliações aplicadas em sala de aula, sem consulta. Para compor a média de provas **MP** a primeira prova tem peso 2 e a segunda, peso 3.

# ### Função para receber as notas das tarefas de laboratório:

# In[1]:


def tupla_float_int(x) :
    x = x[1:-1]       # remove parênteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla


# ### Função para calcular a média das notas das tarefas de laboratório:

# In[2]:


def calc_med_lab(notas_lab):
    temp_med_lab = []
    temp_pes_lab = []
    for i in range(0, len(notas_lab)):
        temp_med_lab.append(notas_lab[i][0]*notas_lab[i][1])
        temp_pes_lab.append(notas_lab[i][1])
    return sum(temp_med_lab) / sum(temp_pes_lab)


# ### Recebendo e calculando a média das notas das atividades conceituais:

# In[3]:


notas_ac = [float(x) for x in input().split()]
mac = sum(notas_ac) / len(notas_ac)

#print("\n")
#for i in range(0, len(notas_lab)):
#    print("Nota da atividade conceitual", i+1, ":", format(notas_ac[i], ".1f"))  
#print("\n")

print("Media das atividades conceituais:", format(mac, ".1f"))


# ### Recebendo e calculando a média das notas das tarefas de laboratório:

# In[4]:


notas_lab = [tupla_float_int(x) for x in input().split()]
ml = calc_med_lab(notas_lab)

#print("\n")
#for i in range(0, len(notas_lab)):
#    print("Nota do Lab", i, ":", format(notas_lab[i][0], ".1f"))
#    print("Peso do Lab", i, ":", notas_lab[i][1])
#print("\n")

print("Media das tarefas de laboratorio:", format(ml, ".1f"))


# ### Recebendo e calculando a média das notas das provas:

# In[5]:


notas_prova = [float(x) for x in input().split()]
mp = (notas_prova[0]*2 + notas_prova[1]*3)/5

#print("\n")
#for i in range(0, len(notas_prova)):
#    print("Nota da prova", i+1, ":", format(notas_prova[i], ".1f"))  
#print("\n")

print("Media das provas:", format(mp, ".1f"))


# ### Calculando a média global das notas:

# In[16]:


media_global = 0.6 * mp + 0.3 * ml + 0.1 * mac
#print(format(media_global, ".1f"))


# ### Recebendo a frequência do aluno:

# In[17]:


frequencia = float(input())


# ### Função para calcular aprovação:

# In[20]:


def calc_aprov(frequencia, media_global, mac, ml, mp):
    if frequencia < 75.0:
        print("Reprovado(a) por frequencia.")
        print("Media final:", format(min(mp, ml), ".1f"))
    elif frequencia >= 75.0:
        if mp >= 5.0 and ml >= 5.0:
            print("Aprovado(a) por nota e frequencia.")
            print("Media final:", format(max(5, media_global), ".1f"))
        elif mp < 2.5 or ml < 2.5:
            print("Reprovado(a) por nota.")
            print("Media final:", format(min(mp, ml), ".1f"))
        else:
            exame = float(input())
            mfinal = ((min(mp, ml)+exame)/2)
            if mfinal < 5.0:
                print("Nota no exame:", format(exame, ".1f"))
                print("Reprovado(a) por nota.")
                print("Media final:", format(mfinal, ".1f"))
            else:
                print("Nota no exame:", format(exame, ".1f"))
                print("Aprovado(a) por nota e frequencia.")
                print("Media final:", format(mfinal, ".1f"))


# ### Código para calcular aprovação:

# In[21]:


calc_aprov(frequencia, media_global, mac, ml, mp)


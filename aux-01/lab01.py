
# coding: utf-8

# In[5]:


x = int(input())

currency = [10000,5000,2000,1000,500,200,100,50,25,10,5]
qtd = []

for item in currency:
    curr_num = x // item
    qtd.append(curr_num)
    x = x % item

print( qtd[0],"nota(s) de R$ 100,00.")
print( qtd[1],"nota(s) de R$ 50,00.")
print( qtd[2],"nota(s) de R$ 20,00.")
print( qtd[3],"nota(s) de R$ 10,00.")
print( qtd[4],"nota(s) de R$ 5,00.")
print( qtd[5],"nota(s) de R$ 2,00.")
print( qtd[6],"moeda(s) de R$ 1,00.")
print( qtd[7],"moeda(s) de R$ 0,50.")
print( qtd[8],"moeda(s) de R$ 0,25.")
print( qtd[9],"moeda(s) de R$ 0,10.")
print(qtd[10],"moeda(s) de R$ 0,05.")


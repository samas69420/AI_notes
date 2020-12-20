"""
from SamasNeuralNetworkLibV2 import *
l=single_round([0.2,0.1,0.5,0.2], 0.5)
print(l)
"""
import random

class OBJ:
    def __init__(self):
        self.att=random.randint(0,100)

l=[]
for i in range(10):
    l.append(OBJ())


def ordina_dec(l): #descrescente
        for i,el in enumerate(l):
            Max = i
            for j in range(i,len(l)):
                if l[j].att>l[Max].att: Max=j
            t=l[i]
            l[i]=l[Max]
            l[Max]=t
        return l


def ordina_dec_par(l,parametro):#=lambda o: l[i].nome_parametro):  # descrescente #?????
    for i, el in enumerate(l):
        par = lambda : parametro
        Max = i
        for j in range(i, len(l)):
            if par(j) > par(Max): Max = j
        t = l[i]
        l[i] = l[Max]
        l[Max] = t
    return l


for element in l:
    print(element.att)
print("")
#l=ordina_dec_par(l,l[i].att)
l.sort(key=lambda x: x.att, reverse=True)
for element in l:
    print(element.att)


"""
for i,o in enumerate(l):
    f=lambda o: l[i].att
    print(f(i))
"""

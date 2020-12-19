# IN QUESTO BLOCCO CI SONO LE DEFINIZIONI DI:
# - differenza tra liste (come se fossero vettori)
# - trasposta mat
# - trasposta mat + conversione lista in metrice riga
# - inizializzazione mat a 0
# - inizializzazione mat a random
# - moltiplicazione matriciale
# - moltiplicazione matriciale + conversione lista in matrice riga
# - moltiplicazione tra liste membro a membro
# - da lista a riga
# - da colonna (elem i-esimo =c[i][0]) a riga (elem i-esimo = r[i])
# - da riga (elem i-esimo = r[i]) a colonna (elem i-esimo =c[i][0])
# - da riga o colonna a lista
# - input function per il training della NN
# - funzione multipla (prende una funzione e la applica a una lista )
# - funzione multipla su colonna
# - inversione di una lista (il primo elemento diventa il primo e via dicendo)
# - sigmoide(x)
# - derivata della sigmoide in funzione dell'input della sigmoide
# - derivata della sigmoide in funzione della sigmoide stessa
# - input function v3 (come la input faction ma filtrata per dati eterogenei)

import random
import math

########################### FUNZIONI INDIPENDENTI ##############################


def diff(l1,l2): # da l1=[a1,b1,c1] e l2=[a2,b2,c2] -> l3=[a1-a2,b1-b2,c1-c2]
  return [element-l2[i] for i,element in enumerate(l1)]


def init_zero(n,m): #inizializza a 0 una matrice n(num rig) x m(num col)
  M=[]
  for i in range(0,n):
    r=[]
    for j in range(0, m):
      r.append(0)
    M.append(r)
  return M


def init_random(n,m,ran): #inizializza a caso una matrice n(num rig) x m(num col)
  M=[]
  for i in range(0,n):
    r=[]
    for j in range(0, m):
      r.append(random.uniform(ran[0],ran[1]))
    M.append(r)
  return M


def sigmoide(x):
  return (1/(1+math.exp(-x)))


def sigmod_prime_x(x):
  s=sigmoide(x)
  return (s*(1-s))


def sigmoid_prime(s):
  return (s*(1-s))


def molt_mat(A,B): # A: n x m    B: m x p  ->  C:n x p
  n=len(A)
  p=len(B[0])
  C=init_zero(n,p)
  for i in range(0, n):
    for j in range(0, p):
      c=0
      for k in range(0, len(A[0])):
        c+=A[i][k]*B[k][j]
      C[i][j]=c
  return C


def list_to_row(x):
  r=[]
  r.append(x)
  x=r
  return r


def to_list(x): # da [[a,b,c]] oppure [[a],[b],[c]] -> [a,b,c]
  lista=[]
  if len(x[0]) == 1: #ho una colonna
    for element in x:
      lista.append(element[0])
    return lista
  if len(x[0]) > 1: # ho una riga
    for element in x[0]:
      lista.append(element)
    return lista


def mmm(l1,l2): # l1: [a1,b1,c1]  l2: [a2,b2,c2]  -> l3: [a1*a2,b1*b2,c1*c2]
  l=[]
  for i in enumerate(l1):
    l.append(l1[i[0]]*l2[i[0]])
  return l


def func_tupla(v, func): # da [v1,v2,...] -> [func(v1),func(v2),...]
  return [func(element) for element in v]


def func_col(c, func): # da [[v1],[v2],...] -> [[func(v1)],[func(v2)],...]
  return [[func(element[0])] for element in c]


def inverti(l): # da [1,2,3,4,5] -> [5,4,3,2,1]
  li=[]
  for i in range(len(l)-1,-1,-1):
    li.append(l[i])
  return li


def input_function():   # questa genera solo esempi del tipo: [[0.2,0.21,0.34,0.23,0.01,0.1],[1,0]]
  def findmax(arr):
    el=arr[0]
    index=0
    posizione=[]
    for element in arr:
      if element>=el:
        el=element
        if index < 3:
          posizione = [1,0]
        elif index >=3:
          posizione = [0,1]
      index=index+1
    return el, posizione
  result=[]
  result0=[]
  result1=[]
  i=0
  while len(result0)<6:
    element=random.randint(1, 99)/100
    #print("element vale: %s" % element)
    if element not in result0:
      result0.append(element)
  result1 = findmax(result0)[1]
  result.append(result0)
  result.append(result1)
  return result


################## FUNZIONI DIPENDENTI (DA QUELLE SOPRA) #######################


def r_to_c(r):   # da [r1,r2,...] a [[r1], [r2], [r3], [r4],...]
  c=init_zero(len(r),1)
  for i,element in enumerate(r):
    c[i][0]=element
  return c


def c_to_r(c):  # da [[c1], [c2], [c3], [c4],...] a [c1, c2, c3, c4,...]
  r=init_zero(1,len(c))
  for i,element in enumerate(c):
    r[0][i]=element[0]
  return r[0]


def mat_molt(A,B): # moltiplicaz matriciale + [a,b,c,...] -> [[a,b,...]]
  if type(A[0]) is int or type(A[0]) is float:
    A=list_to_row(A)
  if type(B[0]) is int or type(B[0]) is float:
    B=list_to_row(B)
  n=len(A)
  p=len(B[0])
  C=init_zero(n,p)
  for i in range(0, n):
    for j in range(0, p):
      c=0
      for k in range(0, len(A[0])):
        c+=A[i][k]*B[k][j]
      C[i][j]=c
  return C


def trasponi(M): # calcola la trasposta di una matrice + conversione lista-riga
  if type(M[0]) is int:
    M=list_to_row(M)
  M_T=[]
  for i in range(len(M[0])):
    r=[]
    for row in M:
      r.append(row[i])
    M_T.append(r)
  return M_T


def check_pesi(pesi,num_check=10, debug=False): # crea 10 nuovi input e controlla che le previsioni della rete siano tutte esatte
  def round_(col):
    lista=to_list(col)
    if lista[0] > lista[1]:
      return [1,0]
    elif lista[0] < lista[1]:
      return [0,1]
  positive=0
  for i in range (0, num_check):
    in_=input_function()
    in_[0]=in_[0]*100
    a=r_to_c(in_[0])
    for weights in pesi:
      a=func_col(mat_molt(weights,a),sigmoide)
    if round_(a) == in_[1]:
      if debug: print("controllo passato")
      positive += 1
    if round_(a) != in_[1]:
      if debug: print("controllo fallito")
      return False
  return True


ultimo=[0,0]
iter=0
def input_function_v3(n, debug=False):  # come la input_function ma filtrata per avere dati eterogenei e il bug della somma fixato
  global ultimo
  global iter
  if iter % n == 0: iter=0
  while True:
    s1=0
    s2=0
    result=input_function()
    if debug: print("ultimo vale: ",ultimo)
    if result[1] != ultimo:
      if debug: print("ok")
      for i,element in enumerate(result[0]):
        if i<3:
          s1+=element
      for i,element in enumerate(result[0]):
        if i>=3:
          s2+=element
      if (((result[1][0]==0 and s1>s2) or (result[1][0]==1 and s2>s1)) and iter<(n/2)):
        if debug: print("s1 e s2 valgono: ", s1," ",s2)
        iter+=1
        ultimo[0]=result[1][0]
        ultimo[1]=result[1][1]
        return result
      if ((result[1][0]==0 and s1<s2) or (result[1][0]==1 and s2<s1)) and iter>=(n/2):
        if debug: print("s1 e s2 valgono: ", s1," ",s2)
        iter+=1
        ultimo[0]=result[1][0]
        ultimo[1]=result[1][1]
        return result
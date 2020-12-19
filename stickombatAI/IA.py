from SamasNeuralNetworkLib import *

#prende due tensori e li fonde prendendo fino all'elemento prima di w da W1 e da w in poi da W2
def fondi(W1,W2,w=[1,0,2]):
    W3=[]
    #riempio W3 fino al punto indicato da w prendendo gli elementi da W1
    for a in range(w[0]):
        W3.append(W1[a])
    W3.append([]) # questa diventa W3[a_]
    for b in range(w[1]):
        W3[w[0]].append(W1[w[0]][b])
    W3[w[0]].append([]) # questa diventa W3[a_]
    for c in range(w[2]):
        W3[w[0]][w[1]].append(W1[w[0]][w[1]][c])
    #W3[w[0]][w[1]].append(W1[w[0]][w[1]][w[2]])
    #riempio W3 dal punto dove sono arrivato fino alla fine con W2
    for c in range(len(W3[w[0]][w[1]]),len(W2[w[0]][w[1]])):
        W3[w[0]][w[1]].append(W2[w[0]][w[1]][c])
    for b in range(len(W3[w[0]]),len(W2[w[0]])):
        W3[w[0]].append(W2[w[0]][b])
    for a in range(len(W3),len(W2)):
        W3.append(W2[a])
    return W3



class DNA:

    # init fa una rete neurale senza bias (crea solo il tensore dei pesi partendo dalla lista dei neur.p.l inculdendo l'input)
    def __init__(self,lista):
        self.W=[]
        for i in range(len(lista)-1):
            self.W.append(init_random(lista[i+1],lista[i],[-1,1]))

    # uso la sigmoide per essere sicuro di avere un fitness compreso tra 0 e 1
    def calcFitness(self,score):
        self.fitness = sigmoide(score)
        print("ho calcolato il fitness e vale ", self.fitness)

    def crossover(self,partner,debug=False):
        l=[]
        l.append(len(trasponi(self.W[0])))
        l=l+[len(element) for element in self.W]
        child=DNA(l)
        a=random.randint(0,len(self.W)-1)
        b=random.randint(0,len(self.W[a])-1)
        c=random.randint(0,len(self.W[a][b])-1)
        midpoint=[a, b, c]
        child.W=fondi(self.W,partner.W,midpoint)
        if debug:
            print("midpoint: ",midpoint)
            print("pesi 1: ", self.W)
            print("pesi 2: ", partner.W)
        return child

    def mutate(self, mutationRate):
        for matrix in self.W:
            for row in matrix:
                for i,element in enumerate(row):
                    x = random.uniform(0, 1)
                    if (x < mutationRate):
                        print("ho mutato blblblbl")
                        row[i]=random.uniform(-1, 1)

    def think(self,input): #forward
        A=[]
        W=self.W
        a = r_to_c(input)
        A.append(a)
        for weights in W:
            z = mat_molt(weights, a)
            a = func_col(z, sigmoide)
            A.append(a)
        return(A[-1])



mutationRate = 0.1

population = []
def setup(totPopu,rete):
    global population
    for i in range(totPopu):
        population.append(DNA(rete))


k = 0
matingPool = []
maxf = 0
def draw():
    global totPopu
    global mutationRate
    global population
    global maxf
    global matingPool
    global k

    # per ogni elemento della popolazione
        # giocare per tempo t

        # calcola il fitness alla fine del tempo

        # trova il fitness più alto

    # riempie la mating pool in modo proporionale al fitness

    # per ogni elemento della popolazione

        # prende i due partner controllando che siano diversi tra loro

        # crossover()

        # mutate()

        # aggiunge il figlio alla popolazione

"""

prova1=DNA([3,3])
prova2=DNA([3,3])
child=prova1.crossover(prova2)
child.mutate(mutationRate)
print("")
print("child: ",child.W)
print(child.think([0,1,0]))
"""
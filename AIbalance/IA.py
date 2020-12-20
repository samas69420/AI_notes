from SamasNeuralNetworkLibV2 import *

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


"""
matingPool = []
maxf = 0
"""

"""

prova1=DNA([3,3])
prova2=DNA([3,3])
child=prova1.crossover(prova2)
child.mutate(mutationRate)
print("")
print("child: ",child.W)
print(child.think([0,1,0]))
"""
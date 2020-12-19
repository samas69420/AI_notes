# è sostanzialmente la traduzione in linguaggio python del codice dal libro the nature of code
# https://github.com/nature-of-code/noc-examples-processing/tree/master/chp09_ga/NOC_9_01_GA_Shakespeare_simplified
# con qualche cambiamento che ho fatto per togliere le cose grafiche inutili e rendere un po' più efficiente la funzione per il fitness

# per indovinare "to be or not to be" ha usato 357 130 296 555 512 349 188 817 1805 1442 iterazioni in 10 tentativi

lettere=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
import random
import math
######################################################################################################################################################

# CLASSE DNA (dove per dna si intende l'istanza di un individuo della popolazione)

class DNA:

    def __init__(self, num):  # costruttore
        self.genes = ""
        for i in range(num):
            self.genes += lettere[random.randint(0, len(lettere) - 1)]

    def calcFitness(self, target):  # calcola il fitness
        score = 0
        for i in range(0, len(self.genes)):
            if (self.genes[i] == target[i]):
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0, len(self.genes))
        for i in range(len(self.genes)):
            # if i>midpoint:child.genes[i]=self.genes[i]
            # else: child.genes[i]=partner.genes[i]
            if i > midpoint:
                child.genes = replace_character(child.genes, self.genes, i)
            else:
                child.genes = replace_character(child.genes, partner.genes, i)
        return child

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            x = random.uniform(0, 1)
            if (x < mutationRate):
                # print("ho mutato blblbl" , x)
                ge = list(self.genes)
                ge[i] = lettere[random.randint(0, len(lettere) - 1)]
                self.genes = "".join(ge)


def replace_character(st1, st2, i):
    # converto le stringhe in liste
    s1 = list(st1)
    s2 = list(st2)
    # faccio lo scambio
    s1[i] = s2[i]
    # riconverto le liste in stringhe
    st1 = "".join(s1)
    st2 = "".join(s2)
    # ritorno la stringa 1 aggiornata
    return st1

######################################################################################################################################################
# FUNZIONI PER LA RIPRODUZIONE E L'EVOLUZIONE

mutationRate = 0.01
totalPopulation = 150

population = []  # array che deve contenere tanti oggetti "DNA"
target = ""

def setup():
    global totalPopulation
    global target
    global population
    target = "mannaggia a cristo mannaggia"
    # target="to be or not to be"

    for i in range(totalPopulation):
        population.append(0)

    for i in range(len(population)):
        element = DNA(len(target))
        population[i] = element

k = 0
matingPool = []  # array che deve contenere i "DNA" per la riproduzione
maxf = 0  # fitness massimo

def draw():
    global totalPopulation
    global mutationRate
    global population
    global trovato
    global maxf
    global matingPool
    global k
    print("miglior genoma -------- fitness")
    while True:

        for i in range(len(population)):
            population[i].calcFitness(target)

        for i in range(len(population)):
            if population[i].fitness > maxf:
                maxf = population[i].fitness
                print(population[i].genes, " ", maxf)
        if maxf == 1: break

        matingPool.clear()
        for i in range(len(population)):
            for j in range(math.ceil(population[i].fitness * 100)):
                matingPool.append(population[i])
        for i in range(len(population)):
            a = random.randint(0, len(matingPool) - 1)
            while True:
                b = random.randint(0, len(matingPool) - 1)
                if b != a: break
            partnerA = matingPool[a]
            partnerB = matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(mutationRate)
            population[i] = child
        # aggiunte mie per il while
        k = k + 1
        if k % 10000 == 0:
            [print(element.genes) for element in population]

######################################################################################################################################################
# MAIN

setup()

draw()

print("iterazioni necessarie: ",k)
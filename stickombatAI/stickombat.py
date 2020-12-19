import pygame
from IA import *
from datetime import datetime

pygame.init()
screen=pygame.display.set_mode((800,600))

#immagini
p1guardia = pygame.image.load("guardians-l.png").convert_alpha()
p1attack = pygame.image.load("attns-l.png").convert_alpha()
p1def = pygame.image.load("defns-l.png").convert_alpha()
p2guardia = pygame.image.load("guardians-r.png").convert_alpha()
p2attack = pygame.image.load("attns-r.png").convert_alpha()
p2def = pygame.image.load("defns-r.png").convert_alpha()

#liste di immagini per l'animazione + index per scorrere la lista
p1surfaces=[p1def, p1guardia, p1attack]
index1=1
previousi1=1
p2surfaces=[p2def, p2guardia, p2attack]
index2=1
previousi2=1

#cose per il punteggio
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
def show_score(x=10,y=10):
    score=font.render("SCORE: "+str(score_value), True, (0,0,0))
    screen.blit(score,(x, y))
def show_gen(x=10,y=50):
    gen=font.render("GENERATION: "+str(generation), True, (0,0,0))
    screen.blit(gen,(x, y))
def show_individual(x=10,y=90):
    ind=font.render("INDIVIDUAL: "+str(individual), True, (0,0,0))
    screen.blit(ind,(x, y))
def show_fitness(x=450,y=10):
    fit=font.render("MAX_FITNESS: "+str(maxf), True, (0,0,0))
    screen.blit(fit,(x, y))
def show_currfitness(x=400,y=50):
    cfit=font.render("CURRENT_FITNESS: "+str(currf), True, (0,0,0))
    screen.blit(cfit,(x, y))

"""
#game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                index1 = 2
            if event.key == pygame.K_LEFT:
                index1 = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                index1 = 1
    n=random.randint(0,150)
    if n in range(0,3): index2 = n
    if index2 == 2 and index1 == 1 and previousi2==1: #vengo colpito
        score_value-=1
        print(score_value)
    if index1 == 2 and index2 == 1 and previousi1!=2: #colpisco
        score_value+=1.5
        print(score_value)
    if index1 == 2 and index2 == 0 and previousi1!=2: #colpisco sulla guardia (penalità per rendere non vantaggioso lo spam di attacco)
        score_value-=1
        print(score_value)
    previousi1 = index1
    previousi2 = index2
    screen.fill((255,255,255))
    show_score()
    screen.blit(p1surfaces[index1],(25,0))
    screen.blit(p2surfaces[index2],(-25,0))
    pygame.display.update()
"""

def round_v(l):
    M=max(l)
    for i,el in enumerate(l):
        if el ==M: l[i]=1
        else: l[i]=0
    return l

totP=15
rete = [3,3]
setup(totP,rete)
#game loop IA
tempo=10
running=True
maxf=0
currf=0
matingPool=[]
mutationRate=0.01
generation=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    individual=0
    for i in range(len(population)):
        t0=datetime.now()
        score_value=0
        while (datetime.now()-t0).seconds < tempo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            n=random.randint(0,150)
            if n in range(0, 3): index2 = n
            if index2 == 0: scelta_avv = [1, 0, 0]
            if index2 == 1: scelta_avv = [0, 1, 0]
            if index2 == 2: scelta_avv = [0, 0, 1]

            scelta = population[i].think(scelta_avv)
            scelta=round_v(scelta)
            #print("scelta: ", scelta)
            if scelta == [1, 0, 0]: index1= 0
            if scelta == [0, 1, 0]: index1 = 1
            if scelta == [0, 0, 1]: index1 = 2

            if index2 == 2 and index1 == 1 and previousi2==1: #vengo colpito
                score_value-=1
                print(score_value)
            if index1 == 2 and index2 == 1 and previousi1!=2: #colpisco
                score_value+=1.5
                print(score_value)
            if index1 == 2 and index2 == 0 and previousi1!=2: #colpisco sulla guardia (penalità per rendere non vantaggioso lo spam di attacco)
                score_value-=1
                print(score_value)
            previousi1 = index1
            previousi2 = index2
            screen.fill((255,255,255))
            show_score()
            show_gen()
            show_individual()
            show_fitness()
            show_currfitness()
            screen.blit(p1surfaces[index1],(25,0))
            screen.blit(p2surfaces[index2],(-25,0))
            pygame.display.update()
        population[i].calcFitness(score_value)
        currf=population[i].fitness
        if population[i].fitness>maxf: maxf=population[i].fitness
        individual+=1
    #aggiorno il max fitness
    """
    for i in range(len(population)):
        if population[i].fitness > maxf:
            maxf = population[i].fitness
            print(population[i].W, " ", maxf)
    """
    #riempio la mating pool
    matingPool.clear()
    for i in range(len(population)):
        for j in range(math.ceil(population[i].fitness * 100)):
            matingPool.append(population[i])
    #evolve
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
    generation+=1

"""
# inizializzazione clean
import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

pygame.display.set_caption("STICKOMBAT")

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.update()
"""

# alcuni bug da risolvere e cose da aggiungere
# - gioco con set di pesi preimpostato
# - salvataggio dei pesi dopo n generazioni
# - cliccare la x non chiude il gioco
from SamasNeuralNetworkLibV2 import *
from SamasNeuralNetworkLibV2 import population

import gym
env = gym.make("CartPole-v1")
observation = env.reset()
score=0

debug=False

totP=150
rete=[4,5,1]
setup(totP,rete)
currf=0
mutationRate = 0.0001
generation=0
gen_fitness=[]

maxf=0
bestW=[]

#test=SamasNeN([4,5,5,1])
#test.W=[[[0.2676934185063464, 0.5350858055045233, -0.8778018238251726, -0.926730128552278], [0.4800301276947325, -0.6358126589271595, -0.038284174013372585, 0.9739023054015195], [-0.47675133427680927, -0.9352956488586581, 0.13768332660499194, 0.4996498280420987], [-0.17609742314318777, -0.5030024601232275, -0.8464339387205044, 0.8343839401480797], [-0.33580691777535043, -0.11230527514902056, -0.34439063163971695, 0.23555041161906343]], [[0.8139143328232321, 0.020170387666521128, 0.2407656416563988, -0.3080037656562573, 0.8052305472677017], [0.3714163105696422, 0.9558828726433164, 0.9127532169553447, -0.4999406351833162, 0.6286846324722024], [0.22442626549009992, 0.8221592541103118, 0.9836861361447851, -0.39673004281773716, 0.11427233276033899], [-0.43769268071727985, -0.2214915312041461, -0.9233246591364754, 0.48831718659468115, -0.769129349644456], [0.9856904159595576, -0.7232879607725162, -0.8805295368269228, 0.1769678060249542, 0.5913534392829523]], [[0.6015537182739883, -0.2002464189012274, 0.11510791049820712, 0.2477207143518103, -0.7654419695313783]]]


#_=0
while True: # game loop
    gen_fitness.clear()
    for i, el in enumerate(population):
        while True:
            env.render()
            #action = env.action_space.sample() # your agent here (this takes random actions)
            out=to_list(population[i].forward(observation))
            #out = to_list(test.forward(observation))
            action = single_round(out,0.5)[0]
            observation, reward, done, info = env.step(action)
            score+=1
            #_+=1
            #if _>=1000:break

            if done:
                observation = env.reset()
                break
            if debug: print(score)

        population[i].calcFitness(score,observation[0])
        gen_fitness.append(population[i].fitness)

        if population[i].fitness > maxf:
            maxf = population[i].fitness
            print("NUOVO MIGLIOR FITNESS: ", maxf)
            bestW = population[i].W
            for element in bestW:
                print(element)
            print(bestW)

        score=0

    # NEUROEVOLUZIONE
    population.sort(key=lambda x: x.fitness, reverse=True)
    """
    # selezione alternativa
    for i in range(1,len(population)):
        partner=population[i]
        child=best.crossover(partner)
        child.mutate(mutationRate)
        new_pop[i]=child
    """
    n_pop=make_new_pop(population,mutationRate)
    if debug: print("n_pop vale: ", n_pop)
    population=n_pop
    generation+=1

    total_fitness=0
    for element in gen_fitness:
        total_fitness+=element
    print("GENERAZIONE NUMERO: ",generation," FITNESS MEDIO: ", total_fitness/totP)

#env.close()

# SCHEMA DELLA NEUROEVOLUZIONE

# while True
    # for element in population
        # while not done
            #loop di gioco
        # calcolo il fitness
    # trovo i due migliori individui
    # fondo i due migliori individui con mutazioni creando una nuova popolazione
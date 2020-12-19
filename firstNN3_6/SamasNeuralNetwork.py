from SamasNeuralNetworkLib import *

# FORWARD CON INPUT FUNCTION

def forward(input):
    global A
    global W
    a = r_to_c(input[0])
    A.append(a)
    for weights in W:
        z = molt_mat(weights, a)
        a = func_col(z, sigmoide)
        A.append(a)


# BACKWARD CON DISCESA

def backward(input, debug=False):
    global D
    global W
    delta = mmm((diff(to_list(A[-1]), input[1])), func_tupla(to_list(A[-1]), sigmoid_prime))
    MAT = mat_molt(A[-2], delta)
    D.append(trasponi(MAT))
    n_layer = len(A)
    index = n_layer - 2
    for i in range(n_layer - 2, 0, -1):
        delta = mmm(func_tupla(to_list(A[-index]), sigmoid_prime), to_list(mat_molt(delta, W[i])))
        MAT = mat_molt(A[-(index + 1)], delta)
        D.append(trasponi(MAT))
        index += 1
    D = inverti(D)
    # arrivato qui ho il gradiente carico quindi posso procedere con la discesa
    learning_rate = 0.1
    for n, w_matrix in enumerate(W):
        for i, row in enumerate(w_matrix):
            for j, weight in enumerate(row):
                w_matrix[i][j] = weight - learning_rate * D[n][i][j]
                if debug: print("ho aggiornato il peso ", i, j, "da:", weight, " a ", w_matrix[i][j])
        if debug: print("")


def train(n, input_f, debug=False):
    global A
    global W
    global D
    for k in range(0, n):
        A.clear()
        D.clear()
        input = input_f(n)
        # input=[[0.1,0.2,0.3,0.4,0.5,0.6],[0,1]]
        forward(input)
        # print("ho finito forward")
        if debug:
            print(k)
            print("")
            print("Weights prima di backward")
            for element in W:
                print(element)
            print("")
        backward(input)
        if debug:
            print("l'input di allenamento è:")
            print(input)
            print("")
            print("Autputs")
            for element in A:
                print(element)
            print("")
            print("Derivate")
            for element in D:
                print(element)
            print("")
            print("Weights aggiornati")
            for element in W:
                print(element)
            print("")
            print("")
            print("")


print("controllo -- allenamenti -- set trovati")

debug = True
num_allen = 10000
set_buoni = 0
allenamenti = 0
while set_buoni == 0:
    W = []
    W.append(init_random(3, 6, [0, 1]))
    W.append(init_random(3, 3, [0, 1]))
    W.append(init_random(2, 3, [0, 1]))
    # arrivato qui ho il tensore dei pesi caricato
    A = []  # qui ci vado a mettere le liste di output per ogni layer (con input)
    D = []  # questo sarà il gradiente
    train(num_allen, input_function_v3)
    check = check_pesi(W)
    if debug: print(check, "----------", allenamenti, "----------", set_buoni)
    if check:
        set_buoni += 1
        print("")
        print("i pesi buoni valgono: ")
        for element in W:
            print(element)
        print("")
        print(W)
    allenamenti += 1
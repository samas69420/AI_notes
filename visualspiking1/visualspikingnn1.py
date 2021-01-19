from tkinter import *
from neuron import neuron
from synapse import synapse
import time
import random

def key(event):
    if event.char =="a": neuron.neurons[0][0].propagate()
    if event.char =="s": neuron.neurons[0][1].propagate()
    if event.char =="d": neuron.neurons[0][2].propagate()
    if event.char =="f": neuron.neurons[0][3].propagate()
def release(event):
    if event.char == "a": canvas.itemconfig(neuron.neurons[0][0].img, fill="")
    if event.char == "s": canvas.itemconfig(neuron.neurons[0][1].img, fill="")
    if event.char == "d": canvas.itemconfig(neuron.neurons[0][2].img, fill="")
    if event.char == "f": canvas.itemconfig(neuron.neurons[0][3].img, fill="")
    canvas.update()


def init():
    # disegna i neuroni e li carica
    for i in range(1,8):
        col=[]
        for j in range(1,5):
              col.append(neuron(canvas,i,j))
        neuron.neurons.append(col)
    # disegna le sinapsi e le carica
    for i in range(len(neuron.neurons)-1):
        el=[] # qui ci metto le sinapsi di tutta la colonna
        for j in range(len(neuron.neurons[0])):
            n1=neuron.neurons[i][j]
            el2=[] #qui ci metto le sinapsi per il singolo neurone
            for k in range(len(neuron.neurons[0])):
                n2=neuron.neurons[i+1][k]
                el2.append(synapse(canvas,n1,n2,random.uniform(-0.8,1.2)))
            el.append(el2)
        synapse.synapses.append(el)

    # metto in primo piano i neuroni
    for i in range(len(neuron.neurons)):
        for j in range(len(neuron.neurons[0])):
            canvas.tag_raise(neuron.neurons[i][j].img)

def evolve():
    for element in synapse.spikes:
        canvas.move(element[0],element[1],element[2]) # element 0 è l'immagine, poi vx e poi vy
    for element in synapse.spikes:
        if canvas.coords(element[0])[0]>element[3][0] and canvas.coords(element[0])[1]>element[3][1]:
            canvas.delete(element[0])
            fire(element[5]) # controlla lo stato del neurone e spara
            synapse.spikes.remove(element)
    canvas.update()

def fire(element):
    if (element.state >= threshold_pos or element.state<=threshold_neg) and element.coords[0]<len(neuron.neurons):
        element.last=time.time()
        element.propagate()
        element.state = 0
    if (element.state >= threshold_pos or element.state <= threshold_neg) and element.coords[0]==len(neuron.neurons):
        # qui faccio una sorta di propagate ma farlocco fasullo fake gimmik lmao
        canvas.itemconfig(element.img, fill="green")
        element.last = time.time()
        element.state = 0


def shutdown():
    for col in neuron.neurons:
        for element in col:
            if time.time()-element.last >= neuron.stayon:
                canvas.itemconfig(element.img, fill="")


def random_input():
    in_col=neuron.neurons[0]
    i = random.randint(0,3)
    in_col[i].propagate()

def customloop(dt):
    global t0
    global t00
    while True:
        if time.time() - t0 >= dt:

            if time.time() - t00 >= 0.1:
                random_input() #accendo un neurone a caso ogni 0.1 sec
                t00=time.time()

            evolve() # propaga gli spikes nella lista
            shutdown() # spegne i neuroni che hanno appena sparato

            t0 = time.time()
        canvas.update()

window = Tk()
window.bind("<Key>", key)
window.bind("<KeyRelease>", release)
window.title('8==D')
WID=800
HE=600
refresh = 0.001 #ogni quanto vengono eseguite le istruzioni nel customloop
canvas = Canvas(window, width=WID, height=HE, bg="black")
canvas.pack()
t0 = time.time() # per il customloop
t00 = time.time() # solo per l'input
threshold_pos=3
threshold_neg=-3
try:
    init()
    customloop(refresh)
    mainloop()
except Exception as e:
    pass
from synapse import synapse
import math
class neuron:

    neurons=[]
    stayon=0.1

    def __init__(self,canvas,x,y):
        self.last=0
        self.coords = x,y
        self.state=0
        self.canvas=canvas
        self.img = self.canvas.create_oval(x*100,y*100,x*100+30,y*100+30,fill="",outline="white")

    def get_neighbors(self):
        coords=self.coords
        neighbors = []
        for i in range(len(neuron.neurons[coords[0]])):
            neighbors.append(neuron.neurons[coords[0]][i])
        return neighbors

    def get_synapses(self):
        i,j=self.coords[0]-1,self.coords[1]-1
        #for element in synapse.synapses[i][j]:  per debug
        #    self.canvas.itemconfig(element.line,width=5)
        return synapse.synapses[i][j]

    def propagate(self):
        # parte logica
        neighbors = self.get_neighbors()
        synapses = self.get_synapses()
        for i,element in enumerate(neighbors):
            element.state=element.state+synapses[i].w
        # parte grafica
        x,y=self.coords
        ncoords=[element.coords for element in neighbors]
        self.canvas.itemconfig(self.img,fill="green")
        for element in ncoords:
            rect=self.canvas.create_rectangle(x*100+11,y*100+11,x*100+19,y*100+19,fill="cyan")
            v=element[0]-x,element[1]-y
            v=3*v[0]/math.sqrt(v[0]**2+v[1]**2),3*v[1]/math.sqrt(v[0]**2+v[1]**2)
            dest=element[0]*100,element[1]*100
            synapse.spikes.append([rect,v[0],v[1],dest])


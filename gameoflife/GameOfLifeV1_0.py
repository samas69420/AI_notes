from tkinter import *
import random
import time

class Cell:
    def __init__(self,canvas,x,y,color,lato=10): #costruttore da 0
        self.canvas = canvas
        self.x=x
        self.y=y
        self.l = lato
        self.image = canvas.create_rectangle(x,y,x+self.l,y+self.l,fill=color)
        self.color=color

    def change_color(self,color):
        #self.image = canvas.create_rectangle(self.x,self.y,self.x+self.l,self.y+self.l,fill=color)
        self.canvas.itemconfig(self.image,fill=color) #canvas.itemconfig(rectangles[y][x], fill=color)
        self.color = color

    def get_neighbors_number(self, debug= False):  #cells[riga][colonna] ; cells[y][x]
        global cells
        x = int(self.x/self.l)
        y = int(self.y/self.l)
        if debug: print("x,y valgono ", x,y)
        n = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if [i,j] != [x,y] and cells[j][i].color == "white":
                    n += 1
        return n


def init():
    global cells
    #faccio la prima riga della cornice
    row = []
    for i in range(int(WID/l)):
        row.append(Cell(canvas,l*i,0,"black",l))
    cells.append(row)

    for j in range(1,int(HE/l)-1):
        row = []
        row.append(Cell(canvas,0,l*j,"black",l)) #cornice
        for i in range(1,int(WID/l)-1):
            n=random.randint(0,100)
            if n>=prob : color= "white"
            else: color = "black"
            row.append(Cell(canvas,l*i,l*j,color,l))
        row.append(Cell(canvas,WID-l,l*j,"black",l)) #cornice
        cells.append(row)

    #faccio l'ultima riga della cornice
    row = []
    for i in range(int(WID/l)):
        row.append(Cell(canvas,l*i,HE-l,"black",l))
    cells.append(row)


def init2(): #per l'oscillatore
    global cells
    #faccio la prima riga della cornice
    row = []
    for i in range(int(WID/l)):
        row.append(Cell(canvas,l*i,0,"black",l))
    cells.append(row)

    for j in range(1,int(HE/l)-1):
        row = []
        row.append(Cell(canvas,0,l*j,"black",l)) #cornice
        for i in range(1,int(WID/l)-1):
            row.append(Cell(canvas,l*i,l*j,"black",l))
        row.append(Cell(canvas,WID-l,l*j,"black",l)) #cornice
        cells.append(row)

    #faccio l'ultima riga della cornice
    row = []
    for i in range(int(WID/l)):
        row.append(Cell(canvas,l*i,HE-l,"black",l))
    cells.append(row)

    #glider
    #cells[10][11].change_color("white")
    #cells[10][12].change_color("white")
    #cells[10][13].change_color("white")
    #cells[9][13].change_color("white")
    #cells[8][12].change_color("white")

    #oscillator
    #cells[10][11].change_color("white")
    #cells[10][12].change_color("white")
    #cells[10][13].change_color("white")

    #cross
    #cells[9][12].change_color("white")
    #cells[11][12].change_color("white")
    #cells[10][11].change_color("white")
    #cells[10][12].change_color("white")
    #cells[10][13].change_color("white")


def evolve(debug=False):
    global cells
    global canvas

    n_cells=[]

    canvas.destroy()
    canvas = Canvas(window, width=WID, height=HE)
    canvas.pack()

    if debug: print("all'inizio le celle 9: 11,12,13 sono: ", cells[9][11].color,cells[9][12].color,cells[9][13].color)
    if debug: print("all'inizio le celle 10: 11,12,13 sono: ", cells[10][11].color,cells[10][12].color,cells[10][13].color)
    if debug: print("all'inizio le celle 11: 11,12,13 sono: ", cells[11][11].color,cells[11][12].color,cells[11][13].color)

    #faccio la prima riga della cornice
    row = []
    for i in range(int(WID/l)):
        row.append(Cell(canvas,l*i,0,"black",l))
    n_cells.append(row)


    for j in range(1,int(HE/l)-1):
        row=[]
        row.append(Cell(canvas,0,l*j,"black",l)) #cornice

        for i in range(1,int(WID/l)-1):
            cell = cells[j][i]
            neig = cell.get_neighbors_number()
            color = cell.color

            if neig <2: color = "black"
            elif neig ==2: color = cell.color
            elif neig == 3: color = "white"
            elif neig > 3: color = "black"

            row.append(Cell(canvas,cell.x,cell.y,color,l))
        row.append(Cell(canvas,WID-l,l*j,"black",l)) #cornice
        n_cells.append(row)

    #faccio l'ultima riga della cornice
    row = []
    for i in range(int(WID/l)):
        row.append(Cell(canvas,l*i,HE-l,"black",l))
    n_cells.append(row)

    if debug: print("dopo in n_cells le celle 9: 11,12,13 sono: ", n_cells[9][11].color,n_cells[9][12].color,n_cells[9][13].color)
    if debug: print("dopo in n_cells le celle 10: 11,12,13 sono", n_cells[10][11].color,n_cells[10][12].color,n_cells[10][13].color)
    if debug: print("dopo in n_cells le celle 11: 11,12,13 sono", n_cells[11][11].color,n_cells[11][12].color,n_cells[11][13].color)
    if debug: time.sleep(100)

    cells = n_cells
    canvas.update()


def customloop():
    global cells
    while True:
        evolve()


window = Tk()
window.title('boh')
WID=800
HE=600
l=20
prob=60
canvas = Canvas(window, width=WID, height=HE)
canvas.pack()
cells = []


init()
customloop()
window.mainloop()
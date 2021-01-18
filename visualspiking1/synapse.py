class synapse:
    synapses=[]
    spikes=[]

    def __init__(self,canvas,pre,post,w):
        self.canvas = canvas
        self.pre = pre
        self.post= post
        self.w = w
        #self.line = self.canvas.create_line(pre.coords[0]*100+15,pre.coords[1]*100+15,post.coords[0]*100+15,post.coords[1]*100+15,fill="gray23")
        if w>0:
            color = "dark green"
        if w<0:
            color = "red4"
        elif w==0:
            color = "gray23"
        self.line = self.canvas.create_line(pre.coords[0]*100+15,pre.coords[1]*100+15,post.coords[0]*100+15,post.coords[1]*100+15,fill=color)

    def set_w(self,w):
        self.w = w
        if w>0:
            color = "green"
        if w<0:
            color = "red"
        elif w==0:
            color = "gray23"
        self.canvas.itemconfig(self.line,fill=color)


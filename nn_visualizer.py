#simple neural net structure visualizer

from nn import Network as Network
from nn import Layer as Layer
import numpy as np
import tkinter as tk


class Visualizer:
    def __init__(self, network, window_size = 500):
        self.nw = network
        self.numlayers = len(network.layers) + 1
        self.max_num_circles =self.nw.getMaxLayerSize()
        self.radius = window_size / (4 * self.max_num_circles)
        self.horiz_offset = (window_size - self.radius*2*self.numlayers)/self.numlayers
        self.coordinates = {}
        self.midy = window_size // 2


        def _create_node(self, x, y, r, **kwargs):
            return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

        tk.Canvas.create_circle = _create_node

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=window_size, height=window_size, borderwidth=0, highlightthickness=0, bg="white")
        self.canvas.grid()

    def createLayer(self, layernum):
        currlayer = self.nw.layers[layernum]
        numcircles = currlayer.getInputDimensions()

        if (numcircles % 2 == 0):
            mid_index = numcircles / 2
            yshift = self.midy - self.radius*(4 * mid_index - 1)
        else:
            mid_index = numcircles // 2 + 1
            yshift = self.midy - self.radius*(2 * mid_index + 1)

        self.coordinates[layernum] = {}
        for i in range(numcircles):
            x = self.radius*(2*layernum + 1) + layernum*self.horiz_offset
            y = self.radius*(4*i + 1) + yshift
            self.coordinates[layernum][i] = (x, y)
            self.canvas.create_circle(x, y, self.radius, outline = "#DDD", width = 4)

    def createFinalLayer(self):
        numcircles = self.nw.final_output_size
        self.coordinates[self.numlayers - 1] = {}

        if (numcircles % 2 == 0):
            mid_index = numcircles / 2
            yshift = self.midy - self.radius*(4 * mid_index - 1)
        else:
            mid_index = numcircles // 2 + 1
            yshift = self.midy - self.radius*(2 * mid_index + 1)

        for i in range(numcircles):
            x = self.radius*(2*(self.numlayers - 1) + 1) + (self.numlayers - 1) * self.horiz_offset
            y = self.radius*(4*i + 1) + yshift
            self.coordinates[self.numlayers - 1][i] = (x, y)
            self.canvas.create_circle(x, y, self.radius, outline = "#DDD", width = 4)

    def show(self):
        self.root.mainloop()

    def createAllLayers(self):
        for i in range(self.numlayers - 1):
            self.createLayer(i)
        self.createFinalLayer()

    def addEdges(self):
        for i in range(self.numlayers - 1):
            currlayer = self.coordinates[i]
            nextlayer = self.coordinates[i+1]
            for n in range(len(currlayer)):
                x0 = currlayer[n][0]
                y0 = currlayer[n][1]
                for n2 in range(len(nextlayer)):
                    x1 = nextlayer[n2][0]
                    y1 = nextlayer[n2][1]
                    if (self.nw.layers[i].getWeight(n, n2) != 0):
                        self.canvas.create_line(x0, y0, x1, y1, fill = '#000000')
                    else:
                        self.canvas.create_line(x0, y0, x1, y1, fill = '#DDD')


    def printCoordinates(self):
        for i in range(len(self.coordinates)):
            print("layer ", i)
            print(self.coordinates[i])


if __name__ == '__main__':
    l0 = Layer(3, 6)
    l0.setWeight(1,3, 0)
    l1 = Layer(6, 3)
    l2 = Layer(3, 2)

    n = Network()
    n.addLayer(l0)
    n.addLayer(l1)
    n.addLayer(l2)

    v = Visualizer(n, window_size = 800)
    v.createAllLayers()
    v.addEdges()
    v.show()
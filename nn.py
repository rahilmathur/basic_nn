#basic neural network implementation

import numpy as np

class Layer:
    #can specify weights with __init__(input, output, weights = )
    def __init__(self, input_dim, output_dim, **optweights):
        self.input_size = input_dim
        self.output_size = output_dim
        if ('weights' in optweights):
            self.weights = optweights['weights']
        else:
            self.weights = np.random.rand(input_dim, output_dim)

    def input(self, input_vector, activation = lambda x: x):
        return [activation(x) for x in np.dot(input_vector, self.weights)]

    def removeConnection(self, input_node, output_node):
        self.setWeight(input_node, output_node, 0)

    def setWeight(self, i, j, weight):
        self.weights[i][j] = weight

    def reinitializeWeights(self):
        self.weights = np.random.rand(input_size, output_size)

    def zeroWeights(self):
        self.weights = np.zeros([input_size, output_size])

    def showWeights(self):
        print(self.weights)

    def getWeight(self, i, j):
        return self.weights[i][j]

    def getInputDimensions(self):
        return self.input_size

    def getOutputDimensions(self):
        return self.output_size


class Network:
    def __init__(self):
        self.layers = []
        self.final_output_size = 0

    def addLayer(self, input_dim, output_dim, **weights):
        if ('weights' in weights):
            self.layers[len(self.layers)] = Layer(input_dim, output_dim, weights['weights'])
        else:
            self.layers[len(self.layers)] = Layer(input_dim, output_dim)
        self.final_output_size = self.layers[len(self.layers)-1].getOutputDimensions()

    def addLayer(self, layer):
        self.layers += [layer]
        self.final_output_size = self.layers[len(self.layers)-1].getOutputDimensions()

    def feedForward(self, input_vector):
        output = input_vector
        for l in self.layers:
            output = l.input(output)
        return(output)

    def showLayers(self):
        for l in self.layers:
            l.showWeights()

    def getMaxLayerSize(self):
        return max(self.final_output_size, max([l.getInputDimensions() for l in self.layers]))


import numpy as np

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        
        # Initialize biases as a list
        self.biases = []
        for y in sizes[1:]:  # for every layer except the input layer
            b = np.random.randn(y, 1)  # column vector of biases
            self.biases.append(b)
        
        # Initialize weights as a list
        self.weights = []
        for x, y in zip(sizes[:-1], sizes[1:]):  # pairs of consecutive layers
            w = np.random.randn(y, x)  # weight matrix with shape (y, x)
            self.weights.append(w)

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))  #1/(1 + e^-z) for every element in z

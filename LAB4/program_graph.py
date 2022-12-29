import numpy as np
from constants import *

class Program_Graph:
    def __init__(self, n=NODES_AMOUNT, min_pow=MIN_POW, max_pow=MAX_POW):
        self.n = n
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.vertices = []

    def create(self):
        for i in range(self.n):
            num_of_edges = np.random.randint(1, self.max_pow + 1)
            all_vertices = np.arange(self.n)
            np.random.shuffle(all_vertices)
            neighbours = all_vertices[:num_of_edges]
            for neighbor in neighbours:
                self.vertices.append([i, neighbor])

    def getVertices(self):
        return self.vertices

    def getNodes(self):
        return self.n

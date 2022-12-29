import matplotlib.pyplot as plt
from representation_graph import *
from program_graph import *


class Algo:
    def __init__(self, graph: Program_Graph):
        self.n = graph.getNodes()
        self.lst = graph.getVertices()

    def getNeighbours(self, vertex):
        neighbour_list = []
        for key, val in self.lst:
            if key == vertex:
                neighbour_list.append(val)
        return neighbour_list

    def isCorrectColoredNeighbours(self, vertex, vertex_colors, current_color):
        neighbours = self.getNeighbours(vertex)
        neighbours_not_in_same_color = [vertex_colors[neighbor] != current_color for neighbor in neighbours]
        if sum(neighbours_not_in_same_color) == len(neighbours_not_in_same_color):
            return True
        return False

    def maxPowerVertex(self):
        elements = [row[0] for row in self.lst]
        max_val = max(set(elements), key=elements.count)
        return max_val

    def try_to_reduce_num_of_colors(self, vertex, vertex_colors, num_colors):
        neighbours = self.getNeighbours(vertex)
        for neighbor in neighbours:
            temp_colors = vertex_colors.copy()
            temp_colors[vertex], temp_colors[neighbor] = temp_colors[neighbor], temp_colors[vertex]
            if self.isCorrectColoredNeighbours(neighbor, temp_colors, temp_colors[neighbor]):
                new_color = RepresentationGraph.getAvailableColor(self.getNeighbours(neighbor), temp_colors, num_colors, vertex_colors[neighbor])
                if new_color != -1:
                    temp_colors[neighbor] = new_color
                    vertex_colors = temp_colors.copy()

        return vertex_colors

    def createGraph(self):
        graph = nx.Graph()
        lst = RepresentationGraph.removeDuplicateEdges(self.lst)
        for row in lst:
            graph.add_edge(row[0], row[1])
        return graph

    def displayGraph(self, vertex_colors):
        print("Number of colors used:", len(set(vertex_colors)))

        print("\n__________________________________________\n")
        graph = self.createGraph()
        RepresentationGraph.drawGraph(graph, vertex_colors)
        plt.show()

    def greedy(self):
        current_color = 0
        vertex_colors = [-1 for _ in range(self.n)]
        while sum([val == -1 for val in vertex_colors]) != 0:
            for vertex in range(self.n):
                if vertex_colors[vertex] == -1:
                    if self.isCorrectColoredNeighbours(vertex, vertex_colors, current_color):
                        vertex_colors[vertex] = current_color
            current_color += 1
        return vertex_colors, current_color

    def bees(self):
        vertex_colors, num_colors = self.greedy()
        print("Before")
        self.displayGraph(vertex_colors)
        vertex = self.maxPowerVertex()
        nxt = [vertex]
        counter = 0
        parent = -1
        randomness = 1
        mutation = randomness
        while len(nxt) < 30:
            vertex = nxt[counter]
            neighbours = self.getNeighbours(vertex)
            for neighbor in neighbours:
                if neighbor != parent:
                    nxt.append(neighbor)
                if mutation == 0:
                    nxt.append(np.random.randint(0, self.n+1))
                    mutation = randomness
            parent = vertex
            counter += 1
            mutation -= 1
        for vertex in nxt:
            vertex_colors = self.try_to_reduce_num_of_colors(vertex, vertex_colors, num_colors)
        print("After")
        self.displayGraph(vertex_colors)

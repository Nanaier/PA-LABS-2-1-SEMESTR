import networkx as nx


class RepresentationGraph:
    def __init__(self):
        self.empty = 0

    @staticmethod
    def drawGraph(graph, vertex_colors):
        layout = nx.spring_layout(graph)
        colors = ['blue', 'yellow', 'red', 'orange', 'black', 'green', 'grey', 'purple', 'pink', 'brown']
        values = [colors[vertex_colors[node]] for node in graph.nodes()]
        nx.draw(graph, layout, with_labels=True, node_color=values, edge_color='black', width=1, alpha=0.8)

    @staticmethod
    def getAvailableColor(neighbours, vertex_colors, num_colors, previous_color):
        available_colors = [color for color in range(num_colors)]
        for neighbor in neighbours:
            color = vertex_colors[neighbor]
            if color in available_colors:
                available_colors.remove(color)
        if previous_color in available_colors:
            available_colors.remove(previous_color)
        if len(available_colors) != 0:
            return available_colors[0]
        return -1

    @staticmethod
    def removeDuplicateEdges(lst):
        without_duplicates = []
        for key, val in lst:
            if key != val:
                if [key, val] and [val, key] not in without_duplicates:
                    without_duplicates.append([key, val])
        return without_duplicates



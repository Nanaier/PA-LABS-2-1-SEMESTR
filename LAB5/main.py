from algo import *
from program_graph import *


def main():
    graph = Program_Graph()
    graph.create()

    algo = Algo(graph)
    algo.bees()


if __name__ == "__main__":
    main()

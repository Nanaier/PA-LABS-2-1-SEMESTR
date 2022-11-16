import sys

class Node:
    def __init__(self, state, depth:int, node):
        self.state = state
        self.depth = depth
        self.parent = node
        self.bytesUsed = 0

    def AddBytesUsed(self, boardSize):
        self.bytesUsed +=sys.getsizeof(int())*(boardSize + 1)

    def getState(self):
        return self.state

    def getDepth(self):
        return self.depth

    def getParent(self):
        return self.parent

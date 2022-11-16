from copy import deepcopy
import time
from Node import Node
from State import State
from queue import PriorityQueue
from PrioritizedItem import PrioritizedItem
from helperFunctions import printBoard
from constants import GBToBytes, ThirtyMinutes

class Algorithms:

    def __init__(self, initial_state, size):

        self.root = Node(initial_state, 0, None)
        self.path = []
        self.boardSize = size
        self.iterAmn = 0
        self.nodesCreatedAmn = 1
        self.nodesSavedAmn = 1
        self.root.AddBytesUsed(self.boardSize)
        self.timerStart = time.time()
        self.deadEnds = 0

    def Expand(self, node):
        currDepth = node.getDepth()
        children = []
        if currDepth == self.boardSize:
            return children
        for col in range(0, self.boardSize):
            newBoard = deepcopy(node.getState())
            newBoard.posititonQueen(currDepth, col)
            children.append(Node(newBoard, currDepth+1, node))
        return children


    def DLS(self, node:Node, lim, currNodesInMemory):

        self.iterAmn+=1
        isCutoff = False
        if node.getState().isReady():
            self.solutions:State = deepcopy(node.getState())
            self.__getStates(node)

            return 0
        if node.getDepth() == lim:
            currNodesInMemory-=1
            return 2

        children = self.Expand(node)

        self.nodesCreatedAmn += len(children)
        currNodesInMemory += len(children)
        if currNodesInMemory > self.nodesSavedAmn:
            self.nodesSavedAmn = currNodesInMemory
        currTime = time.time() - self.timerStart
        if currNodesInMemory * self.root.bytesUsed > GBToBytes or currTime > ThirtyMinutes:
            self.deadEnds+=1
            return 1
        for i in range(0, len(children)):
            result = self.DLS(children[i], lim, currNodesInMemory)
            if result == 2:
                isCutoff = True
            else:
                if result != 1:
                    return result

        currNodesInMemory-=1
        if isCutoff:
            return 2
        else:
            return 1



    def IDS(self):
        for i in range(self.boardSize):
            currNodeSaved = 0
            result = self.DLS(self.root, i, currNodeSaved)
            if result == 0:
                return True
            else:
                if result == 1:
                    return False
        return False

    def A_star(self):
        queue = PriorityQueue(0)
        queue.put(PrioritizedItem(self.root.getState().F1(), self.root))
        while queue.qsize() >0:
            self.iterAmn+=1
            curr = queue.get()
            if curr.item.getState().isReady():
                self.solutions: State = deepcopy(curr.item.getState())
                self.__getStates(curr.item)
                return True
            children = self.Expand(curr.item)
            self.nodesCreatedAmn += len(children)
            currTime = time.time() - self.timerStart
            if queue.qsize() * self.root.bytesUsed > GBToBytes or currTime > ThirtyMinutes:
                self.deadEnds += 1
                return 1
            for i in range(len(children)):
                queue.put(PrioritizedItem(children[i].getState().F1(), children[i]))
            if queue.qsize() > self.nodesSavedAmn:
                self.nodesSavedAmn = queue.qsize()

        return False


    def __getStates(self, node):
        lst = []
        while node.getParent() is not None:
            lst.append(node.getState())
            node = node.getParent()
        print("\n------------Solution start-------------\n")
        for i in range(len(lst)-1, -1, -1):
            printBoard(lst[i])
        print("\n------------Solution end-------------\n")

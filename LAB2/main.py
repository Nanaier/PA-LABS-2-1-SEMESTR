from helperFunctions import getInput, generateBoard, printBoard
import time
from Algorithms import Algorithms

size, chosenAlgo = getInput()
state = generateBoard(size)

print("\n------------Initial state-------------\n")
print(state.board)
printBoard(state)

algo = Algorithms(state, size)
if chosenAlgo == 'i':
    algo.IDS()
    solution = algo.solutions
    currTime = time.time() - algo.timerStart
    print("\n------------The solution-------------\n")
    printBoard(solution)
    print(f"\n Iterations: {algo.iterAmn}\n Nodes Created: {algo.nodesCreatedAmn}\n Nodes Saved: {algo.nodesSavedAmn}\n Amount of Dead-ends: {algo.deadEnds}\n Time Spent: {currTime}\n")


if chosenAlgo == 'a':
    algo.A_star()
    solution = algo.solutions
    currTime = time.time() - algo.timerStart
    print("\n------------The solution-------------\n")
    printBoard(solution)
    print(f"\n Iterations: {algo.iterAmn}\n Nodes Created: {algo.nodesCreatedAmn}\n Nodes Saved: {algo.nodesSavedAmn}\n Amount of Dead-ends: {algo.deadEnds}\n Time Spent: {currTime}\n")


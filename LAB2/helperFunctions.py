from State import State
import random
import string

def getInput():
    n = int(input("Enter the size: "))
    chosenAlgo = input("Enter a for A* or i for IDS: ")
    while chosenAlgo != 'a' and chosenAlgo != 'i':
        chosenAlgo = input("Enter correct letter: ")
    return n, chosenAlgo

def generateBoard(size):
    state = State(size)
    state.board = random.sample(range(0, size), size)

    return state

def printBoard(state):
    alphabet = list(string.ascii_lowercase)
    for k in range(0, state.boardSize+1):
        if k == 0:
            print(' ', end='   ')
        else:
            print(k, end='   ')
    print('')
    for i in range(0, state.boardSize):
        if i < (len(alphabet)-1):
            print(alphabet[i], end='  ')
        else:
            print(alphabet[i%len(alphabet)], end=' ')
        for j in range(0, state.boardSize):
            if state.board[i] == j:
                print('[Q]', end=' ')
            else:
                print('[ ]', end=' ')
        print('')

class State:
    def __init__(self, n):
        self.boardSize = n
        self.board = [0]*self.boardSize

    def getBoard(self):
        return self.board

    def isReady(self):
        for i in range(1, self.boardSize):
            for j in range (i-1, -1, -1):
                if self.board[i] == self.board[j]:
                    return False
                differance = i - j
                if self.board[i] - differance == self.board[j] or self.board[i] + differance == self.board[j]:
                    return False
        return True

    def isByRules(self, row, col):
        for i in range(col-1, -1, -1):
            if row == self.board[i]:
                return False
            differance = col - i
            if row - differance == self.board[i] or row + differance == self.board[i]:
                return False
        return True

    def posititonQueen(self, row, col):
        self.board[row] = col

    def F1(self):
        result = 0
        for i in range(self.boardSize):
            foundOnRow = False
            foundOnMainDiag = False
            foundOnSideDiag = False
            for j in range(i+1, self.boardSize):
                if not foundOnRow and self.board[j] == self.board[i]:
                    foundOnRow = True
                    result+=1
                if not foundOnMainDiag and i - self.board[i] == j - self.board[j]:
                    foundOnMainDiag = True
                    result+=1
                if not foundOnSideDiag and i + self.board[i] == j + self.board[j]:
                    foundOnSideDiag = True
                    result+=1
        return result




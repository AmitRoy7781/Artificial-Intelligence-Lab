#
#   Amit Roy, Roll: JH - 40
#   Constrained Satisfaction Problem using minConflict: n-Queen Problem
#

import random
from datetime import *
import time

intermediateSteps = False
#MAKE THIS FLAG  True to PRINT INTERMEDIATE STEPS

class EIGHT_QUEEN(object):
    
    def __init__(self,totalRow,maxMoves):
        self.r = []
        self.c = []
        self.totalRows = totalRow
        self.maxMoves = maxMoves

    def boardInit(self):

        for curCol in range(self.totalRows):

            min = self.totalRows
            self.c = []
            self.r.append(0)
            for row in range(len(self.r)):

                cnt = self.ConflictChecking(self.r[row], curCol)
                if cnt < min:
                    self.c = []
                    self.c.append(row)
                    min = cnt
                elif cnt == min:
                    self.c.append(row)

            self.r[curCol] = random.choice(self.c)

    def ConflictChecking(self, curRow, curCol):

        cnt = 0
        for rowIndex in range(len(self.r)):
            if rowIndex != curCol:
                if self.r[rowIndex] == curRow or abs(self.r[rowIndex] - curRow) == abs(rowIndex - curCol):
                    cnt += 1

        return cnt


    def queenMove(self, queen_col):
        self.c = []
        min = self.totalRows

        for rowIndex in range(len(self.r)):
            cnt = self.ConflictChecking(rowIndex, queen_col)

            if cnt < min:
                self.c = []
                self.c.append(rowIndex)
                min = cnt
            elif cnt == min:
                self.c.append(rowIndex)
        if self.c:
            self.r[queen_col] = random.choice(self.c)


    


    def BoardSolve(self):
        totalMove = 0
        boardSolved = False
        while boardSolved is False:

            if totalMove>self.maxMoves:
                return -1

            cnt = 0
            self.c = []

            for val in range(len(self.r)):
                cnt += self.ConflictChecking(self.r[val], val)

            if cnt == 0:
                boardSolved = True
                break

            totalMove = totalMove + 1
            newQueen = random.randint(0, len(self.r) - 1)
            self.queenMove(newQueen)
            global intermediateSteps
            if intermediateSteps:
                self.printBoard()


        return totalMove



    def printBoard(self):
        res = ''
        for rowIndex in range(len(self.r)):
            for colIndex in range(len(self.r)):
                if self.r[colIndex] == rowIndex:
                    res += "Q "
                else:
                    res += ". "
            res += "\n"
        print (res)




def SolveNQueen(n):
    startTime = time.time()
    totalQueens = n
    print("For ",n," Queens:")
    print("==================")

    eq = EIGHT_QUEEN(totalQueens, maxMoves)

    random.seed(datetime.now())
    print("Initial Board:")
    print("===============")
    eq.boardInit()
    eq.printBoard()
    totalMoves = eq.BoardSolve()
    print("Final Board:")
    print("=============")
    eq.printBoard()

    elapsedTime = time.time() - startTime
    timeQueens[totalQueens] = elapsedTime
    moveQueens[totalQueens] = totalMoves

    print("Queens: ",n,"\nTotal # of Intermediate Steps : ", totalMoves, "\nTotal Time: ", elapsedTime)
    print()
    print()


if __name__ == "__main__":



    maxMoves = 100000
    timeQueens = {}
    moveQueens = {}


    startTime = time.time()
    totalQueens = 8
    print("For 8 Queens:")
    print("==================")


    eq = EIGHT_QUEEN(totalQueens, maxMoves)

    random.seed(datetime.now()) #to randomize board every time
    print("Initial Board:")
    print("===============")
    eq.boardInit()
    eq.printBoard()
    totalMoves = eq.BoardSolve()
    print("Final Board:")
    print("=============")
    eq.printBoard()

    elapsedTime = time.time() - startTime
    timeQueens[totalQueens] = elapsedTime
    moveQueens[totalQueens] = totalMoves

    if totalMoves == -1:
        print("Queens: 8\n","No Solution")
    else:
        print("Queens: 8\nTotal # of Intermediate Steps : ", totalMoves, "\nTotal Time: ", elapsedTime)
    print()
    print()

    startTime = time.time()
    totalQueens = 12
    print("For 12 Queens:")
    print("==================")

    eq = EIGHT_QUEEN(totalQueens, maxMoves)

    random.seed(datetime.now())
    print("Initial Board:")
    print("===============")
    eq.boardInit()
    eq.printBoard()
    totalMoves = eq.BoardSolve()
    print("Final Board:")
    print("=============")
    eq.printBoard()

    elapsedTime = time.time() - startTime
    timeQueens[totalQueens] = elapsedTime
    moveQueens[totalQueens] = totalMoves

    if totalMoves == -1:
        print("Queens: 12\n","No Solution")
    else:
        print("Queens: 12\nTotal # of Intermediate Steps : ", totalMoves, "\nTotal Time: ", elapsedTime)
    print()
    print()

    startTime = time.time()
    totalQueens = 15
    print("For 15 Queens:")
    print("==================")

    eq = EIGHT_QUEEN(totalQueens, maxMoves)

    random.seed(datetime.now())
    print("Initial Board:")
    print("===============")
    eq.boardInit()
    eq.printBoard()
    totalMoves = eq.BoardSolve()
    print("Final Board:")
    print("=============")
    eq.printBoard()

    elapsedTime = time.time() - startTime
    timeQueens[totalQueens] = elapsedTime
    moveQueens[totalQueens] = totalMoves

    if totalMoves == -1:
        print("Queens: 15\n","No Solution")
    else:
        print("Queens: 15\nTotal # of Intermediate Steps : ", totalMoves, "\nTotal Time: ", elapsedTime)
    print()
    print()

    for totalQueens in range(10,101,10):

        startTime = time.time()
        print("For ",totalQueens," Queens:")
        print("=====================")

        eq = EIGHT_QUEEN(totalQueens, maxMoves)

        random.seed(datetime.now())
        print("Initial Board:")
        print("==============")
        eq.boardInit()
        eq.printBoard()
        totalMoves = eq.BoardSolve()
        print("Final Board:")
        print("=============")
        eq.printBoard()
        elapsedTime = time.time() - startTime
        print("Queens: ", totalQueens, "\nTotal # of Intermediate Steps : ", totalMoves, "\nTotal Time: ", elapsedTime)
        print()
        print()
        timeQueens[totalQueens] = elapsedTime
        moveQueens[totalQueens] = totalMoves

    print("Queens : 8, Time: " ,timeQueens[8], ", Moves: ", moveQueens[8])
    print("Queens : 10, Time: ", timeQueens[10], ", Moves: ", moveQueens[10])
    print("Queens : 12, Time: ", timeQueens[12], ", Moves: ", moveQueens[12])
    print("Queens : 15, Time: ", timeQueens[15], ", Moves: ", moveQueens[15])

    for numberOfQueens in range(20,101,10):
        print("Queens : ", numberOfQueens ,", Time: ", timeQueens[numberOfQueens], ", Moves: ", moveQueens[numberOfQueens])




import numpy as np


# Domain Related Function
def getDomainSize():
    domainSize = 1 + np.random.randint(500, size=1)
    return (domainSize)


def getDomain(domainSize):
    domain = np.random.randint(1000, size=domainSize)
    return list(domain)


def getDomainList(numberOfNodes):
    domainList = []
    for i in range(numberOfNodes):
        domainList.append(getDomain(getDomainSize()))
    return domainList


# constraint related function
def REVISE(Di, Dj, constriant):
    delete = False
    temp = []
    for x in Di:
        if satisfyConstraint(constriant, x, Dj):
            temp.append(x)
        else:
            delete = True
    #print(temp)
    return delete, temp



def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def satisfyConstraint(constraint, x, Dj):
    # x a value of Di
    # the domain Dj

    if constraint == 1:  # y<=x
        for y in Dj:
            if y <= x:
                return True;
        return False

    elif constraint == 2:  # y>=x
        for y in Dj:
            if y >= x:
                return True;
        return False

    elif constraint == 3:  # y=x
        for y in Dj:
            if y == x:
                return True;
        return False

    elif constraint == 4:  # y!=x
        for y in Dj:
            if y != x:
                return True;
        return False

    elif constraint == 5:  # y%x=0
        for y in Dj:
            if x != 0 and y % x == 0:
                return True
        return False

    elif constraint == 6:  # gcd(x,y)=1
        for y in Dj:
            if gcd(x, y) == 1:
                return True;
        return False;
    elif constraint == 7: #x%y==0
        for y in Dj:
            if y != 0 and x % y == 0:
                return True
        return False


# graph_related_function
def generateGraph(size):
    adjMat = np.random.randint(7, size=(size, size));

    for i in range(0, size):
        adjMat[i][i] = 0

        for j in range(i + 1, size):

            if adjMat[i][j]!=0:

                adjMat[i][j] += 1

                if adjMat[i][j] == 1:
                    adjMat[j][i] = 2

                elif adjMat[i][j] == 2:
                    adjMat[j][i] = 1

                elif adjMat[i][j] == 5:
                    adjMat[j][i] = 7

                elif adjMat[i][j] == 7:
                    adjMat[j][i] = 5

                else:
                    adjMat[j][i] = adjMat[i][j]
            else:
                adjMat[j][i] = 0
    return adjMat

def getEdges(adjMat):
    edgeList = []
    for i in range(0,len(adjMat)):
        for j in range(0,len(adjMat)):
            if adjMat[i][j]!=0 and i!=j:
                edgeList.append((i,j))
    return edgeList


def printConstraint(adjMat):
    for i in range(0,len(adjMat)):
        for j in range(0,len(adjMat)):
            if adjMat[i][j] and i!=j:
                print(str(i)+ "---->"+str(j),getConstraintLabel(i,j,adjMat[i][j]))

def getConstraintLabel(x,y,constraint):

    x = 'x' + str(x)
    y = 'x' + str(y)

    if constraint==1: #y<=x
        return y + " <= " + x

    elif constraint==2: #y>=x
        return y + " >= " + x

    elif constraint==3: #y=x
        return y + " = " + x

    elif constraint==4: #y!=x
        return y + " != " +  x

    elif constraint==5: #y%x=0
        return y + " % " + x + " = 0"

    elif constraint==6: #gcd(x,y)=1
        return "gcd(" + x +  "," + y + " ) =  1"
    elif constraint==7: #x%y=0
        return x + " % " + y + " = 0"

    #elif constraint==7:

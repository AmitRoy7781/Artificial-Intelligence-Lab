import numpy as np
import networkx as nx
import random


# Domain Related Function
def getDomainSize():
    domainSize = 1 + np.random.randint(50, size=1)
    return (20)


def getDomain(domainSize):
    domain = np.random.randint(1000, size=domainSize)
    return list(set(domain))
    # return list(domain)

def getDomainList(numberOfNodes):
    domainList = []
    for i in range(numberOfNodes):
        domainList.append(getDomain(getDomainSize()))
    return domainList



def REVISE(Di,Dj,constraint):
    revised = False
    temp = []
    cnt = 0
    for x in Di:
        notSatisfied = True
        for y in Dj:
            cnt+= 1
            if satisfy(x,y,constraint):
                temp.append(x)
                notSatisfied = False
                break
        revised |= notSatisfied
    return revised,temp,cnt

def satisfy(x, y, constraint):
    if constraint == 0:
        return True

    elif constraint == 1:  # y<=x
        return (y <= x)

    elif constraint == 2:  # y>=x
        return (y >= x)

    elif constraint == 3:  # y=x
        return (y == x)

    elif constraint == 4:  # y!=x
        return (y != x)

    elif constraint == 5:  # y%x=0
        return (x != 0 and y % x == 0)

    elif constraint == 6:  # gcd(x,y)=1
        return gcd(x, y) == 1

    elif constraint == 7:  # x%y==0
        return (y != 0 and x % y == 0)

    elif constraint == 8:  # y = ax^2 + bx + c
        return (y == x * x + x + 1)

    elif constraint == 9:  # x = ay^2 + by + c
        return (y * y + y + 1 == x)

    elif constraint == 10:  # y = mx + c
        return (y == 2 * x + 1)

    elif constraint == 11:  # my + c = x
        return (2 * y + 1 == x)



def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

cnt = 0

def satisfyConstraint(constraint, x, Dj):
    # x a value of Di
    # the domain Dj



    if constraint == 0:
        return True

    elif constraint == 1:  # y<=x
        for y in Dj:
            if y <= x:
                return True
        return False

    elif constraint == 2:  # y>=x
        for y in Dj:
            if y >= x:
                return  True

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
    elif constraint == 8:       #y = ax^2 + bx + c
        for y in Dj:
            if y== x*x + x + 1:
                return True
        return False
    elif constraint == 9:       #x = ay^2 + by + c
        for y in Dj:
            if y*y + y + 1==x:
                return True
        return False
    elif constraint == 10:      #y = mx + c
        for y in Dj:
            if y== 2*x + 1:
                return True
        return False

    elif constraint == 11:      #my + c = x
        for y in Dj:
            if 2*y + 1 == x :
                return True
        return False


#printing Adj Matrix
def printAdjMat(adjMat):
    numberOfNodes = len(adjMat)
    for i in range(numberOfNodes):
        for j in range(numberOfNodes):
            print(adjMat[i][j],end=" ")
        print()
    print()

# graph_related_function
def generateGraph(size,edgeProbablity):

    # if size ==1:
    #     edges = 0
    # else:
    #     edges = random.randint(size,(size*(size+1))/2)

    G = nx.gnp_random_graph(size,edgeProbablity)
    adjMat = []

    #build empty adjMatrix
    for i in range(size):
        lst = []
        for j in range(size):
            lst.append(0)
        adjMat.append(lst)

    #add edges to it
    for u,v in G.edges:
        if u==v:
            continue

        constraint = int(1 + np.random.randint(11, size=1))

        if constraint == 1:
            c_uv = 1
            c_vu = 2
        elif constraint == 2:
            c_uv = 2
            c_vu = 1
        elif constraint == 5:
            c_uv = 5
            c_vu = 7
        elif constraint == 7:
            c_uv = 7
            c_vu = 5
        elif constraint == 8:
            c_uv = 8
            c_vu = 9
        elif constraint == 9:
            c_uv = 9
            c_vu = 8
        elif constraint == 10:
            c_uv = 10
            c_vu = 11
        elif constraint == 11:
            c_uv = 11
            c_vu = 10
        else:
            c_uv = constraint
            c_vu = constraint

        adjMat[u][v] = c_uv
        adjMat[v][u] = c_vu

    # printAdjMat(adjMat)
    return adjMat


def getEdges(adjMat):
    edgeList = []
    for i in range(0,len(adjMat)):
        for j in range(0,len(adjMat)):
            if adjMat[i][j]!=0 and i!=j:
                edgeList.append((i,j))
    return edgeList


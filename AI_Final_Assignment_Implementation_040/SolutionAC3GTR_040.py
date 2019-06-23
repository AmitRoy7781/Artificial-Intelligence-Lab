from Utility2 import *


def AC3GTR(edgeList, adjMat, domainList):
    queue = []
    for edge in edgeList:
        # rev+=1
        queue.append(edge)

    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}

    numberOfNodes = len(adjMat)  # change here



    # for x in range(1000):
    #     dict3[x] = -1

    for x in range(numberOfNodes):
        dict2[x] = dict3

    for x in range(numberOfNodes):
        dict1[x] = dict2

    Mark = {}

    for x in range(numberOfNodes):
        Mark[x] = {}

    for x in range(len(domainList)):
        D = domainList[x]
        for y in D:
            Mark[x][y] = 1


    while len(queue)!=0:

        edge = queue[0]
        queue.remove(edge)

        node1 = edge[0]
        node2 = edge[1]
        Di = domainList[node1]
        Dj = domainList[node2]
        constraint = adjMat[node1][node2]


        change,Di,dict1[node1][node2],dict1[node2][node1],Mark = REVISE(dict1[node1][node2],dict1[node2][node1],node1,node2,Di, Dj, constraint, Mark)
        domainList[node1] = Di

        if change is True:


            # if len(Di) == 0:
            #     break


            i = node1
            for k in range(0, len(adjMat)):
                if adjMat[k][i] and i != k and k != node2:
                    queue.append((k,i))
                    #rev+=1
                    #queue.append((i, k))


    return domainList

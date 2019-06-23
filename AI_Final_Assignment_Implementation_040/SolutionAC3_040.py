from Utility import *


def AC3(edgeList, adjMat, domainList):
    queue = []
    for edge in edgeList:
        # rev+=1
        queue.append(edge)

    while len(queue)!=0:

        edge = queue[0]
        queue.remove(edge)

        node1 = edge[0]
        node2 = edge[1]
        Di = domainList[node1]
        Dj = domainList[node2]
        constraint = adjMat[node1][node2]


        change, Di,cnt = REVISE(Di, Dj, constraint)
        domainList[node1] = Di

        if change is True:


            if len(Di) == 0:
                break


            i = node1
            for k in range(0, len(adjMat)):
                if adjMat[k][i] and i != k and k != node2:
                    queue.append((k,i))
                    #rev+=1
                    #queue.append((i, k))


    return domainList

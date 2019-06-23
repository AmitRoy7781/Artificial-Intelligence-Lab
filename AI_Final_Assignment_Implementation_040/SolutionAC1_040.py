from Utility import *


def AC1(edgeList,adjMat,domainList):


    queue = []
    for edge in edgeList:
        queue.append(edge)

    while True:
        change = False

        for edge in queue:

            node1 = edge[0]
            node2 = edge[1]
            Di = domainList[node1]
            Dj = domainList[node2]
            constraint = adjMat[node1][node2]


            ret,Di,cnt = REVISE(Di,Dj,constraint)
            domainList[node1] = Di

            change |= ret

        if change is False:
            break


    return domainList

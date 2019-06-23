from Utility import *
from copy import  deepcopy

def containEdge(Q,edge):
    for e in Q:
        if e == edge:
            return True
    return False


def AC2(edgeList,adjMat,domainList):


    numberOfNodes = len(adjMat)


    queue = []
    queuePrime = []


    for i in range(numberOfNodes):

        for j in range(0,i):
            if adjMat[i][j]:
                queue.append((i,j))
                queuePrime.append((j,i))

        while len(queue)!=0:

            while len(queue)!=0:

                edge = queue[0]
                queue.remove(edge)
                k = edge[0]
                m = edge[1]

                Di = domainList[k]
                Dj = domainList[m]
                constraint = adjMat[k][m]


                change, Di,cnt = REVISE(Di, Dj, constraint)
                domainList[k] = Di

                if change is True:
                    for edge2 in edgeList:
                        node1 = edge2[0]
                        node2 = edge2[1]

                        if node1 == k and node2 != m and node2<=i:
                            if containEdge(queuePrime,(node2,node1)) is False:
                                queuePrime.append((node2,node1))
                        # elif node2==k and node1 != m and node1 <=i:
                        #     queuePrime.append((node1,node2))

            queue = deepcopy(queuePrime)
            queuePrime = []


    return domainList


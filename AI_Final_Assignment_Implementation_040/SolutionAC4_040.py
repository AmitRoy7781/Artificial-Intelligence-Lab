from Utility import *
from copy import deepcopy


def AC4(edgeList, adjMat, domainList):
    q = []
    S = {}
    C = {}
    numberOfNodes = len(adjMat)

    for vi in range(numberOfNodes):
        for ai in domainList[vi]:
            for vj in range(numberOfNodes):
                C[(vi, ai, vj)] = 0

    for vj in range(numberOfNodes):
        for aj in domainList[vj]:
            S[(vj, aj)] = []

    for edge in edgeList:
        vi, vj = edge
        domain1 = deepcopy(domainList[vi])
        domain2 = deepcopy(domainList[vj])
        constraint = adjMat[vi][vj]
        # rev+=1

        for ai in domain1:
            for aj in domain2:

                if satisfy(ai, aj, constraint):
                    C[(vi, ai, vj)] += 1
                    S[(vj, aj)].append((vi, ai))

            if C[(vi, ai, vj)] == 0:
                # rev+= 1
                q.append((vi, ai))
                domainList[vi].remove(ai)

                if len(domainList[vi])==0:
                    return domainList



    while len(q) != 0:
        vj, aj = q[0]
        q.remove(q[0])

        for vi,ai in S[(vj,aj)]:
            flag = False
            for tempDomain in domainList[vi]:
                if ai == tempDomain:
                    flag = True
                    break

            if flag is True:
                C[(vi, ai, vj)] -= 1
                if C[(vi, ai, vj)] ==0:
                    q.append((vi, ai))
                    domainList[vi].remove(ai)

                    if len(domainList[vi]) == 0:
                        return domainList

    return domainList
from Utility import *
from SolutionAC1_040 import *
from SolutionAC2_040 import *
from SolutionAC3_040 import *
from SolutionAC4_040 import *
from copy import deepcopy


def printDomain(domainList):
    for i in range(len(domainList)):
        print((i+1), domainList[i])



if __name__ == '__main__':


    solutionFound = False

    while solutionFound is False:

        numberOfNodes =5
        adjMat = generateGraph(numberOfNodes,0.5)
        # adjMat = getAdjMat()
        printAdjMat(adjMat)
        edgeList = getEdges(adjMat)
        # print(edgeConstraint)
        # showGraph(edgeList, edgeLabel)
        domainList = getDomainList(numberOfNodes)




        # domainList = getDomainList2()
        printDomain(domainList)

        domainList1 = AC1(deepcopy(edgeList),deepcopy(adjMat),deepcopy(domainList))
        domainList2 = AC2(deepcopy(edgeList),deepcopy(adjMat),deepcopy(domainList))
        domainList3 = AC3(deepcopy(edgeList),deepcopy(adjMat),deepcopy(domainList))
        domainList4 = AC4(deepcopy(edgeList),deepcopy(adjMat),deepcopy(domainList))



        solutionFound = True
        for i in range(numberOfNodes):


            if len(domainList1[i])==0 or len(domainList2[i])==0 or len(domainList3[i])==0 or len(domainList4[i])==0:
                solutionFound = False
                break


        if solutionFound is True:
            for i in range(numberOfNodes):
                print("AC1: ", (domainList1[i]))
                print("AC2: ", (domainList2[i]))
                print("AC3: ", (domainList3[i]))
                print("AC4: ", (domainList4[i]))
            #showGraph(edgeList, edgeLabel,numberOfNodes)

            # if domainList1==domainList3:
            #     print("Amit")






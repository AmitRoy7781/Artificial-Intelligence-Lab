from Utility import *
from SolutionAC1_040 import *
from SolutionAC2_040 import *
from SolutionAC3_040 import *
from SolutionAC4_040 import *
from copy import deepcopy

from matplotlib import pyplot as plt
import time






if __name__ == '__main__':

    x  = []
    yAC1 = []
    yAC2 = []
    yAC3 = []
    yAC4 = []


    type = input("Node(n)/Edges(e): ")
    st = float(input("Start: "))
    en = float(input("End: "))
    step = float(input("Step Size: "))

    numberOfNodes = 200
    edgeProbability = 0.5

    while st<=en:



        if type == 'n':
            numberOfNodes = int(st)
        else:
            edgeProbability = st

        cnt = 10
        print(st)

        AC1_Time = 0
        AC2_Time = 0
        AC3_Time = 0
        AC4_Time = 0

        for i in range(cnt):

            adjMat = generateGraph(numberOfNodes, edgeProbability)
            edgeList = getEdges(adjMat)
            domainList = getDomainList(numberOfNodes)

            startTime = time.time()
            domainList1 = AC1(deepcopy(edgeList),deepcopy(adjMat),deepcopy(domainList))
            elapsedTime = time.time() - startTime
            #yAC1.append(elapsedTime)
            AC1_Time += elapsedTime


            startTime = time.time()
            domainList2 = AC2(deepcopy(edgeList), deepcopy(adjMat), deepcopy(domainList))
            elapsedTime = time.time() - startTime
            # yAC2.append(elapsedTime)
            AC2_Time += elapsedTime

            startTime = time.time()
            domainList3 = AC3(deepcopy(edgeList), deepcopy(adjMat), deepcopy(domainList))
            elapsedTime = time.time() - startTime
            # yAC3.append(elapsedTime)
            AC3_Time += elapsedTime

            startTime = time.time()
            domainList4 = AC4(deepcopy(edgeList), deepcopy(adjMat), deepcopy(domainList))
            elapsedTime = time.time() - startTime
            # yAC4.append(elapsedTime)
            AC4_Time += elapsedTime

        if type =='n':
            x.append(numberOfNodes)
        else:
            x.append(edgeProbability)

        yAC1.append((1000*AC1_Time)/cnt)
        yAC2.append((1000*AC2_Time)/cnt)
        yAC3.append((1000*AC3_Time)/cnt)
        yAC4.append((1000*AC4_Time)/cnt)

        st += step



    print("AC1: ")
    for val in yAC1:
        print(val)

    print("AC2: ")
    for val in yAC2:
        print(val)

    print("AC3: ")
    for val in yAC3:
        print(val)

    print("AC4: ")
    for val in yAC4:
        print(val)



    plt.plot(x, yAC1, color='g', label='AC 1')
    plt.plot(x, yAC2, color='b', label='AC 2')
    plt.plot(x, yAC3, color='r', label='AC 3')
    plt.plot(x, yAC4, color='y', label='AC 4')
    plt.ylabel('Running Time (msec)')

    if type=='n':
        plt.xlabel('Number of Nodes')
    else:
        plt.xlabel('Edge Percentages')
    plt.suptitle('Comparative Performance Analysis of Arc Consistency AC Algorithm')
    plt.title('Amit Roy, Roll: 40')
    plt.legend(loc='upper left')
    plt.savefig('performance.png')
    plt.show()



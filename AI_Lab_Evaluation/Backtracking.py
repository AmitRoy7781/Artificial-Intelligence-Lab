from Utility import *
from copy import *

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def satisfy(x,y,constraint):

    if constraint == 0:
        return True
    elif constraint == 1:  # y<=x
        if y <= x:
            return True;
        return False

    elif constraint == 2:  # y>=x
        if y >= x:
            return True;
        return False

    elif constraint == 3:  # y=x
        if y == x:
            return True;
        return False

    elif constraint == 4:  # y!=x
        if y != x:
            return True;
        return False

    elif constraint == 5:  # y%x=0
        if x != 0 and y % x == 0:
            return True
        return False

    elif constraint == 6:  # gcd(x,y)=1
        if gcd(x, y) == 1:
            return True;
        return False;
    elif constraint == 7: #x%y==0
        if y != 0 and x % y == 0:
            return True
        return False



def isConsistent(adjMat,A,X,x):

    for Y,y in A.items():
        constraint = adjMat[X][Y]
        if satisfy(x,y,constraint) is False:
            return False
    return True


def isComplete(numberOfNodes,A):
    for nodes in range(numberOfNodes):
        if nodes not in A.keys():
            return False
    return True



def BT_FC(numberOfNodes,adjMat,A,U,D):

    if isComplete(numberOfNodes,A):
        print(A)
        return  True

    if len(U)==0:
        #print(A)
        return False


    X = U[0]
    U.remove(X)


    for x in D[X]:
        if isConsistent(adjMat,A,X,x):
            A[X] = x
            Dprime = deepcopy(D)


            adjY = []
            for Y in U:
                if adjMat[X][Y]:
                    adjY.append(Y)
                    temp = []
                    for yy in Dprime[Y]:
                        for node,xx in A.items():

                            # xx = A[node]
                            # yy = y
                            constraint = adjMat[node][Y]

                            if satisfy(xx,yy,constraint):
                                temp.append(yy)

                    Dprime[Y] = temp

            flag = True

            for Y in adjY:
                if len(Dprime[Y]) == 0:
                    flag = False
                    break
            if flag:
                result = BT_FC(numberOfNodes,adjMat,A,U,Dprime)

                if result is not False:
                    return result

            A.pop(x, None)

    return False


if __name__ == '__main__':

    solutionFound = False;

    while solutionFound is False:

        numberOfNodes = 5
        adjMat = generateGraph(numberOfNodes)


        A = {}

        U = []
        for nodes in range(numberOfNodes):
            U.append(nodes)


        D = getDomainList(numberOfNodes)



        ret  = BT_FC(deepcopy(numberOfNodes),deepcopy(adjMat)
              ,deepcopy(A),deepcopy(U),deepcopy(D))

        solutionFound |= ret

        print(solutionFound)

        if solutionFound:
            print(adjMat)
            printConstraint(adjMat)




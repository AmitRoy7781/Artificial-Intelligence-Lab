# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

from game import Directions

from collections import deque
# from queue import PriorityQueue
import heapq

goalState = ""
goal_found = False
maxDepth = 1


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    vis = {}
    parent = {}
    distance = {}
    global goalState
    global goal_found

    goalState = ""
    goal_found = False

    distance[startState] = 0

    dfs_util(problem, startState, vis, parent, distance)

    moves = []
    while True:

        if goalState not in parent.keys():
            break

        parentState = parent[goalState]

        goalState = parentState[0]
        moves.append(parentState[2])

    moves.reverse()
    # print(moves)
    return moves


def dfs_util(problem, parentState, vis, parent, distance):
    vis[parentState] = 1
    if problem.isGoalState(parentState):
        global goalState
        global goal_found

        goalState = parentState
        goal_found = True

        return

    successorList = problem.getSuccessors(parentState)
    successorList.reverse()

    for currentStateInfo in successorList:
        currentState = currentStateInfo[0]
        currentStateCost = currentStateInfo[2]

        if currentState not in vis.keys():
            distance[currentState] = distance[parentState] + currentStateCost
            parent[currentState] = [parentState]
            parent[currentState] += currentStateInfo
            dfs_util(problem, currentState, vis, parent, distance)

        global goal_found

        if goal_found is True:
            break


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    vis = {}
    distance = {}
    queue = deque()
    parent = {}

    startState = problem.getStartState()

    queue.append(startState)
    vis[startState] = True
    distance[startState] = 0

    while len(queue) is not 0:
        parentState = queue[0]
        queue.popleft()

        if problem.isGoalState(parentState):
            goalState = parentState
            break

        successorList = problem.getSuccessors(parentState)
        for currentStateInfo in successorList:
            currentState = currentStateInfo[0]
            # currentStateDirection = currentStateInfo[1]
            currentStateCost = currentStateInfo[2]

            if currentState not in vis.keys():
                queue.append(currentState)
                vis[currentState] = True
                distance[currentState] = distance[parentState] + currentStateCost
                parent[currentState] = [parentState]
                parent[currentState] += currentStateInfo

    moves = []
    while True:
        if goalState is startState:
            break

        parentState = parent[goalState]

        goalState = parentState[0]
        moves.append(parentState[2])

    moves.reverse()
    # print(moves)
    return moves


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()

    queue = util.PriorityQueue()
    parent = {}
    distance = {}

    queue.push(startState,0)
    distance[startState] = 0

    while not queue.isEmpty():

        parentState = queue.pop()

        if problem.isGoalState(parentState):
            goalState = parentState
            break

        successorList = problem.getSuccessors(parentState)
        for currentStateInfo in successorList:
            currentState = currentStateInfo[0]
            currentStateCost = currentStateInfo[2]

            if currentState not in distance.keys():
                distance[currentState] = distance[parentState] + currentStateCost
                parent[currentState] = [parentState]
                parent[currentState] += currentStateInfo
                queue.push(currentState,distance[currentState])

            elif distance[currentState] > distance[parentState] + currentStateCost:
                distance[currentState] = distance[parentState] + currentStateCost
                parent[currentState] = [parentState]
                parent[currentState] += currentStateInfo
                queue.push(currentState, distance[currentState])
    moves = []
    while True:
        if goalState is startState:
            break

        parentState = parent[goalState]

        goalState = parentState[0]
        moves.append(parentState[2])

    moves.reverse()
    # print(moves)
    return moves


def iterativeDeepeningSearch(problem):
    startState = problem.getStartState()

    global goalState
    global goal_found
    global maxDepth

    goalState = ""
    goal_found = False
    maxDepth = 1

    while goal_found is False:
        vis = {}
        parent = {}
        distance = {}
        distance[startState] = 0

        ids_dfs_util(problem, startState, vis, parent, distance, 0)

        maxDepth += 1

    moves = []
    while True:

        if goalState not in parent.keys():
            break

        parentState = parent[goalState]

        goalState = parentState[0]
        moves.append(parentState[2])

    moves.reverse()
    # print(moves)
    return moves


def ids_dfs_util(problem, parentState, vis, parent, distance, depth):
    global maxDepth

    if depth > maxDepth:
        return

    vis[parentState] = 1

    if problem.isGoalState(parentState):
        global goalState
        global goal_found

        goalState = parentState
        goal_found = True

        return

    successorList = problem.getSuccessors(parentState)

    for currentStateInfo in successorList:
        currentState = currentStateInfo[0]
        currentStateCost = currentStateInfo[2]

        if currentState not in vis.keys():
            distance[currentState] = distance[parentState] + currentStateCost
            parent[currentState] = [parentState]
            parent[currentState] += currentStateInfo
            ids_dfs_util(problem, currentState, vis, parent, distance, depth + 1)

            global goal_found

            if goal_found is True:
                return


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    startState = problem.getStartState()

    queue = util.PriorityQueue()
    parent = {}
    distance = {}

    queue.push(startState, 0+heuristic(startState,problem))
    distance[startState] = 0

    while not queue.isEmpty():

        parentState = queue.pop()

        if problem.isGoalState(parentState):
            goalState = parentState
            break

        successorList = problem.getSuccessors(parentState)
        for currentStateInfo in successorList:
            currentState = currentStateInfo[0]
            currentStateCost = currentStateInfo[2]

            if currentState not in distance.keys():
                distance[currentState] = distance[parentState] + currentStateCost
                parent[currentState] = [parentState]
                parent[currentState] += currentStateInfo
                queue.push(currentState, distance[currentState]+heuristic(currentState,problem))
            elif (distance[currentState] > distance[parentState] + currentStateCost):
                distance[currentState] = distance[parentState] + currentStateCost
                parent[currentState] = [parentState]
                parent[currentState] += currentStateInfo
                queue.push(currentState, distance[currentState]+heuristic(currentState,problem))

    moves = []
    while True:
        if goalState is startState:
            break

        parentState = parent[goalState]

        goalState = parentState[0]
        moves.append(parentState[2])

    moves.reverse()
    # print(moves)
    return moves


def greedyBestFirstSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    startState = problem.getStartState()

    queue = util.PriorityQueue()
    parent = {}
    distance = {}

    queue.push(startState, 0 + heuristic(startState, problem))
    distance[startState] = 0

    while not queue.isEmpty():

        parentState = queue.pop()

        if problem.isGoalState(parentState):
            goalState = parentState
            break

        successorList = problem.getSuccessors(parentState)
        for currentStateInfo in successorList:
            currentState = currentStateInfo[0]
            currentStateCost = currentStateInfo[2]

            if currentState not in distance.keys():
                distance[currentState] = distance[parentState] + currentStateCost
                parent[currentState] = [parentState]
                parent[currentState] += currentStateInfo
                queue.push(currentState,heuristic(currentState, problem))


    moves = []
    while True:
        if goalState is startState:
            break

        parentState = parent[goalState]

        goalState = parentState[0]
        moves.append(parentState[2])

    moves.reverse()
    # print(moves)
    return moves


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
rbfs = greedyBestFirstSearch



#dfs:
# python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs -z .5
# python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs -z .5
# python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs -z .5

#bfs
#python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs -z .5
#python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs -z .5
#python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

#ucs
#python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs -z .5
#python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs -z .5
#python pacman.py -l bigMaze -p SearchAgent -a fn=ucs -z .5

#ids
#python pacman.py -l tinyMaze -p SearchAgent -a fn=ids -z .5
#python pacman.py -l mediumMaze -p SearchAgent -a fn=ids -z .5
#python pacman.py -l bigMaze -p SearchAgent -a fn=ids -z .5

#astar
#python pacman.py -l tinyMaze -p SearchAgent -a fn=astar -z .5
#python pacman.py -l mediumMaze -p SearchAgent -a fn=astar -z .5
#python pacman.py -l bigMaze -p SearchAgent -a fn=astar -z .5

#rbfs
#python pacman.py -l tinyMaze -p SearchAgent -a fn=rbfs -z .5
#python pacman.py -l mediumMaze -p SearchAgent -a fn=rbfs -z .5
#python pacman.py -l bigMaze -p SearchAgent -a fn=rbfs -z .5









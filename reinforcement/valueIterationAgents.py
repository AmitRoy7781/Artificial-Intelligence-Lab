# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.actions = {}

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        cnt = 0                         #a counter to iterate for given number of iterations
        while cnt <self.iterations:

            MaxUtilityValues = {}               #temporary dict to store the maximum utility value per state
            actionsMaxUtility = {}              #temporary dict to store the actions of the maximum utility value
            states = self.mdp.getStates()       #all states of the markov decision process


            for state in states:                              #iterating through all the state

                actions = self.mdp.getPossibleActions(state)  #all possible set of actions from the given state

                if len(actions) == 0 :                         # no actions available for the given state
                    MaxUtilityValues[state] = 0                # setting maxUtility to zero
                    actionsMaxUtility[state] = None            # setting actions for max utility to None

                else:
                    MaxUtilityValues[state] = -1000000000000000000000   #setting Max utility to a large negative number
                    for action in actions:                              #iterating through all the action
                        utilityVal = self.computeQValueFromValues(state,action) #utiilty value from the state for the current action
                        if utilityVal > MaxUtilityValues[state]:                #if utility value is greater than the previous utility of the current state
                            MaxUtilityValues[state] = utilityVal                #setting maxUtilityValue of the current state to the utility  value
                            actionsMaxUtility[state] = action                   #seting actionsMaxutility of the current state to current action

            cnt+= 1         #increasing the loop counter

            self.values = MaxUtilityValues      #storing local values to global values
            self.actions = actionsMaxUtility

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        edges = self.mdp.getTransitionStatesAndProbs(state,action)

        #edges contain all possible transition from given state and for given action
        #each transition contain next state and the probability of going to that state

        ret = 0
        #contain the Q-value for all possible transitions from given state and for action

        for edge in edges:
            s = state               # s = start state
            sprime = edge[0]        # sprime = next state
            a = action              # a = action

            transition_probability = edge[1]                             # probability of transition from s to sprime by given action a: T(s,a,sprime)
            transition_reward = self.mdp.getReward(s, a, sprime)         # reward of transition from s to sprime by using given action a: r(s,a,sprime)
            transition_utility = self.getValue(sprime)                   # utility of state sprime: u(sprime)
            transition_discount = self.discount                          # discount gamma

            ret += (transition_reward + (transition_discount * transition_probability * transition_utility))
            #since the reward is associated with every transition from state u to state v
            #so I have added it for every transition, instead of adding only once after calculating
            #the enire Qvalue of a particular state for a given action

        return ret
        # util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """

        # "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        actions = self.actions
        if len(actions) ==0:
            return None
        return actions[state]


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


#python gridworld.py -a value -i 100 -k 10
#python gridworld.py -a value -i 5

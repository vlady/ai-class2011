# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    frontier = Stack()
    frontier.push(problem.getStartState())
    reached = {}
    reached[problem.getStartState()] = None

    path = []
    while not frontier.isEmpty():
        state = frontier.pop()
        if problem.isGoalState(state):
            # backtrack the steps
            while reached[state] is not None:
                action_pack = reached[state]
                state = action_pack[0]
                path.append(action_pack[1])
            path.reverse()
            break
        for s in problem.getSuccessors(state):
            next_state = s[0]
            if reached.has_key(next_state):
                continue
            action = s[1]
            reached[next_state] = (state, action)
            frontier.push(next_state)
    return path

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    from util import Queue
    frontier = Queue()
    frontier.push(problem.getStartState())
    reached = {}
    reached[problem.getStartState()] = None

    path = []
    while not frontier.isEmpty():
        state = frontier.pop()
        if problem.isGoalState(state):
            # backtrack the steps
            while reached[state] is not None:
                action_pack = reached[state]
                state = action_pack[0]
                path.append(action_pack[1])
            path.reverse()
            break
        for s in problem.getSuccessors(state):
            next_state = s[0]
            if reached.has_key(next_state):
                continue
            action = s[1]
            reached[next_state] = (state, action)
            frontier.push(next_state)
    return path

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    from util import PriorityQueue
    frontier = PriorityQueue()
    frontier.push(problem.getStartState(), 0)
    reached = {}
    reached[problem.getStartState()] = (None, None, 0)

    path = []
    while not frontier.isEmpty():
        state = frontier.pop()
        if problem.isGoalState(state):
            # backtrack the steps
            while reached[state][0] is not None:
                action_pack = reached[state]
                state = action_pack[0]
                path.append(action_pack[1])
            path.reverse()
            break
        for s in problem.getSuccessors(state):
            next_state = s[0]
            if reached.has_key(next_state):
                continue
            action = s[1]
            cost = s[2] + reached[state][2]
            reached[next_state] = (state, action, cost)
            frontier.push(next_state, cost)
    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

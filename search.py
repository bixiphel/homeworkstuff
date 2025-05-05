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
from smtpd import program

import util
from util import Stack


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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    # Initialize data structures
    stack = Stack()     # Holds the list of nodes to visit. Data is stored as ( (x,y), [path] ), where (x,y) is the location, and [path] is the path of nodes to the current location
    visited = []        # Holds the list of nodes that have been visited
    path = []           # Stores the path of nodes from the starting state

    # Basic check to see if the starting state is the goal state
    if problem.isGoalState(problem.getStartState()):
        return []       # This returns an empty list because we don't move from a node to another node

    # Adds the initial state to the stack with an empty path (since we haven't moved yet) as a tuple
    stack.push( (problem.getStartState(), []) )

    # Performs the search
    while not stack.isEmpty():
        state, path = stack.pop()       # Observes the top element of the stack and splits it into the location (state) and path components
        visited.append(state)           # Adds the node to the list of visited nodes

        # Checks if the current node is the goal state and returns it if it is
        if problem.isGoalState(state):
            return path

        # Creates a temporary list of all the successors of the current state
        successors = problem.getSuccessors(state)

        # Adds the successors to the stack **ONLY IF** they have not been visited before
        if successors:          # Initial check to see if the node has successors to add in the first place
            for item in successors:
                if item[0] not in visited:
                    # I was having some trouble with formatting the path and found something similar to this on a forum, which ended up working
                    newPath = path + [item[1]]
                    stack.push((item[0], newPath))

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # I reviewed the class notes and watched some of the 2018 lectures for CS 188 at Berkeley, and BFS is almost the same thing as DFS but with a queue
    # Hence I just pasted the code from above and made some tweaks.

    from util import Queue

    # Initialize data structures
    queue = Queue()  # Holds the list of nodes to visit. Data is stored as ( (x,y), [path] ), where (x,y) is the location, and [path] is the path of nodes to the current location
    visited = []  # Holds the list of nodes that have been visited

    # Basic check to see if the starting state is the goal state
    if problem.isGoalState(problem.getStartState()):
        return []  # This returns an empty list because we don't move from a node to another node

    # Adds the initial state to the stack with an empty path (since we haven't moved yet) as a tuple
    queue.push((problem.getStartState(), []))           # The queue from util uses the push function to add elements

    # Performs the search
    while not queue.isEmpty():
        # The queue's pop function is literally the same as the stack's, so this doesn't do anything different
        state, path = queue.pop()  # Observes the top element of the stack and splits it into the location (state) and path components
        visited.append(state)  # Adds the node to the list of visited nodes

        # Checks if the current node is the goal state and returns it if it is
        if problem.isGoalState(state):
            return path

        # Creates a temporary list of all the successors of the current state
        successors = problem.getSuccessors(state)

        # Adds the successors to the stack **ONLY IF** they have not been visited before
        if successors:  # Initial check to see if the node has successors to add in the first place
            for item in successors:
                # This was a more substantial change, but follows the pseudocode from the slides and the fomatting
                if item[0] not in visited and item[0] not in (state[0] for state in queue.list):
                    # I was having some trouble with formatting the path and found something similar to this on a forum, which ended up working
                    newPath = path + [item[1]]
                    queue.push((item[0], newPath))

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # The 'util.py' file provides a Priority Queue instead of a Heap, so I'll use that and paste the code from BFS with some tweaks
    from util import PriorityQueue

    # Initialize data structures
    pq = PriorityQueue()  # Holds the list of nodes to visit. Data is stored as ( (x,y), [path] ), where (x,y) is the location, and [path] is the path of nodes to the current location
    visited = []  # Holds the list of nodes that have been visited

    # Basic check to see if the starting state is the goal state
    if problem.isGoalState(problem.getStartState()):
        return []  # This returns an empty list because we don't move from a node to another node

    # Priority Queues also take a priority as a parameter, hence the 0
    pq.push((problem.getStartState(), []), 0)  # The queue from util uses the push function to add elements

    # Performs the search
    while not pq.isEmpty():
        # The queue's pop function is literally the same as the stack's, so this doesn't do anything different
        state, path = pq.pop()  # Observes the top element of the stack and splits it into the location (state) and path components
        visited.append(state)  # Adds the node to the list of visited nodes

        # Checks if the current node is the goal state and returns it if it is
        if problem.isGoalState(state):
            return path

        # Creates a temporary list of all the successors of the current state
        successors = problem.getSuccessors(state)

        # Adds the successors to the stack **ONLY IF** they have not been visited before
        if successors:  # Initial check to see if the node has successors to add in the first place
            for item in successors:
                # This was adapted from the BFS successor conditionals and tweaked to mirror the pseudocode from the lecture slides
                if item[0] not in visited and item[0] not in (state[2][0] for state in pq.heap):
                    # I was having some trouble with formatting the path and found something similar to this on a forum, which ended up working
                    newPath = path + [item[1]]
                    newPriority = problem.getCostOfActions(newPath)         # We have to calculate the priority of the next action
                    pq.push((item[0], newPath), newPriority)
                # If the state is already in the Priority Queue, this checks if the current path is cheaper than the previously stored one
                elif item[0] not in visited and item[0] in (state[2][0] for state in pq.heap):
                    for state in pq.heap:
                        if state[2][0] == item[0]:
                            oldPriority = problem.getCostOfActions(state[2][1])

                    newPriority = problem.getCostOfActions(path + [item[1]])

                    # Updates the priority of the new priority score is cheaper than the old one
                    if oldPriority > newPriority:
                        newPath = path + [item[1]]
                        pq.update((item[0], newPath), newPriority)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # This is the same as the UCS algorithm, but the cost has an additional term added on top of it: the heuristic cost
    # The pseudocode for this is line-for-line the same except where we calculate the new cost, so we can again paste the previous code

    # The 'util.py' file provides a Priority Queue instead of a Heap, so I'll use that and paste the code from BFS with some tweaks
    from util import PriorityQueue

    # Initialize data structures
    pq = PriorityQueue()  # Holds the list of nodes to visit. Data is stored as ( (x,y), [path] ), where (x,y) is the location, and [path] is the path of nodes to the current location
    visited = []  # Holds the list of nodes that have been visited

    # Basic check to see if the starting state is the goal state
    if problem.isGoalState(problem.getStartState()):
        return []  # This returns an empty list because we don't move from a node to another node

    # Priority Queues also take a priority as a parameter, hence the 0
    pq.push((problem.getStartState(), []), 0)  # The queue from util uses the push function to add elements

    # Performs the search
    while not pq.isEmpty():
        # The queue's pop function is literally the same as the stack's, so this doesn't do anything different
        state, path = pq.pop()  # Observes the top element of the stack and splits it into the location (state) and path components
        visited.append(state)  # Adds the node to the list of visited nodes

        # Checks if the current node is the goal state and returns it if it is
        if problem.isGoalState(state):
            return path

        # Creates a temporary list of all the successors of the current state
        successors = problem.getSuccessors(state)

        # Adds the successors to the stack **ONLY IF** they have not been visited before
        if successors:  # Initial check to see if the node has successors to add in the first place
            for item in successors:
                # This was adapted from the BFS successor conditionals and tweaked to mirror the pseudocode from the lecture slides
                if item[0] not in visited and item[0] not in (state[2][0] for state in pq.heap):
                    # I was having some trouble with formatting the path and found something similar to this on a forum, which ended up working
                    newPath = path + [item[1]]
                    newPriority = problem.getCostOfActions(newPath) + heuristic(item[0], problem)
                    pq.push((item[0], newPath), newPriority)
                # If the state is already in the Priority Queue, this checks if the current path is cheaper than the previously stored one
                elif item[0] not in visited and item[0] in (state[2][0] for state in pq.heap):
                    for state in pq.heap:
                        if state[2][0] == item[0]:
                            oldPriority = problem.getCostOfActions(state[2][1])

                    newPriority = problem.getCostOfActions(path + [item[1]]) + heuristic(item[0], problem)

                    # Updates the priority of the new priority score is cheaper than the old one
                    if oldPriority > newPriority:
                        newPath = path + [item[1]]
                        pq.update((item[0], newPath), newPriority)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

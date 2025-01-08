from node import *

# Represent a search result
class Result:
    def __init__(self, initial_state, search_objective, path, cost, gen_nodes, 
                 visit_nodes, algorithm=None, verbose = False):
        self.initial_state = initial_state
        self.search_objective = search_objective
        self.path = path
        self.cost = cost
        self.gen_nodes = gen_nodes
        self.visit_nodes = visit_nodes
        self.algorithm = algorithm
        self.cost_function = Node.cost_function
        self.heuristic = Node.heuristic_function
        self.verbose = verbose
    
    def __str__(self):
        res = f"""Inital State: {self.initial_state}
Search Objective: {self.search_objective}
Path: {self.path}
Path Cost: {self.cost}
Count Nodes Genereted: {self.gen_nodes}
Count Nodes Visited: {self.visit_nodes}
"""
        if self.verbose:
            res += f"""Algorithm: {self.algorithm}
Cost Function: {self.cost_function}
Heuristic: {self.heuristic}
"""
        return res

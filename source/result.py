class Result:
    def __init__(self, initial_state, search_objective, path, cost, gen_nodes, 
                 visit_nodes):
        self.initial_state = initial_state
        self.search_objective = search_objective
        self.path = path
        self.cost = cost
        self.gen_nodes = gen_nodes
        self.visit_nodes = visit_nodes
    
    def __str__(self):
        return f"""Inital State: {self.initial_state}
Search Objective: {self.search_objective}
Path: {self.path}
Path Cost: {self.cost}
Count Nodes Genereted: {self.gen_nodes}
Count Nodes Visited: {self.visit_nodes}
"""

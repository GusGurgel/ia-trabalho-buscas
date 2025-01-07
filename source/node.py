class Node:
    def __init__(self, pos, t, cost, prev=None):
        self.pos = pos    # node position
        self.t = t        # node depth
        self.cost = cost  # cost to node
        self.prev = prev  # node parent
    
    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost
    
    def __str__(self):
        return f"pos: {self.pos}, t: {self.t}, cost: {self.cost}"
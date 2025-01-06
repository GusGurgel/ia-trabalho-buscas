class Node:
    def __init__(self, pos, t, cost, prev=None):
        self.pos = pos
        self.t = t
        self.cost = cost
        self.prev = prev
    
    def __str__(self):
        return f"pos: {self.pos}, t: {self.t}, cost: {self.cost}, prev: {self.prev.pos}"
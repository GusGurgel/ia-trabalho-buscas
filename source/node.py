class Node:
    def __init__(self, pos, cost=0, parrent=None):
        self.pos = pos    # node position
        self.cost = cost  # cost to node
        self.parrent = parrent  # node parent

        # Calculte node depth
        if self.parrent == None:
            self.t = 0
        else:
            self.t = self.parrent.t + 1

        # Calculate acumulate cost
        if parrent == None:
            self.accumulate_cost = self.cost + 0
        else:
            self.accumulate_cost = self.cost + parrent.accumulate_cost
    
    def __gt__(self, other):
        return self.accumulate_cost > other.accumulate_cost

    def __lt__(self, other):
        return self.accumulate_cost < other.accumulate_cost
    
    def __str__(self):
        return f"pos: {self.pos}, depth: {self.t}, cost: {self.cost}, "
from math import sqrt
from result import Result
from node import Node

# [ Constants ]
MAP_SIZE = (30, 30) # cols x rows

# Base agente actions
F1 = lambda pos : (pos[0]-1, pos[1])
F2 = lambda pos : (pos[0]+1, pos[1])
F3 = lambda pos : (pos[0], pos[1]-1)
F4 = lambda pos : (pos[0], pos[1]+1)

# All actions and conts functions possibilities
ACTIONS_KEYS = ["f1", "f2", "f3", "f4"]
COST_KEYS = ["c1", "c2", "c3", "c4"]

# All agent actions based on cost function
ACTIONS = {
    "c1": {
        "f1": lambda node : Node(F1(node.pos), node.t+1, 10,  node),
        "f2": lambda node : Node(F2(node.pos), node.t+1, 10,  node),
        "f3": lambda node : Node(F3(node.pos), node.t+1, 10,  node),
        "f4": lambda node : Node(F4(node.pos), node.t+1, 10,  node),
    },
    "c2": {
        "f1": lambda node : Node(F1(node.pos), node.t+1, 15, node),
        "f2": lambda node : Node(F2(node.pos), node.t+1, 15, node),
        "f3": lambda node : Node(F3(node.pos), node.t+1, 10, node),
        "f4": lambda node : Node(F4(node.pos), node.t+1, 10, node),
    },
    "c3": {
        "f1": lambda node : Node(F1(node.pos), node.t+1, 10 + (abs(5-node.t+1)%6), node),
        "f2": lambda node : Node(F2(node.pos), node.t+1, 10 + (abs(5-node.t+1)%6), node),
        "f3": lambda node : Node(F3(node.pos), node.t+1, 10, node),
        "f4": lambda node : Node(F4(node.pos), node.t+1, 10, node),
    },
    "c4": {
        "f1": lambda node : Node(F1(node.pos), node.t+1, 5 + (abs(10-node.t+1)%11), node),
        "f2": lambda node : Node(F2(node.pos), node.t+1, 5 + (abs(10-node.t+1)%11), node),
        "f3": lambda node : Node(F3(node.pos), node.t+1, 10, node),
        "f4": lambda node : Node(F4(node.pos), node.t+1, 10, node),
    }
}

# Heuristic functions
def H1(pos1, pos2):
    return 10*sqrt(pow(abs(pos1[0]-pos2[0]),2)+pow(abs(pos1[1]-pos2[1]),2))

def H2(pos1, pos2):
    return 10*(abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1]))

# Return True if position is valid, otherwise return False 
def is_valid_pos(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] <= MAP_SIZE[0] and pos[1] <= MAP_SIZE[1]

def get_neighbors(node, cost_function):
    neighbors = []
    for f in ACTIONS_KEYS:
        neighbor = ACTIONS[cost_function][f](node)
        if is_valid_pos(neighbor.pos):
            neighbors.append(neighbor)
    return neighbors

# [ Variables ]
interest_points = {}

# [ Search algorithms ]

# Run on start of any search function
def search_function_prelude(inital_pos, objective_pos, cost_function):
    if cost_function not in COST_KEYS:
        raise Exception(f"Invalid cost function -> {cost_function}")
    if not is_valid_pos(inital_pos):
        raise Exception(f"Invalid inital state -> {inital_pos}")
    if not is_valid_pos(objective_pos):
        raise Exception(f"Invalid objective state -> {objective_pos}")

# Return path and cost to a searched node
def get_path_and_cost_to_node(node : Node):
    current = node
    path = []
    cost = 0
    while current != None:
        path.append(current.pos)
        cost += current.cost
        current = current.prev
    path.reverse()
    return(path, cost)

def DFS(inital_pos, objective_pos, cost_function) -> Result:
    search_function_prelude(inital_pos, objective_pos, cost_function)

    stack = [Node(inital_pos, 0, 0)] 
    visited = {}
    gen_node_count = 0
    visited_node_count = 0
    res_node = None

    while len(stack) > 0:
        current = stack.pop()
        visited[current.pos] = True
        visited_node_count += 1

        if current.pos == objective_pos:
            res_node = current
            break

        for neighbor in get_neighbors(current, cost_function):
            if not neighbor.pos in visited.keys():
                gen_node_count += 1
                stack.append(neighbor)
    
    path, cost = get_path_and_cost_to_node(res_node)
    if path == []:
        path = "Error"
        cost = None
    return Result(inital_pos, objective_pos, path, cost, gen_node_count, 
                  visited_node_count)
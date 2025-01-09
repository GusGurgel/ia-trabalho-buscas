from result import Result
from node import Node
from queue import PriorityQueue

# [ Variables ]
interest_points = {}

# [ Search algorithms ]

# Run on start of any search function
def search_function_prelude(inital_pos, objective_pos):
    if not Node(inital_pos).is_valid():
        raise Exception(f"Invalid inital state -> {inital_pos}")
    if not Node(objective_pos).is_valid():
        raise Exception(f"Invalid objective state -> {objective_pos}")

def DFS(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)

    stack = [Node(inital_pos)]
    visited = []
    generate_node_count = 0
    visited_node_count = 0
    result_node = None

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            if not neighbor.pos in visited:
                generate_node_count += 1
                stack.append(neighbor)

        visited.append(current_node.pos)
        visited_node_count += 1

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        visited_node_count,
        "DFS",
        verbose
    )


def BFS(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)

    queue = [Node(inital_pos)]
    visited = []
    generate_node_count = 0
    visited_node_count = 0
    result_node = None

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            if not neighbor.pos in visited:
                generate_node_count += 1
                queue.append(neighbor)

        visited.append(current_node.pos)
        visited_node_count += 1

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        visited_node_count,
        "BFS",
        verbose
    )

def UCS(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)

    queue = PriorityQueue()
    queue.put(Node(inital_pos))

    visited = []
    generate_node_count = 0
    visited_node_count = 0
    result_node = None

    while not queue.empty():
        current_node = queue.get()

        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            if not neighbor.pos in visited:
                generate_node_count += 1
                queue.put(neighbor)

        visited.append(current_node.pos)
        visited_node_count += 1

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        visited_node_count,
        "UCS",
        verbose
    )

def Greedy(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)

    visited = []
    generate_node_count = 0
    visited_node_count = 0
    result_node = None

    current = Node(inital_pos)
    while True:
        visited_node_count += 1
        
        # Find path case
        if current.pos == objective_pos:
            result_node = current
            current = None
            break

        # Get neighbors sorted by heuristic function
        neighbors = sorted(current.get_neighbors(), 
                           key=lambda x: x.get_heuristic_value(Node(objective_pos)))
        generate_node_count += len(neighbors)
        # Filter by visited
        neighbors = list(filter(lambda x: x.pos not in visited, neighbors))

        # print(list(map(lambda x: f"{x.pos}, {x.get_heuristic_value(Node(objective_pos))}", neighbors)))

        # No path find case
        if len(neighbors) == 0:
            current = None
            break

        # Set old node as visited
        visited.append(current.pos)

        # Get the node with lower heuristic function cost
        current = neighbors[0]


    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        visited_node_count,
        "Greedy",
        verbose
    )

def A_Star(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)
    Node.use_a_star_compration = True
    Node.a_start_objective_node = Node(objective_pos)

    queue = PriorityQueue()
    queue.put(Node(inital_pos))

    visited = []
    generate_node_count = 0
    visited_node_count = 0
    result_node = None

    while not queue.empty():
        current_node = queue.get()

        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            if not neighbor.pos in visited:
                generate_node_count += 1
                queue.put(neighbor)

        visited.append(current_node.pos)
        visited_node_count += 1

    Node.use_a_star_compration = False
    Node.a_start_objective_node = None

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        visited_node_count,
        "A_Star",
        verbose
    )

# print(A_Star((0, 0), (0, 2), True))
Node.cost_function = "c1"
Node.heuristic_function = "h1"
print(Greedy((0, 0), (1, 1), True))
from result import Result
from node import Node
from queue import PriorityQueue
import random

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
    generate_node_count = 1 # Considering inital_pos
    result_node = None

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            visited.append(current_node)
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            if not neighbor.pos in visited:
                generate_node_count += 1
                stack.append(neighbor)

        visited.append(current_node.pos)

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        len(visited),
        "DFS",
        verbose
    )


def BFS(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)

    queue = [Node(inital_pos)]
    visited = []
    generate_node_count = 1
    result_node = None

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            visited.append(current_node)
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            if not neighbor.pos in visited:
                generate_node_count += 1
                queue.append(neighbor)

        visited.append(current_node.pos)

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        len(visited),
        "BFS",
        verbose
    )

def UCS(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)

    queue = PriorityQueue()
    queue.put(Node(inital_pos))

    visited = []
    generate_node_count = 1
    result_node = None

    while not queue.empty():
        current_node = queue.get()

        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            visited.append(current_node)
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            if not neighbor.pos in visited:
                generate_node_count += 1
                queue.put(neighbor)

        visited.append(current_node.pos)

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        len(visited),
        "UCS",
        verbose
    )

def Greedy(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)

    visited = []
    generate_node_count = 1
    result_node = None

    current = Node(inital_pos)
    while True:
        # Find path case
        if current.pos == objective_pos:
            visited.append(current)
            result_node = current
            current = None
            break

        # Get neighbors sorted by heuristic function
        neighbors = sorted(current.get_neighbors(), 
                           key=lambda x: x.get_heuristic_value(Node(objective_pos)))
        generate_node_count += len(neighbors)
        # Filter by visited
        neighbors = list(filter(lambda x: x.pos not in visited, neighbors))


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
        len(visited),
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
    generate_node_count = 1
    result_node = None

    while not queue.empty():
        current_node = queue.get()

        if current_node.pos in visited:
            continue

        if current_node.pos == objective_pos:
            visited.append(current_node)
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            generate_node_count += 1
            if not neighbor.pos in visited:
                queue.put(neighbor)

        visited.append(current_node.pos)

    Node.use_a_star_compration = False
    Node.a_start_objective_node = None

    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,
        "+Infinity" if result_node == None else result_node.accumulate_cost,
        generate_node_count,
        len(visited),
        "A_Star",
        verbose
    )

def verify_tuple_is_in_array(array, tuple):
    for i in array:
        if i[0] == tuple[0] and i[1] == tuple[1]:
            return True
    return False

if __name__ == "__main__":
    starting_points = []
    destinations = []
    resultsBFS = []
    resultsDFS = []
    resultsUCS = []

    while len(starting_points) < 50:
        starting = (random.randint(0, 29), random.randint(0, 29))
        destination = (random.randint(0, 29), random.randint(0, 29))
        if not verify_tuple_is_in_array(starting_points, starting) and not verify_tuple_is_in_array(destinations, destination):
            starting_points.append(starting)
            destinations.append(destination)
            
   
    Node.heuristic_function = "h1"

    print('BFS')
    for starting in starting_points:
        Node.cost_function = "c1"
        r1 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r1)
        Node.cost_function = "c2"
        r2 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r2)
        Node.cost_function = "c3"
        r3 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r3)
        Node.cost_function = "c4"
        r4 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r4)

    print('DFS')
    for starting in starting_points:
        Node.cost_function = "c1"
        r1 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r1)
        Node.cost_function = "c2"
        r2 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r2)
        Node.cost_function = "c3"
        r3 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r3)
        Node.cost_function = "c4"
        r4 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r4)

    print('UCS')
    for starting in starting_points:
        Node.cost_function = "c1"
        r1 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r1)
        Node.cost_function = "c2"
        r2 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r2)
        Node.cost_function = "c3"
        r3 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r3)
        Node.cost_function = "c4"
        r4 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r4)
    
    print('Saving resultBFS')
    Result.saveResultsAsCSV(resultsBFS, "resultBFS.csv")
    print('Saving resultDFS')
    Result.saveResultsAsCSV(resultsDFS, "resultDFS.csv" )
    print('Saving resultUCS')
    Result.saveResultsAsCSV(resultsUCS, "resultUCS.csv")

    # Node.cost_function = "c1"
    # r1 = BFS((0, 0), (2,  2), True)
    # r2 = DFS((0, 0), (2,  2), True)

    # Result.saveResultsAsCSV([r1, r2])
    # print(A_Star((0, 0), (8,  7), True))
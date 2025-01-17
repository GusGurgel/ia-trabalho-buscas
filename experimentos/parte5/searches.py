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

def A_Star(inital_pos, objective_pos, verbose=False) -> Result:
    search_function_prelude(inital_pos, objective_pos)
    objective_state = (*objective_pos, True)
    Node.use_a_star_compration = True
    Node.a_start_objective_node = Node(objective_pos)

    queue = PriorityQueue()
    queue.put(Node((*inital_pos, False)))

    visited = []
    generate_node_count = 1
    result_node = None

    while not queue.empty():
        current_node = queue.get()

        if current_node.state in visited:
            continue

        if current_node.state == objective_state:
            visited.append(current_node)
            result_node = current_node
            break

        for neighbor in current_node.get_neighbors():
            generate_node_count += 1
            if not neighbor.state in visited:
                queue.put(neighbor)

        visited.append(current_node.state)

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
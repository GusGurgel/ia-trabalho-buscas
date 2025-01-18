from result import Result
from node import Node
from queue import PriorityQueue

# [ Algorítmos de busca ]

# Essa função deve rodar antes do início de cada algorítmo de busca. Ela
# garante que as posicões inical e de objetivos não estejam fora da borda do
# mapa.
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
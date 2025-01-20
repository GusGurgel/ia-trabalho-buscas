from result import Result
from node import Node
from queue import PriorityQueue

# [ Algorítmos de busca ]

# Essa função deve rodar antes do início de cada algorítmo de busca. Ela
# garante que as posicões inicial e de objetivo não estejam fora da borda do
# mapa.
def search_function_prelude(inital_pos, objective_pos):
    # Verifica se a posição inicial é válida.
    if not Node(inital_pos).is_valid():
        raise Exception(f"Invalid inital state -> {inital_pos}")
    # Verifica se a posição objetivo é válida.
    if not Node(objective_pos).is_valid():
        raise Exception(f"Invalid objective state -> {objective_pos}")

# Algoritmo A*
def A_Star(inital_pos, objective_pos, verbose=False) -> Result:
    # Pré-condição para garantir que os estados inicial e objetivo sejam válidos.
    search_function_prelude(inital_pos, objective_pos)

    # Define o estado objetivo, com um valor booleano se o nó já passou em
    # uma farmácia
    objective_state = (*objective_pos, True)

    # Ativa o uso de comparação A* nos nós e define o nó objetivo para cálculo de heurística.
    Node.use_a_star_compration = True
    Node.a_start_objective_node = Node(objective_pos)

    # Inicializa a fila de prioridade para o algoritmo A*.
    queue = PriorityQueue()
    queue.put(Node((*inital_pos, False)))  # Adiciona o nó inicial na fila.

    visited = []  # Lista de estados já visitados.
    generate_node_count = 1  # Contador de nós gerados.
    result_node = None  # Variável para armazenar o nó de resultado.

    # Loop principal do algoritmo A*.
    while not queue.empty():
        # Obtém o nó com menor custo total (f = g + h) da fila de prioridade.
        current_node = queue.get()

        # Verifica se o estado do nó atual já foi visitado.
        if current_node.state in visited:
            continue

        # Verifica se o nó atual é o estado objetivo.
        if current_node.state == objective_state:
            visited.append(current_node)  # Adiciona o nó objetivo na lista de visitados.
            result_node = current_node  # Define o nó atual como o resultado.
            break

        # Gera os vizinhos do nó atual e os adiciona na fila de prioridade.
        for neighbor in current_node.get_neighbors():
            generate_node_count += 1  # Incrementa o contador de nós gerados.
            if not neighbor.state in visited:
                queue.put(neighbor)

        # Marca o estado do nó atual como visitado.
        visited.append(current_node.state)

    # Restaura as configurações padrão da classe Node após a execução do algoritmo.
    Node.use_a_star_compration = False
    Node.a_start_objective_node = None

    # Retorna o resultado com as informações sobre o caminho, custo e estatísticas do algoritmo.
    return Result(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,  # Caminho encontrado ou erro.
        "+Infinity" if result_node == None else result_node.accumulate_cost,  # Custo acumulado.
        generate_node_count,  # Número de nós gerados.
        len(visited),  # Número de estados visitados.
        "A_Star",  # Nome do algoritmo.
        verbose  # Flag para exibir informações adicionais.
    )

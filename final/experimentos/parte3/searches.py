from result import Result
from node import Node
from queue import PriorityQueue

# [ Search algorithms ]

# Essa função deve rodar antes do início de cada algorítmo de busca. Ela
# garante que as posicões inical e de objetivos não estejam fora da borda do
# mapa.
def search_function_prelude(inital_pos, objective_pos):
    if not Node(inital_pos).is_valid():
        raise Exception(f"Invalid inital state -> {inital_pos}")
    if not Node(objective_pos).is_valid():
        raise Exception(f"Invalid objective state -> {objective_pos}")

def Greedy(inital_pos, objective_pos, verbose=False) -> Result:
    # Roda o prelúdio de busca
    search_function_prelude(inital_pos, objective_pos)

    # Lista para rastrear os nós visitados
    visited = []
    # Contador para o número de nós gerados durante a busca
    generate_node_count = 1
    # Variável para armazenar o nó resultado, caso o objetivo seja alcançado
    result_node = None

    # Inicializa a busca a partir do nó inicial
    current = Node(inital_pos)
    while True:
        # Caso em que o objetivo é encontrado
        if current.pos == objective_pos:
            visited.append(current)  # Marca o nó atual como visitado
            result_node = current  # Armazena o nó objetivo
            current = None  # Encerra a busca
            break

        # Obtém os vizinhos do nó atual, ordenados pela função heurística
        neighbors = sorted(current.get_neighbors(), 
                           key=lambda x: x.get_heuristic_value(Node(objective_pos)))
        generate_node_count += len(neighbors)  # Incrementa o contador de nós gerados

        # Filtra os vizinhos para remover aqueles já visitados
        neighbors = list(filter(lambda x: x.pos not in visited, neighbors))

        # Caso em que nenhum caminho é encontrado
        if len(neighbors) == 0:
            current = None  # Encerra a busca
            break

        # Marca o nó atual como visitado
        visited.append(current.pos)

        # Seleciona o vizinho com menor custo de função heurística
        current = neighbors[0]

    # Retorna o resultado da busca com as informações relevantes
    return Result(
        inital_pos,  # Posição inicial
        objective_pos,  # Posição objetivo
        "Error" if result_node == None else result_node.path,  # Caminho encontrado ou erro
        "+Infinity" if result_node == None else result_node.accumulate_cost,  # Custo acumulado ou infinito
        generate_node_count,  # Número de nós gerados
        len(visited),  # Número de nós visitados
        "Greedy",  # Nome do algoritmo
        verbose  # Modo verboso
    )

# Busca A*
def A_Star(inital_pos, objective_pos, verbose=False) -> Result:
    # Roda o prelúdio de busca
    search_function_prelude(inital_pos, objective_pos)

    # Ativa o modo de comparação A* nos nós
    Node.use_a_star_compration = True
    # Define o nó objetivo para o cálculo da heurística
    Node.a_start_objective_node = Node(objective_pos)

    # Inicializa a fila de prioridade para os nós a serem explorados
    # Como a comparação para A* cada nó vai ser comparado pelo custo
    # acumulado + a heurística utilizada
    queue = PriorityQueue()
    queue.put(Node(inital_pos))  # Adiciona o nó inicial à fila

    # Lista para armazenar os estados visitados
    visited = []
    # Contador para o número de nós gerados durante a busca
    generate_node_count = 1
    # Variável para armazenar o nó resultante (se encontrado)
    result_node = None

    # Loop principal de exploração
    while not queue.empty():
        # Retira o nó com maior prioridade (custo acumulado + heurística) da fila
        current_node = queue.get()

        # Ignora o nó atual se ele já foi visitado
        if current_node.pos in visited:
            continue

        # Verifica se o nó atual é o objetivo
        if current_node.pos == objective_pos:
            visited.append(current_node)  # Marca o nó como visitado
            result_node = current_node  # Define o nó atual como o resultado
            break  # Encerra a busca

        # Itera sobre os vizinhos do nó atual
        for neighbor in current_node.get_neighbors():
            # Incrementa o contador de nós gerados
            generate_node_count += 1
            # Adiciona o vizinho na fila se ele ainda não foi visitado
            if not neighbor.pos in visited:
                queue.put(neighbor)

        # Marca o nó atual como visitado
        visited.append(current_node.pos)

    # Desativa o modo de comparação A* nos nós 
    Node.use_a_star_compration = False
    Node.a_start_objective_node = None

    # Retorna os resultados da busca
    return Result(
        inital_pos,  # Posição inicial
        objective_pos,  # Posição objetivo
        "Error" if result_node == None else result_node.path,  # Caminho ou erro
        "+Infinity" if result_node == None else result_node.accumulate_cost,  # Custo ou infinito
        generate_node_count,  # Número de nós gerados
        len(visited),  # Número de nós visitados
        "A_Star",  # Nome do algoritmo
        verbose  # Flag de verbosidade
    )

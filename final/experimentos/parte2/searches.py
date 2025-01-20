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

# Busca de Custo Uniforme
def UCS(inital_pos, objective_pos, verbose=False) -> Result:
    # Roda o prelúdio de busca
    search_function_prelude(inital_pos, objective_pos)

    # Inicializa uma fila de prioridade para os nós a serem explorados
    queue = PriorityQueue()
    # Adiciona o nó inicial na fila de prioridade
    # A comparação dos nós é feita internamente pelas fuções __gt__ e __lt__.
    # a métrica de comparação é o custo acumulativo até o nó em questão
    queue.put(Node(inital_pos))

    # Lista para armazenar os estados visitados
    visited = []
    # Contador para o número de nós gerados, começando com o nó inicial
    generate_node_count = 1
    # Variável para armazenar o nó resultado da busca
    result_node = None

    # Loop principal da busca
    # Executa enquanto a fila de prioridade não estiver vazia
    while not queue.empty():
        # Remove o nó com a menor prioridade (custo acumulado mais baixo)
        current_node = queue.get()

        # Se o nó já foi visitado, ignora e passa para o próximo
        if current_node.pos in visited:
            continue

        # Verifica se o nó atual é o objetivo
        if current_node.pos == objective_pos:
            # Se for o objetivo, adiciona à lista de visitados, define o resultado e termina
            visited.append(current_node)
            result_node = current_node
            break

        # Explora os vizinhos do nó atual
        for neighbor in current_node.get_neighbors():
            # Adiciona os vizinhos na fila se ainda não foram visitados
            if not neighbor.pos in visited:
                generate_node_count += 1  # Incrementa o contador de nós gerados
                queue.put(neighbor)      # Adiciona o vizinho na fila de prioridade

        # Adiciona o nó atual à lista de visitados
        visited.append(current_node.pos)

    # Retorna o resultado da busca com informações como caminho, custo acumulado
    # e métricas
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

from result import Result
from node import Node
from node_a_star import Node_A_Star
from queue import PriorityQueue
from result_a_star_with_stop import Result_A_Star_With_Stop

# [ Algorítmos de busca ]

# Essa função deve rodar antes do início de cada algorítmo de busca. Ela
# garante que as posicões inical e de objetivos não estejam fora da borda do
# mapa.
def search_function_prelude(inital_pos, objective_pos):
    if not Node(inital_pos).is_valid():
        raise Exception(f"Invalid inital state -> {inital_pos}")
    if not Node(objective_pos).is_valid():
        raise Exception(f"Invalid objective state -> {objective_pos}")

# Busca Em Profundiade
def DFS(inital_pos, objective_pos, verbose=False) -> Result:
    # Roda o prelúdio de busca
    search_function_prelude(inital_pos, objective_pos)

    # Inicia a stack de busca com nó inicia
    stack = [Node(inital_pos)]
    # Vetor que guarda os estado visistados
    visited = []
    # Número de nós visitados considerando o nó inicial
    generate_node_count = 1 
    # Nó resultado. Se não for atribuido nenhum nó a ele, então a busca
    # falhou
    result_node = None

    # Loop de exploração
    # Roda enquanto ainda tem elementos na pilha de busca
    while len(stack) > 0:
        # Retira o elemento no topo da stack
        current_node = stack.pop()

        # Se o nó já tiver sido visitado, então ele não precisa ser
        # explorado
        if current_node.pos in visited:
            continue

        # Se for o objetivo, adiciona à lista de visitados, define o resultado e
        # termina
        if current_node.pos == objective_pos:
            visited.append(current_node)
            result_node = current_node
            break

        # Explorar o nó atual colocando seus vizinhos na pilha de exploração
        for neighbor in current_node.get_neighbors():
            # Para todo vizinho, se ele não tiver sido visitado, então
            # coloque ele na pilha e conte mais um nó gerado
            if not neighbor.pos in visited:
                generate_node_count += 1
                stack.append(neighbor)

        # Adicionar nó atual na lista de visitados
        visited.append(current_node.pos)

    # O resultado da busca é retornado
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

# Busca em Largura
def BFS(inital_pos, objective_pos, verbose=False) -> Result:
    # Roda o prelúdio de busca
    search_function_prelude(inital_pos, objective_pos)

    # Inicializa a fila de busca com o nó inicial
    queue = [Node(inital_pos)]
    # Lista para armazenar os estados visitados
    visited = []
    # Contador para o número de nós gerados, começando com o nó inicial
    generate_node_count = 1
    # Variável para armazenar o nó resultado da busca
    result_node = None

    # Loop principal da busca em largura
    # Executa enquanto há elementos na fila
    while len(queue) > 0:
        # Remove o elemento na frente da fila
        current_node = queue.pop(0)

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
                queue.append(neighbor)

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
        "BFS",                
        verbose               
    )

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


# Algoritmo A*
def A_Star_With_Stop(inital_pos, objective_pos, verbose=False) -> Result:
    # Pré-condição para garantir que os estados inicial e objetivo sejam válidos.
    search_function_prelude(inital_pos, objective_pos)

    # Define o estado objetivo, com um valor booleano se o nó já passou em
    # uma farmácia
    objective_state = (*objective_pos, True)

    # Ativa o uso de comparação A* nos nós e define o nó objetivo para cálculo de heurística.
    Node_A_Star.use_a_star_compration = True
    Node_A_Star.a_start_objective_node = Node_A_Star(objective_pos)

    # Inicializa a fila de prioridade para o algoritmo A*.
    queue = PriorityQueue()
    queue.put(Node_A_Star((*inital_pos, False)))  # Adiciona o nó inicial na fila.

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

    # Restaura as configurações padrão da classe Node_A_Star após a execução do algoritmo.
    Node_A_Star.use_a_star_compration = False
    Node_A_Star.a_start_objective_node = None

    # Retorna o resultado com as informações sobre o caminho, custo e estatísticas do algoritmo.
    return Result_A_Star_With_Stop(
        inital_pos,
        objective_pos,
        "Error" if result_node == None else result_node.path,  # Caminho encontrado ou erro.
        "+Infinity" if result_node == None else result_node.accumulate_cost,  # Custo acumulado.
        generate_node_count,  # Número de nós gerados.
        len(visited),  # Número de estados visitados.
        "A_Star",  # Nome do algoritmo.
        verbose  # Flag para exibir informações adicionais.
    )

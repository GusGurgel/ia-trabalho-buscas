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

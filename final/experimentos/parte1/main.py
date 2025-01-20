import random
from os.path import realpath, dirname, join
from node import Node
from result import Result
from searches import BFS, DFS, UCS

if __name__ == "__main__":
    # Lista para armazenar os pares de objetivos de busca (início e objetivo)
    search_objectives = []

    # Gera 50 pares únicos de posições iniciais e objetivos de busca
    while len(search_objectives) < 50:
        starting = (random.randint(0, 30), random.randint(0, 30))  # Posição inicial aleatória
        objective = (random.randint(0, 30), random.randint(0, 30))  # Posição objetivo aleatória
        search_objective = (starting, objective)  # Cria o par (início, objetivo)

        # Garante que o par gerado não seja duplicado
        if search_objective not in search_objectives:
            search_objectives.append(search_objective)

    # Lista de funções de custo que podem ser usadas para a busca
    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    # Lista das buscas disponíveis, associadas a seus respectivos nomes
    SEARCHES = [("BFS", BFS), ("DFS", DFS), ("UCS", UCS)]
    # Caminho onde os resultados serão salvos
    SAVE_PATH = join(dirname(realpath(__file__)), "resultado")

    # Itera sobre cada algoritmo de busca disponível
    for search_name, search_function in SEARCHES:
        print(f"running {search_name}...")  # Indica qual algoritmo está sendo executado
        results = []  # Lista para armazenar os resultados da busca

        # Itera sobre cada par de posições iniciais e objetivos
        for search_objective in search_objectives:
            # Itera sobre cada função de custo definida
            for cost_function in COST_FUNCTIONS:
                Node.cost_function = cost_function  # Define a função de custo atual no nó
                # Executa a busca e armazena o resultado na lista de resultados
                results.append(search_function(
                    search_objective[0],  # Posição inicial
                    search_objective[1]   # Posição objetivo
                ))
        
        # Salva os resultados em um arquivo CSV com o nome correspondente ao algoritmo
        print(f"Saving result{search_name}.csv")
        Result.saveResultsAsCSV(results, join(SAVE_PATH, f"resultado{search_name}.csv"))

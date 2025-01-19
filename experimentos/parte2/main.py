import random
from os.path import realpath, dirname, join
from node import Node
from result import Result
from searches import UCS, A_Star

if __name__ == "__main__":
    # Lista que armazenará os objetivos das buscas
    search_objectives = []

    # Gera 50 pares únicos de posições iniciais e objetivos
    while len(search_objectives) < 50:
        starting = (random.randint(0, 30), random.randint(0, 30))  # Gera posição inicial aleatória
        objective = (random.randint(0, 30), random.randint(0, 30))  # Gera posição objetivo aleatória
        search_objective = (starting, objective)

        # Adiciona o par gerado à lista, se ainda não estiver presente
        if search_objective not in search_objectives:
            search_objectives.append(search_objective)
        
    # Define as funções de custo disponíveis
    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    # Define as funções heurísticas disponíveis para o A*
    HEURISTIC_FUNCTIONS = ["h1", "h2"]
    # Define os algoritmos de busca a serem executados
    SEARCHES = [("UCS", UCS), ("A_Star", A_Star)]
    # Caminho para salvar os resultados
    SAVE_PATH = join(dirname(realpath(__file__)), "resultado")

    # Loop principal que executa cada algoritmo de busca
    for search_name, search_function in SEARCHES:
        print(f"running {search_name}...")  # Indica o início da execução do algoritmo
        results = []  # Lista para armazenar os resultados do algoritmo atual

        # Itera sobre cada objetivo de busca gerado
        for search_objective in search_objectives:
            # Itera sobre todas as funções de custo
            for cost_function in COST_FUNCTIONS:
                # Se o algoritmo atual for A*, também itera sobre as funções heurísticas
                if search_name == "A_Star":
                    for heuristic_function in HEURISTIC_FUNCTIONS:
                        Node.heuristic_function = heuristic_function  # Define a função heurística
                        Node.cost_function = cost_function  # Define a função de custo
                        # Executa a busca e armazena o resultado
                        results.append(search_function(
                            search_objective[0],  # Posição inicial
                            search_objective[1]   # Posição objetivo
                        ))
                else:
                    # Para outros algoritmos, apenas define a função de custo
                    Node.cost_function = cost_function
                    # Executa a busca e armazena o resultado
                    results.append(search_function(
                        search_objective[0],  # Posição inicial
                        search_objective[1]   # Posição objetivo
                    ))

        # Salva os resultados do algoritmo atual em um arquivo CSV
        print(f"Saving result{search_name}.csv")
        Result.saveResultsAsCSV(results, join(SAVE_PATH, f"resultado{search_name}.csv"))

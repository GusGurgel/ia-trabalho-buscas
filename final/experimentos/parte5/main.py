import random
from os.path import realpath, dirname, join
from node import Node
from result import Result
from searches import A_Star
from settings import *

if __name__ == "__main__":
    # Cada objetivo de busca é uma trípla de 
    # (posição_inicial, posição_final, farmácias disponíveis)
    search_objectives = [] 

    # Gerando nós objetivos de busca
    while len(search_objectives) < 25:
        pharmacies = []

        # Gerar conjunto de 4 farmácias em posições aleatórias
        while len(pharmacies) < 4:
            pharmacy_position = (random.randint(0, 30), random.randint(0, 30))  # Gera posição aleatória para farmácia
            if pharmacy_position not in pharmacies:
                pharmacies.append(pharmacy_position)  # Adiciona a posição ao conjunto de farmácias se não estiver presente

        starting = (random.randint(0, 30), random.randint(0, 30))  # Gera posição inicial aleatória
        objective = (random.randint(0, 30), random.randint(0, 30))  # Gera posição objetivo aleatória
        search_objective = (starting, objective, pharmacies)

        if search_objective not in search_objectives:
            search_objectives.append(search_objective)  # Adiciona o objetivo de busca à lista se não for duplicado

    # Funções de custo e heurísticas disponíveis para os nós
    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    HEURISTIC_FUNCTIONS = ["h1", "h2"]

    # Algoritmos de busca a serem executados
    SEARCHES = [("A_Star", A_Star)]

    # Caminho para salvar os resultados
    SAVE_PATH = join(dirname(realpath(__file__)), "resultado")

    # Loop pelos algoritmos de busca
    for search_name, search_function in SEARCHES:
        print(f"running {search_name}...")  # Exibe o nome do algoritmo que está sendo executado
        results = []

        # Itera pelos objetivos de busca
        for inital_pos, objective_pos, pharmacies in search_objectives:
            Node.pharmacy_positions = pharmacies  # Define as posições das farmácias no nó

            # Itera pelas funções heurísticas
            for heuristic_function in HEURISTIC_FUNCTIONS:
                Node.heuristic_function = heuristic_function  # Define a função heurística a ser usada

                # Itera pelas funções de custo
                for cost_function in COST_FUNCTIONS:
                    Node.cost_function = cost_function  # Define a função de custo a ser usada

                    # Executa o algoritmo de busca e armazena o resultado
                    results.append(search_function(
                        inital_pos,
                        objective_pos
                    ))

        # Salva os resultados no formato CSV
        print(f"Saving result{search_name}.csv")
        Result.saveResultsAsCSV(results, join(SAVE_PATH, f"resultado{search_name}.csv"))

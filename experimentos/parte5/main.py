import random
from os.path import realpath, dirname, join
from node import Node
from result import Result
from searches import A_Star
from settings import *

if __name__ == "__main__":
    # Cada objetivo de busca é uma trípla de 
    # (posição_inicial, posição_final, framácias disponíveis)
    search_objectives = [] 

    # Gerando nós objetivos de busca
    while len(search_objectives) < 25:
        pharmacies = []

        # Gerar conjunto de 4 framácias em posições aleatórias
        while len(pharmacies) < 4:
            pharmacy_position = (random.randint(0, 30), random.randint(0, 30))
            if pharmacy_position not in pharmacies:
                pharmacies.append(pharmacy_position)

        starting = (random.randint(0, 30), random.randint(0, 30))
        objective = (random.randint(0, 30), random.randint(0, 30))
        search_objective = (starting, objective, pharmacies)

        if search_objective not in search_objectives:
            search_objectives.append(search_objective)
    
        
    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    HEURISTIC_FUNCTIONS = ["h1", "h2"]
    SEARCHES = [("A_Star", A_Star)]
    SAVE_PATH = join(dirname(realpath(__file__)), "resultado")

    for search_name, search_function in SEARCHES:
        print(f"running {search_name}...")
        results = []
        for inital_pos, objective_pos, pharmacies in search_objectives:
            Node.pharmacy_positions = pharmacies
            for heuristic_function in HEURISTIC_FUNCTIONS:
                Node.heuristic_function = heuristic_function
                for cost_function in COST_FUNCTIONS:
                    Node.cost_function = cost_function
                    results.append(search_function(
                        inital_pos,
                        objective_pos
                    ))
        print(f"Saving result{search_name}.csv")
        Result.saveResultsAsCSV(results, join(SAVE_PATH, f"resultado{search_name}.csv"))
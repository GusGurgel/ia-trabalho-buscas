import random
import copy
from os.path import realpath, dirname, join
from searches import BFS, DFS
from result import Result
from node import Node

if __name__ == "__main__":
    search_objectives = []

    while len(search_objectives) < 20:
        starting = (random.randint(0, 30), random.randint(0, 30))
        objective = (random.randint(0, 30), random.randint(0, 30))
        search_objective = (starting, objective)

        if search_objective not in search_objectives:
            search_objectives.append(search_objective)
        
    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    SEARCHES = [("BFS",BFS), ("DFS",DFS)]
    SAVE_PATH = join(dirname(realpath(__file__)), "resultado")

    for search_name, search_function in SEARCHES:
        print(f"running {search_name}...")
        results = []
        for search_objective in search_objectives:
            for i in range(1, 21):
                result, result_node = search_function(
                    search_objective[0],
                    search_objective[1]
                )
                for cost_function in COST_FUNCTIONS:
                    result_copy = copy.deepcopy(result)
                    result_copy.execution_number = i
                    result_copy.cost = result_node.get_cost_with_cost_function(cost_function)
                    result_copy.cost_function = cost_function
                    result_copy.verbose = True
                    results.append(result_copy)
        print(f"Saving result{search_name}.csv")
        Result.saveResultsAsCSV(results, join(SAVE_PATH, f"resultado{search_name}.csv"))
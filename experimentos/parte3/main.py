import random
from os.path import realpath, dirname, join
from node import Node
from result import Result
from searches import UCS, A_Star

if __name__ == "__main__":
    search_objectives = []

    while len(search_objectives) < 50:
        starting = (random.randint(0, 30), random.randint(0, 30))
        objective = (random.randint(0, 30), random.randint(0, 30))
        search_objective = (starting, objective)

        if search_objective not in search_objectives:
            search_objectives.append(search_objective)
        
    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    HEURISTIC_FUNCTIONS = ["h1", "h2"]
    SEARCHES = [("UCS",UCS), ("A_Star", A_Star)]
    SAVE_PATH = join(dirname(realpath(__file__)), "resultado")

    for search_name, search_function in SEARCHES:
        print(f"running {search_name}...")
        results = []
        for search_objective in search_objectives:
            for cost_function in COST_FUNCTIONS:
                    for heuristic_function in HEURISTIC_FUNCTIONS:
                        Node.heuristic_function = heuristic_function
                        Node.cost_function = cost_function
                        results.append(search_function(
                            search_objective[0],
                            search_objective[1]
                        ))

        print(f"Saving result{search_name}.csv")
        Result.saveResultsAsCSV(results, join(SAVE_PATH, f"resultado{search_name}.csv"))
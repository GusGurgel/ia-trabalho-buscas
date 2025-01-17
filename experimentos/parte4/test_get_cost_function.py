# Para essa etapa do projeto foi necessário implementar uma função separada
# para pegar o custo do caminho usando uma determinada função de custo. Esse
# arquivo é dedicado a um bateria de testes para provar que a nova função de
# calcular custo bate com a que estava sendo usado anteriormente.

import random
from os.path import realpath, dirname, join
from node import Node
from searches import BFS, DFS

def testGetCostFunction():
    search_objectives = []

    while len(search_objectives) < 50:
        starting = (random.randint(0, 30), random.randint(0, 30))
        objective = (random.randint(0, 30), random.randint(0, 30))
        search_objective = (starting, objective)

        if search_objective not in search_objectives:
            search_objectives.append(search_objective)

    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    SEARCHES = [("BFS",BFS), ("DFS",DFS)]

    index = 0
    for search_name, search_function in SEARCHES:
        for search_objective in search_objectives:
            for cost_function in COST_FUNCTIONS:
                index += 1
                Node.cost_function = cost_function
                result, result_node = search_function(
                    search_objective[0],
                    search_objective[1]
                )
                cost_with_function = result_node.get_cost_with_cost_function(cost_function)

                assert cost_with_function == result.cost
                print(f"test {index} 🆗 {result.cost} == {cost_with_function}")

if __name__ == "__main__":
    testGetCostFunction()
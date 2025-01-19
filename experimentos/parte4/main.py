import random
import copy
from os.path import realpath, dirname, join
from searches import BFS, DFS
from result import Result
from node import Node

# Ponto de entrada principal do script
if __name__ == "__main__":
    search_objectives = []  # Lista para armazenar os pares de estado inicial e objetivo

    # Gera 20 pares únicos de estados iniciais e objetivos
    while len(search_objectives) < 20:
        starting = (random.randint(0, 30), random.randint(0, 30))  # Estado inicial aleatório
        objective = (random.randint(0, 30), random.randint(0, 30))  # Estado objetivo aleatório
        search_objective = (starting, objective)  # Combinação de estado inicial e objetivo

        # Adiciona o par gerado apenas se for único
        if search_objective not in search_objectives:
            search_objectives.append(search_objective)
        
    # Lista de funções de custo a serem aplicadas
    COST_FUNCTIONS = ["c1", "c2", "c3", "c4"]
    # Lista de algoritmos de busca e suas referências
    SEARCHES = [("BFS", BFS), ("DFS", DFS)]
    # Caminho para salvar os arquivos de resultado
    SAVE_PATH = join(dirname(realpath(__file__)), "resultado")

    # Itera sobre cada algoritmo de busca
    for search_name, search_function in SEARCHES:
        print(f"running {search_name}...")  # Indica o início do processamento do algoritmo
        results = []  # Lista para armazenar os resultados das buscas

        # Itera sobre cada par de objetivo de busca
        for search_objective in search_objectives:
            # Executa a busca 20 vezes para cada par de objetivo
            for i in range(1, 21):
                # Executa a função de busca para o estado inicial e objetivo
                result, result_node = search_function(
                    search_objective[0],
                    search_objective[1]
                )

                # Aplica cada função de custo aos resultados
                for cost_function in COST_FUNCTIONS:
                    result_copy = copy.deepcopy(result)  # Cria uma cópia do resultado
                    result_copy.execution_number = i  # Número da execução atual
                    # Calcula o custo com base na função de custo atual
                    result_copy.cost = result_node.get_cost_with_cost_function(cost_function)
                    result_copy.cost_function = cost_function  # Define a função de custo usada
                    result_copy.verbose = True  # Ativa a exibição detalhada
                    results.append(result_copy)  # Adiciona o resultado à lista

        # Salva os resultados em um arquivo CSV
        print(f"Saving result{search_name}.csv")
        Result.saveResultsAsCSV(results, join(SAVE_PATH, f"resultado{search_name}.csv"))
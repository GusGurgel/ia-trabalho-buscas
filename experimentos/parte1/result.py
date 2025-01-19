from node import *
import csv

# Constante que define os campos do cabeçalho para o arquivo CSV de resultados
RESULT_CSV_FIELDS = [[
    "Inital State",       # Estado inicial da busca
    "Search Objective",   # Objetivo da busca
    "Path",               # Caminho percorrido na busca
    "Cost",               # Custo total do caminho
    "Generated Nodes",    # Número de nós gerados
    "Visited Nodes",      # Número de nós visitados
    "Algorithm",          # Algoritmo usado (e.g., UCS, A*)
    "Cost Function",      # Função de custo utilizada
    "Heuristic"           # Função heurística utilizada (se aplicável)
]]

# Representa o resultado de uma busca
class Result:
    # Método estático para salvar um array de objetos Result em um arquivo CSV
    @staticmethod
    def saveResultsAsCSV(arr, path="result.csv"):
        with open(path, 'w', newline='') as file:
            arr = map(lambda x: x.as_array(), arr)  # Converte cada resultado para um array
            writer = csv.writer(file)
            # Escreve o cabeçalho no arquivo
            writer.writerows(RESULT_CSV_FIELDS)
            # Escreve os resultados no arquivo
            writer.writerows(arr)

    # Inicializador da classe Result
    def __init__(self, initial_state, search_objective, path, cost, gen_nodes, 
                 visit_nodes, algorithm=None, verbose=False):
        self.initial_state = initial_state  # Estado inicial da busca
        self.search_objective = search_objective  # Objetivo da busca
        self.path = path  # Caminho resultante da busca
        self.cost = cost  # Custo do caminho
        self.gen_nodes = gen_nodes  # Número de nós gerados
        self.visit_nodes = visit_nodes  # Número de nós visitados
        self.algorithm = algorithm  # Nome do algoritmo utilizado
        self.cost_function = Node.cost_function  # Função de custo utilizada
        self.heuristic = Node.heuristic_function  # Função heurística utilizada (se aplicável)
        self.verbose = verbose  # Indica se informações adicionais devem ser exibidas

    # Retorna os atributos da instância como uma lista (para salvar no CSV)
    def as_array(self):
        return [
            self.initial_state,      # Estado inicial
            self.search_objective,   # Objetivo da busca
            self.path,               # Caminho
            self.cost,               # Custo
            self.gen_nodes,          # Nós gerados
            self.visit_nodes,        # Nós visitados
            self.algorithm,          # Algoritmo
            self.cost_function,      # Função de custo
            self.heuristic           # Função heurística
        ]

    # Representação em string para exibição dos resultados no console
    def __str__(self):
        res = f"""Inital State: {self.initial_state}
Search Objective: {self.search_objective}
Path: {self.path}
Path Cost: {self.cost}
Count Nodes Genereted: {self.gen_nodes}
Count Nodes Visited: {self.visit_nodes}
"""
        # Adiciona informações extras se o verbose estiver ativado
        if self.verbose:
            res += f"""Algorithm: {self.algorithm}
Cost Function: {self.cost_function}
Heuristic: {self.heuristic}
"""
        return res

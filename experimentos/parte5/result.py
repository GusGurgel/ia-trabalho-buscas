from node import *
import csv

# Campos para o cabeçalho do arquivo CSV que armazenará os resultados
RESULT_CSV_FIELDS = [[
    "Inital State",
    "Search Objective",
    "Pharmacy Positions",
    "Path",
    "Cost",
    "Generated Nodes",
    "Visited Nodes",
    "Algorithm",
    "Cost Function",
    "Heuristic"
]]

# Classe que representa o resultado de uma busca
class Result:
    # Método para salvar os resultados como um arquivo CSV
    def saveResultsAsCSV(arr, path="result.csv"):
        with open(path, 'w', newline='') as file:
            arr = map(lambda x : x.as_array(), arr)  # Converte os resultados para o formato de array
            writer = csv.writer(file)
            # Escreve o cabeçalho no arquivo CSV
            writer.writerows(RESULT_CSV_FIELDS)
            # Escreve as linhas correspondentes aos resultados
            writer.writerows(arr)

    # Construtor da classe Result
    def __init__(self, initial_state, search_objective, path, cost, gen_nodes, 
                 visit_nodes, algorithm=None, verbose = False):
        self.initial_state = initial_state  # Estado inicial da busca
        self.search_objective = search_objective  # Objetivo da busca
        self.path = path  # Caminho encontrado durante a busca
        self.cost = cost  # Custo total do caminho encontrado
        self.gen_nodes = gen_nodes  # Quantidade de nós gerados
        self.visit_nodes = visit_nodes  # Quantidade de nós visitados
        self.algorithm = algorithm  # Algoritmo utilizado na busca
        self.cost_function = Node.cost_function  # Função de custo utilizada
        self.heuristic = Node.heuristic_function  # Função heurística utilizada
        self.pharmacy_positions = Node.pharmacy_positions.copy()  # Cópia das posições das farmácias
        self.verbose = verbose  # Define se informações adicionais serão exibidas

    # Método para converter os atributos do resultado para um array
    def as_array(self):
        return [
            self.initial_state,  # Estado inicial da busca
            self.search_objective,  # Objetivo da busca
            self.pharmacy_positions,  # Posições das farmácias
            self.path,  # Caminho encontrado
            self.cost,  # Custo total
            self.gen_nodes,  # Nós gerados
            self.visit_nodes,  # Nós visitados
            self.algorithm,  # Algoritmo utilizado
            self.cost_function,  # Função de custo
            self.heuristic  # Função heurística
        ]
        
    # Método para converter o resultado para uma string formatada
    def __str__(self):
        res = f"""Inital State: {self.initial_state}
Search Objective: {self.search_objective}
Pharmacy Positions: {self.pharmacy_positions}
Path: {self.path}
Path Cost: {self.cost}
Count Nodes Genereted: {self.gen_nodes}
Count Nodes Visited: {self.visit_nodes}
"""
        if self.verbose:  # Adiciona informações adicionais se verbose estiver habilitado
            res += f"""Algorithm: {self.algorithm}
Cost Function: {self.cost_function}
Heuristic: {self.heuristic}
"""
        return res

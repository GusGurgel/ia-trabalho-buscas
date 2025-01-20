import time
from node import Node
from node_a_star import Node_A_Star
from searches import DFS, BFS, UCS, Greedy, A_Star, A_Star_With_Stop

def get_algorithm_choice():
    algorithms = ["DFS", "BFS", "UCS", "Greedy", "A_Star", "A_Star_With_Stop"]
    while True:
        print("Escolha o algoritmo de busca:")
        for i, algo in enumerate(algorithms, start=1):
            print(f"{i}. {algo}")
        try:
            choice = int(input("Digite o número correspondente: "))
            if 1 <= choice <= len(algorithms):
                return algorithms[choice - 1]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def get_cost_function():
    cost_functions = ["c1", "c2", "c3", "c4"]
    while True:
        print("Escolha a função de custo (c1, c2, c3, c4):")
        cost = input("Digite a função de custo: ").strip()
        if cost in cost_functions:
            return cost
        else:
            print("Função de custo inválida. Tente novamente.")

def get_heuristic_function():
    heuristic_functions = ["h1", "h2"]
    while True:
        print("Escolha a função heurística (h1, h2):")
        heuristic = input("Digite a função heurística: ").strip()
        if heuristic in heuristic_functions:
            return heuristic
        else:
            print("Função heurística inválida. Tente novamente.")

def get_pharmacy_positions():
    while True:
        try:
            print("Digite as posições das farmácias no formato x,y (máximo 4, separadas por espaço):")
            positions = input("Digite as posições: ").strip()
            positions = [tuple(map(int, pos.split(","))) for pos in positions.split()]
            if len(positions) <= 4:
                return positions
            else:
                print("Número de farmácias excede o limite de 4. Tente novamente.")
        except ValueError:
            print("Formato inválido. Tente novamente usando o formato x,y.")

def get_position(prompt):
    while True:
        try:
            print(f"{prompt} (valores válidos: entre 0 e 30):")
            x, y = map(int, input("Digite a posição no formato x,y: ").strip().split(","))
            if 0 <= x <= 30 and 0 <= y <= 30:
                return (x, y)
            else:
                print("Posição fora dos limites válidos. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Use o formato x,y com números inteiros.")

def main():
    print("Aplicação CLI para encontrar caminhos em um grafo.")
    algorithm = get_algorithm_choice()

    start_position = get_position("Digite a posição inicial")
    goal_position = get_position("Digite a posição objetivo")
    Node.cost_function = get_cost_function()
    Node_A_Star.cost_function = Node.cost_function

    if algorithm in ["Greedy", "A_Star", "A_Star_With_Stop"]:
        Node.heuristic_function = get_heuristic_function()
        Node_A_Star.heuristic_function = Node.heuristic_function

    if algorithm == "A_Star_With_Stop":
        Node_A_Star.pharmacy_positions = get_pharmacy_positions()

    allow_repeated_states = True

    algorithm_function = {
        "DFS": DFS,
        "BFS": BFS,
        "UCS": UCS,
        "Greedy": Greedy,
        "A_Star": A_Star,
        "A_Star_With_Stop": A_Star_With_Stop,
    }[algorithm]

    print(f"Executando o algoritmo {algorithm}...")
    start_time = time.time()
    result = algorithm_function(start_position, goal_position, allow_repeated_states)
    end_time = time.time()

    print("\nResultado da busca:")
    print(result)
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()

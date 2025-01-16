import random
from node import Node
from main import BFS, DFS, UCS
from result import Result


def verify_tuple_is_in_array(array, tuple):
    for i in array:
        if i[0] == tuple[0] and i[1] == tuple[1]:
            return True
    return False

if __name__ == "__main__":
    starting_points = []
    destinations = []
    resultsBFS = []
    resultsDFS = []
    resultsUCS = []

    while len(starting_points) < 50:
        starting = (random.randint(0, 30), random.randint(0, 30))
        destination = (random.randint(0, 30), random.randint(0, 30))
        if not verify_tuple_is_in_array(starting_points, starting) and not verify_tuple_is_in_array(destinations, destination):
            starting_points.append(starting)
            destinations.append(destination)
        
    print('Starting points:', len(starting_points))
    print('Destinations:', len(destinations))
            
    Node.heuristic_function = "h1"

    print('BFS')
    for starting in starting_points:
        Node.cost_function = "c1"
        r1 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r1)
        Node.cost_function = "c2"
        r2 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r2)
        Node.cost_function = "c3"
        r3 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r3)
        Node.cost_function = "c4"
        r4 = BFS(starting, destinations[starting_points.index(starting)], False)
        resultsBFS.append(r4)

    print('DFS')
    for starting in starting_points:
        Node.cost_function = "c1"
        r1 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r1)
        Node.cost_function = "c2"
        r2 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r2)
        Node.cost_function = "c3"
        r3 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r3)
        Node.cost_function = "c4"
        r4 = DFS(starting, destinations[starting_points.index(starting)], False)
        resultsDFS.append(r4)

    print('UCS')
    for starting in starting_points:
        Node.cost_function = "c1"
        r1 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r1)
        Node.cost_function = "c2"
        r2 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r2)
        Node.cost_function = "c3"
        r3 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r3)
        Node.cost_function = "c4"
        r4 = UCS(starting, destinations[starting_points.index(starting)], False)
        resultsUCS.append(r4)
    
    print('Saving resultBFS')
    Result.saveResultsAsCSV(resultsBFS, "resultBFS.csv")
    print('Saving resultDFS')
    Result.saveResultsAsCSV(resultsDFS, "resultDFS.csv" )
    print('Saving resultUCS')
    Result.saveResultsAsCSV(resultsUCS, "resultUCS.csv")
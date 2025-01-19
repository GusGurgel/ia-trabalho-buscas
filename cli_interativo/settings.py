MAP_SIZE = (30, 30)  # cols x rows

F1 = lambda pos: (pos[0] - 1, pos[1])
F2 = lambda pos: (pos[0] + 1, pos[1])
F3 = lambda pos: (pos[0], pos[1] - 1)
F4 = lambda pos: (pos[0], pos[1] + 1)

ACTIONS = [F1, F2, F3, F4]
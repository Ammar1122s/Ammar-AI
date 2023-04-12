from queue import Queue

# define the initial and goal states of the puzzle
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# define the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# define a function to get the next state given the current state and a move
def get_next_state(state, move):
    row, col = get_blank_position(state)
    next_state = [row[:] for row in state]
    print(next_state)
    next_row = row + move[0]
    next_col = col + move[1]
   # next_state[row][col], next_state[next_row][next_col] = next_state[next_row][next_col], next_state[row][col]
    return next_state

# define a function to get the position of the blank tile (0)
def get_blank_position(state):
    for row in range(3):
        for col in range(3):        
            if state[row][col] == 0:
                return row, col

# define the BFS algorithm
def bfs(initial_state, goal_state):
    queue = Queue()
    queue.put((initial_state, []))
    visited = set()
    
    while not queue.empty():
        state, path = queue.get()
        print(state)
        if state == goal_state:
            return path
        visited.add(str(state))
        for move in moves:
            next_state = get_next_state(state, move)
            if str(next_state) not in visited:
                queue.put((next_state, path + [move]))
                
    return None

# solve the puzzle
solution = bfs(initial_state, goal_state)

if solution:
    print("Solution found in", len(solution), "moves:", solution)
else:
    print("Solution not found")

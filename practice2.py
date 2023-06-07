my_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B", "H"],
    "E": ["B", "H"],
    "F": ["C", "H"],
    "H": ["D", "E", "F", "G"],
    "G": ["C", "H"]
}

opened = []
closed = []
backtrack = []

opened.append(("A", 1))  # start node is A, set depth as 1
searchNode = "H"

# Loop

while True:
    if len(opened) == 0:
        print("Target not found")
        break
    node = opened.pop()
    if node[0] == searchNode:
        print("Node found")
        break
    if node[1] == 4:  # Backtrack after reaching depth 3
        print("Depth has reached 3")
        while len(backtrack) > 0:
            print(backtrack.pop())
        continue
    children = my_graph[node[0]]
    for child in children[::-1]:
        if (node[0], child) not in closed:# Update parent-child relationship for backtracking
            if node[1] <=3:
                opened.append((child, node[child] + 1))  # Update depth of child
        backtrack.append((node[0], child))
    closed.append(node)
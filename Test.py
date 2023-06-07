my_graph = {"A": [("B", 2, 2), ("C", 4, 4)],
            "B": [("A", 2 , 2), ("C", 5,5), ("D", 1,1), ("F", 2,2)],
            "C": [("A", 4,4), ("B", 5,5), ("D", 3,3), ("G", 2,2)],
            "D": [("B", 1,1), ("C", 3,3), ("E", 3,3)],
            "E": [("D", 3, 3)],
            "F": [("B", 2, 2)],
            "G": [("C", 2, 2 )]}

open_queue = []
closed_queue = []
searchNode = input("Enter the node: ")
open_queue.append(("/", "A", 0, 0)) 
LoopTerminate = False


while not LoopTerminate:
    if len(open_queue) == 0:
        print("Not Found")
        LoopTerminate = True

    if not LoopTerminate:
        node = open_queue.pop(0)
        if node[1] == searchNode:
            print("Node Found")
            LoopTerminate = True
        
        children = my_graph[node[1]]
        #print("THIS IS WHAT CHILDREN HAVE",children)
        for child in children:
            u = node[3]+child[2]
            childNode = (node[1],child[0],child[1],u)
            print(childNode)
            if (node[1],child[0],child[1]) not in closed_queue:
                open_queue.append(childNode)
        closed_queue.append((node[0],node[1],node[2]))

        open_queue.sort(key=lambda x:x[3])
        print(open_queue)
        print("Heloooooooooooooooooo")
        #  break loops gracefully use a variable and initialize it false , in while condition at a specific condition make it true
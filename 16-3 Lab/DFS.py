grpah = { "A":["B","C"],
         "B":["F","A"],
         "C":["F","D","E","A"],
         "D":["C"],
         "E":["G","C"],
         "F":["B","C"],
         "G":["E"]}


node = input("Enter the Node: ")

node = node.upper()

open =[]
close = []

check = True
open.append(("/","A"))

# print(open)

while(check):
    if len(open) == 0:
        print("Target not Found")
        check = False
    if check:
        n = open.pop()
        #print(n)
        if n[1] == node:
            print("Target Hits...")
            check= False

        children = grpah[n[1]]

        # print(children)

        for child in children[::-1]:
            if not ((n[1],child) in close):
                open.append((n[1],child))
        # print(open)
        close.append(n)
        print(close)
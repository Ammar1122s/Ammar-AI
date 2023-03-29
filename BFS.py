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

open.append(("/","A"))

while True:
     if len(open) == 0:
        print("Target not Found")
        break
     n = open.pop(0)
    # print(n ,"\n")
     
     if n[1] == node:
         print("Target Hits!")
         break
     
     children = grpah[n[1]]
     
     for child in children:
         if not ((n[1],child) in close):
             open.append((n[1],child))
    
     close.append(n)
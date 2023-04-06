
grpah = { "A":[("B",2,2),("C",4,4)],
         "B":[("A",2,2),("C",5,5),("D",1,1),("F",2,2)],
         "C":[("A",4,4),("B",5,5),("D",3,3),("G",2,2)],
         "D":[("B",1,1),("C",3,3),("E",3,3)],
         "E":[("D",3,3)],
         "F":[("B",2,2)],
         "G":[("C",2,2)]}

# "A" parent ("B",2,2) "B" is child 2 is it's weight and next 2 is g(n)

node = input("Enter the Node: ")

node = node.upper()

open =[]
close = []

check = True
open.append(("/","A",0,0))

while check:
     if len(open) == 0:
        print("Target not Found")
        check = False
     if(check):
        n = open.pop(0)
        if n[1] == node:
         print("Target Hits!")
         check=False
     
        children = grpah[n[1]]
     
        for child in children:
            z = n[3] + child[2]
            if not ((n[1],child[0],child[1],z) in close):
             open.append((n[1],child[0],child[1],z))
    
     close.append(n)
     open.sort(key= lambda x: x[3])
     print(open)
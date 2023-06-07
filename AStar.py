# ("B",2,2,1) 2 is cast, 2 is g(n) and 1 is h(n)
#f(n) = g(n) + h(n)

grpah = { "A":[("B",2,2,1),("C",4,4,2)],
         "B":[("A",2,2,4),("C",5,5,6),("D",1,1,7),("F",2,2,3)],
         "C":[("A",4,4,6),("B",5,5,1),("D",3,3,2),("G",2,2,6)],
         "D":[("B",1,1,9),("C",3,3,12),("E",3,3,1)],
         "E":[("D",3,3,4)],
         "F":[("B",2,2,2)],
         "G":[("C",2,2,1)]}

node = input("Enter the Node: ")

node = node.upper()

open =[]
close = []

# ("/","A",0,0,1,1) 0 is cast, 0 is g(n) , 1 is h(n), 1 is f(n)
check = True
open.append(("/","A",0,0,1,1))

while check:
     if len(open) == 0:
        print("Target not Found")
        check = False
     if(check):
        n = open.pop(0)
        if n[1] == node:
         print("Target Hits!")
         
         print(n)
         print(n[0] + " is parent, ", n[1] ," is child " , n[2], " is cast ", n[3], " is g(n) ", n[4], " is h(n) ", n[5], " is f(n)" )
         check=False 
     
        children = grpah[n[1]]
     
        for child in children:
            z = n[3] + child[2]
            horistics = z + n[4]
            if not ((n[1],child[0],child[1]) in close):
             open.append((n[1],child[0],child[1],z,child[3],horistics))
            
     close.append((n[0],n[1],n[2]))
     print(open)
     open.sort(key= lambda x: x[5])
     print(open)
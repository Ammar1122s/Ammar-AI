
grpah = { "A":[("B",2,1),("C",4,6)],
         "B":[("C",5,15),("D",1,10),("F",2,21)],
         "C":[("D",3,13),("G",2,5)],
         "D":[("E",3,1)],
         "E":[("H",3,2)],
         "F":[("I",2,7)],
         "G":[("J",2,8)],
         "H":[],
         "I":[],
         "J":[]}

# "A" parent ("B",2,2) "B" is child 2 is it's weight and next 2 is h(n)

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
         print(n)
         check=False
     
        children = grpah[n[1]]
     
        for child in children:
            # z = n[3] + child[2]
            if not ((n[1],child[0],child[1]) in close):
             open.append((n[1],child[0],child[1],child[2]))
            
     close.append((n[0],n[1],n[2]))
     print(open)
     open.sort(key= lambda x: x[3])
     print(open)
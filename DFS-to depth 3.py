grpah = { "A":[("B",2),("C",2)],
         "B":[("A",1),("D",3),("E",3)],
         "C":[("A",1),("F",3),("G",3)],
         "D":[("B",2),("H",4)],
         "E":[("B",2),("H",4)],
         "F":[("C",2),("H",4)],
         "G":[("C",2),("H",4)],
         "H":[("D",3),("E",3),("F",3),("G",3)]}

# for example  "A":[("B",2)  "A" is the parent "B" is it's child and 2 is the depth level 


node = input("Enter the Target Node: ")

node = node.upper()

open =[]
close = []

check = True
open.append(("/","A",1))


while(check):
    if len(open) == 0:
        print("Target not Found")
        check = False
    if check:
        n = open.pop()
        if not len(open)==0:
            for x in close:
                if n[1] in x[1]:
                    n=open.pop()
        if n[1] == node:
            print("Target Hits...")
            check= False

        children = grpah[n[1]]

        for child in children[::-1]:
            
            if not ((n[1],child[0],child[1]) in close):
                
                if child[1] <= 3: # here i am checking if the depth is greater than 3 or not
                    
                    open.append((n[1],child[0],child[1]))
        close.append(n)
        # print(open)
        
        
        
    
import random

env = { 1:[2,3,4,5],
       2:[1,2,3,5],
       3:[3,5],
       4:[1,2,3,5],
       5:[1,3,5],
       6:[1,3,5],
       7:[1,3,5],
       8:[2,3,4,5]
}

final = []

for e in env:
    for sub in env[e]:
        final.append((e,sub))
        
        
print(final)


selected = random.sample(final,13)


selected.insert(0,(8,1))
selected.insert(len(selected),(1,1))

print("\n",selected)


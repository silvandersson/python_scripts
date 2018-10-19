"""
15 forks, 15 spoons
Permute randomly
Pick 10 consecutive items
Can you always find a way to do this and end up with 5 forks and 5 spoons? 
"""
import random

collection = []
for k in range(15):
    collection.append("fork")
for j in range(15):
    collection.append("spoon")
#  print(collection)

N = 10
success = 0
for i in range(N):
    random.shuffle(collection)
    #  print(collection)
    consecutive_ten_found = False
    for offset in range(0, 21):
        consecutive_collection = collection[0 + offset: 10 + offset]
        if consecutive_collection.count("fork") == 5:
            consecutive_ten_found = True
            print(consecutive_collection)
    if consecutive_ten_found:
        success += 1
print("Number of simulations: ", N)
print("Number of successful consecutive items found: ", success)
#==============================================================================
# Cars
# There are n cars starting at 0 in uniform, random order.
# Each car has a unique, maximum speed.
# A car travels at the minimum of its maximum speed and the speed of the 
# car in front of it.
# What is the expected number of clumps of cars?
#==============================================================================
import math
import random

n = 10 #nbr of cars
cars = [i for i in range(1,n+1)] # set the max speeds to 1..n for simplicity
M = 1000 #nbr of iterations
tot_nbr_of_clumps = 0

for k in range(1, M+1):
    random.shuffle(cars) # put cars in random order
    print("Initial queue of cars with max speed x: " + str(cars))
    front_speed = n + 1 # init front speed to highest value
    nbr_of_clumps = 0
    for car in cars:
        print(car)
        if car < front_speed:
            front_speed = car
            nbr_of_clumps += 1
    print("Number of clumps formed: " + str(nbr_of_clumps))
    tot_nbr_of_clumps += nbr_of_clumps

print("Average nbr of clumps formed: " + str(tot_nbr_of_clumps / M))
print("2log(n) = " + str(math.log2(n)))
print("log(n) = " + str(math.log(n)))
harmonic_sum = 0
for i in range(1, n+1):
    harmonic_sum += 1/i
print("SUM(1/n) = " + str(harmonic_sum))
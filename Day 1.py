# Day 1 - 2/12/19

import math

#part one
##def calculateFuel(mass):
##    return math.floor(int(mass)/3) - 2

#part two
def calculateFuel(mass):
    fuel_mass = math.floor(int(mass)/3) - 2
    if(fuel_mass > 0):
        return fuel_mass + calculateFuel(fuel_mass)
    else:
        return 0

total = 0

f = open("puzzle_input/day1.txt", "r")
for num in f:
    total += calculateFuel(num)
f.close()

print(total)

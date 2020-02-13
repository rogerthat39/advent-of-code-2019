# Day 1

import math

#part one
#calculate fuel needed for mass of ship
##def calculateFuel(mass):
##    return math.floor(int(mass)/3) - 2

#part two
#calculate fuel needed for mass of ship + extra mass of fuel
def calculateFuel(mass):
    fuel_mass = math.floor(int(mass)/3) - 2
    if(fuel_mass > 0):
        return fuel_mass + calculateFuel(fuel_mass)
    else:
        return 0

#main routine
total = 0

f = open("puzzle_input/day1.txt", "r")
for num in f:
    total += calculateFuel(num)
f.close()

print(total)

#Day 2 - 2/12/19

#part one
def getIntsList():
    f = open("puzzle_input/day2.txt", "r")
    ints = [int(x.strip()) for x in f.readline().split(',')]
    f.close()
    return ints

def intCode(ints):
    for i in range(0, len(ints), 4):
        n = ints[i]
        if(n == 1):
            a = ints[ints[i+1]]
            b = ints[ints[i+2]]
            ints[ints[i+3]] = a + b
        elif(n == 2):
            a = ints[ints[i+1]]
            b = ints[ints[i+2]]
            ints[ints[i+3]] = a * b
        elif (n==99):
            break
    return ints[0]

ints = getIntsList()
ints[1] = 12
ints[2] = 2
print(intCode(ints))

#part two

def findNounAndVerb(noun=50, verb=0):
    #reset ints list
    ints = getIntsList()

    #insert noun and verb into position 1 and 2 in the program memory
    ints[1] = noun
    ints[2] = verb

    #run the intCode program
    result = intCode(ints)

    #check whether the output equals the target (19690720)
    if(result == 19690720):
        return 100*noun + verb
    
    #since verb is only added at the end, only change it if the result is within 19690720 +/- 99
    #starting verb at 0, we can just check within range 19690720 - 99
    elif(result >= 19690720 - 99):
        return findNounAndVerb(noun, verb+1)
    
    #otherwise, alter the noun
    elif(result > 19690720):
        return findNounAndVerb(noun-1, verb)
    elif(result < 19690720):
        return findNounAndVerb(noun+1, verb)
    else:
        print("oops")
        return

print(findNounAndVerb())



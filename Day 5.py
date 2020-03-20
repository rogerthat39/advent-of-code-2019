#Day 5 - based on day 2 "Intcode" computer

def getIntsList():
    f = open("puzzle_input/day5.txt", "r")
    ints = [int(x.strip()) for x in f.readline().split(',')]
    f.close()
    return ints

def intCode(ints):
    n = 0
    i = 0
    
    while(n != 99):
        n = ints[i]
        modes = determineModes(str(n))

        #change the opcode to the last two digits if the mode was supplied
        if(modes != ['0','0','0']):
            n = int(str(n)[-2:])

        #opcode 1 - add two digits and store in position given
        if(n == 1):
            a = getValue(i+1, modes[0])
            b = getValue(i+2, modes[1])
            ints[ints[i+3]] = a + b
            i += 4 #go to next instruction
            
        #opcode 2 - multiply two digits and store in position given
        elif(n == 2):
            a = getValue(i+1, modes[0])
            b = getValue(i+2, modes[1])
            ints[ints[i+3]] = a * b
            i += 4 #go to next instruction
            
        #opcode 3 - store input from user in position given
        elif(n == 3):
            ints[ints[i+1]] = int(input("Enter an input: "))
            i += 2 #go to next instruction - this instruction is 2 chars long
            
        #opcode 4 - output the digit in the position given
        elif(n == 4):
            print(getValue(i+1, modes[0]))
            i += 2 #go to next instruction - this instruction is 2 chars long

        #opcode 5 - jump to given place in program if True
        elif(n == 5):
            if(getValue(i+1, modes[0]) != 0):
                i = getValue(i+2, modes[1]) #set pointer to second parameter
            else:
                i += 3 #go to the next instruction as normal

        #opcode 6 - jump to given place in program if False
        elif(n == 6):
            if(getValue(i+1, modes[0]) == 0):
                i = getValue(i+2, modes[1]) #set pointer to second parameter
            else:
                i += 3 #go to the next instruction as normal

        #opcode 7 - store '1' in position given if first param less than second
        elif(n == 7):
            if(getValue(i+1, modes[0]) < getValue(i+2, modes[1])):
                ints[ints[i+3]] = 1
            else:
                ints[ints[i+3]] = 0
            i += 4 #go to next instruction (this instruction is 3 chars long)

        #opcode 8 - store '1' in position given if first and second params match
        elif (n == 8):
            if(getValue(i+1, modes[0]) == getValue(i+2, modes[1])):
                ints[ints[i+3]] = 1
            else:
                ints[ints[i+3]] = 0
            i += 4 #go to next instruction (this instruction is 3 chars long)
        
    #return the diagnostic code at position 0 in list
    print("Halting...")
    return ints[0]

#returns modes if they were supplied, or a list of 0's if none present
def determineModes(instruction):
    if(len(instruction) > 2):
        #get all digits apart from opcode (2 right-most digits)
        modes = instruction[:-2]
            
        #reversed so it reads left to right (so the first mode comes first)
        modes = list(reversed(modes))

        #pad out the list (where mode is not supplied, mode = 0)
        while(len(modes) < 3):
            modes.append('0')

        return modes
    else:
        return ['0','0','0']

#returns a value depending on which mode is given
def getValue(location, mode):
    if(mode == '1'): #immediate mode - returns the value itself
        return ints[location]
    elif(mode == '0'): #position mode - returns value in that position in list
        return ints[ints[location]]

#main routine
ints = getIntsList()
intCode(ints)


#Day 9 - based on day 5 "Intcode" computer

def getIntsList():
    f = open("puzzle_input/day9.txt", "r")
    ints = [int(x.strip()) for x in f.read().split(',')]
    f.close()
    return ints

def intCode(ints):
    global relative_base
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
            #check whether ints list is long enough to store value in that address
            for value in [i+1, i+2, i+3]:
                if(getValue(value, modes[2]) >= len(ints)):
                    padOutIntsList(getValue(value, modes[2]))

            a = ints[getValue(i+1, modes[0])]
            b = ints[getValue(i+2, modes[1])]
                
            ints[getValue(i+3, modes[2])] = a + b
            i += 4 #go to next instruction
            
        #opcode 2 - multiply two digits and store in position given
        elif(n == 2):        
            #check whether ints list is long enough to store value in that address
            for value in [i+1, i+2, i+3]:
                if(getValue(value, modes[2]) >= len(ints)):
                    padOutIntsList(getValue(value, modes[2]))

            a = ints[getValue(i+1, modes[0])]
            b = ints[getValue(i+2, modes[1])]
                
            ints[getValue(i+3, modes[2])] = a * b
            i += 4 #go to next instruction
            
        #opcode 3 - store input from user in position given
        elif(n == 3):
            ints[getValue(i+1, modes[0])] = int(input("Enter an input: "))
            i += 2 #go to next instruction
            
        #opcode 4 - output the digit in the position given
        elif(n == 4):
            print(ints[getValue(i+1, modes[0])])
            i += 2 #go to next instruction - this instruction is 2 chars long

        #opcode 5 - jump to given place in program if True
        elif(n == 5):
            if(ints[getValue(i+1, modes[0])] != 0):
                i = ints[getValue(i+2, modes[1])] #set pointer to second parameter
            else:
                i += 3 #go to the next instruction

        #opcode 6 - jump to given place in program if False
        elif(n == 6):
            if(ints[getValue(i+1, modes[0])] == 0):
                i = ints[getValue(i+2, modes[1])] #set pointer to second parameter
            else:
                i += 3 #go to the next instruction

        #opcode 7 - store '1' in position given if first param less than second
        elif(n == 7):
            #check whether ints list is long enough to store value in that address
            if(getValue(i+3, modes[2]) >= len(ints)):
                padOutIntsList(getValue(i+3, modes[2]))
                
            if(ints[getValue(i+1, modes[0])] < ints[getValue(i+2, modes[1])]):
                ints[getValue(i+3, modes[2])] = 1
            else:
                ints[getValue(i+3, modes[2])] = 0
            i += 4 #go to next instruction

        #opcode 8 - store '1' in position given if first and second params match
        elif (n == 8):
            #check whether ints list is long enough to store value in that address
            if(getValue(i+3, modes[2]) >= len(ints)):
                padOutIntsList(getValue(i+3, modes[2]))
                
            if(ints[getValue(i+1, modes[0])] == ints[getValue(i+2, modes[1])]):
                ints[getValue(i+3, modes[2])] = 1
            else:
                ints[getValue(i+3, modes[2])] = 0
            i += 4 #go to next instruction

        #opcode 9 - add parameter to relative base
        elif (n == 9):
            #check whether ints list is long enough to store value in that address
            if(getValue(i+1, modes[0]) >= len(ints)):
                padOutIntsList(getValue(i+1, modes[0]))

            relative_base += ints[getValue(i+1, modes[0])]
            i += 2 #go to next instruction
        
    #return the diagnostic code at position 0 in list
    print("Halting...")

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
    if(mode == '0'): #position mode - returns value in that position in list
        return ints[location]
    
    elif(mode == '1'): #immediate mode - returns the value itself
        return location
        
    elif(mode == '2'): #relative mode - returns value from relative base offset by location
    
        return relative_base + ints[location]

#add '0's to the end of the list so we can write to locations in ints list
#that don't currently exist
def padOutIntsList(location):
    for i in range(len(ints), location+1):
        ints.append(0)

#main routine
relative_base = 0
ints = getIntsList()
intCode(ints)

#Day 3

def insertToGrid(x, y, char):
    global originX
    global originY
    global currentPointX
    global currentPointY
    global steps_wire_2

    #add 1 to the step counter (if drawing wire 2)
    if(char == "2"):
        steps_wire_2 += 1
        if (steps_wire_2 > leastSteps):
            return
    
    if(x > len(grid)-1):
        #if position in downwards X direction doesn't exist, add new row
        grid.append([])

        #fill new row with dots
        for i in range(0, len(grid[x-1])):
            grid[x].append('.')

        #add char to position
        grid[x][y] = char
        
    elif(x == -1):
        #if position in upwards X direction doesn't exist
        grid.insert(0, [])

        #fill new row with dots
        for i in range(0, y+1):
            grid[0].append('.')

        #add char to position
        grid[0][y] = char
        
        #update origin position
        originX += 1

        #reset x to 0
        currentPointX = 1 #will be 0 when it has -1 applied
    
    #if position in right Y direction doesn't exist
    #append dots until Y reached
    elif(y > len(grid[x])-1):
        for i in range(len(grid[x])-1, y):
            grid[x].append('.')
            
    #add char to position
        grid[x][y] = char

    elif(y == -1):
        #if position in left Y direction doesn't exist
        #indent each row by one
        for l in grid:
            l.insert(0, '.')
            
        #add char to position
        grid[x][0] = char

        #update origin position
        originY += 1

        #reset y to 0
        currentPointY = 1 #will be 0 when it has -1 applied

    else: #if position already exists
        #put the char letter on the grid if empty spot available
        #don't put an 'x' on the same wire crossing with itself
        if(grid[x][y] == '.' or grid[x][y] == char):
            grid[x][y] = char
        #put an 'x' on an intersection (but not on the origin!)
        elif(grid[x][y] != 'O'):
            grid[x][y] = 'x'
            #calculateDistanceFromOrigin(x, y)
            calculateStepsFromOrigin(x, y)
            
def drawWire(directions, char):
    global originX
    global originY
    global currentPointX
    global currentPointY

    #start the wire from the origin point
    currentPointX = originX
    currentPointY = originY

    #draw the wire based on the directions given (eg. U4 = up 4)
    for d in directions:
        if d[0] == 'R':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX, currentPointY+1, char)
                currentPointY += 1
              
        elif d[0] == 'L':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX, currentPointY-1, char)
                currentPointY -= 1
            
        elif d[0] == 'U':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX-1, currentPointY, char)
                currentPointX -= 1
            
        elif d[0] == 'D':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX+1, currentPointY, char)
                currentPointX += 1

def calculateDistanceFromOrigin(x, y):
    #calculates the manhattan distance between new intersection and origin
    #if distance is the new shortest, closestDistance variable is updated
    global originX
    global originY
    global closestDistance

    if(originY > y):
        YDistance = originY - y
    else:
        YDistance = y - originY
    if(originX > x):
        XDistance = originX - x
    else:
        XDistance = x - originX

    totalDistance = XDistance + YDistance
    
    if(totalDistance < closestDistance):
        closestDistance = totalDistance

def calculateStepsFromOrigin(x, y):
    #calculate combined step count for wire 1 + wire 2 using coordinates
    #of intersection.

    #follow the path of wire 1 until you get to the x/y coordinates
    global originX
    global originY
    global leastSteps

    #start the wire from the origin point
    #note this is not the same "currentPointX" as the global variable - we need that to stay the same so the rest of the wire can be drawn
    currentPointX = originX
    currentPointY = originY

    steps_wire_1 = 0

    #similar to drawWire, but without the inserting (this has already happened!)
    for d in wire1:
        if(currentPointX == x and currentPointY == y):
            break
        
        direction = d[0]
        steps = int(d[1:])
        
        if direction == 'R':
            for i in range(0, steps):
                currentPointY += 1
                steps_wire_1 += 1
                if(currentPointX == x and currentPointY == y):
                    break
              
        elif direction == 'L':
            for i in range(0, steps):
                currentPointY -= 1
                steps_wire_1 += 1
                if(currentPointX == x and currentPointY == y):
                    break
            
        elif direction == 'U':
            for i in range(0, steps):
                currentPointX -= 1
                steps_wire_1 += 1
                if(currentPointX == x and currentPointY == y):
                    break
            
        elif direction == 'D':
            for i in range(0, steps):
                currentPointX += 1
                steps_wire_1 += 1
                if(currentPointX == x and currentPointY == y):
                    break

    #add steps wire 1 and wire 2 to get total
    totalSteps = steps_wire_1 + steps_wire_2
    #print(str(totalSteps) + " = " + str(steps_wire_1) + " + " + str(steps_wire_2))

    #compare step count with current least
    if(leastSteps > totalSteps):
        leastSteps = totalSteps

#read data from text file
f = open("puzzle_input/day3.txt", "r")
wire1 = [x.strip() for x in f.readline().split(',')] #x.strip gets rid of the \n character in the first line
wire2 = [x.strip() for x in f.readline().split(',')]
f.close()

#set up variables
grid = [['O']]
originX = 0
originY = 0
currentPointX = originX
currentPointY = originY

closestDistance = 999999999
leastSteps = 9999999999
steps_wire_2 = 0

#draw the two wires
drawWire(wire1, "1")
drawWire(wire2, "2")

#print the answer
#print(closestDistance)
print(leastSteps)

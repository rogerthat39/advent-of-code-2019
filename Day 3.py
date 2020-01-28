#Day 3 - 4/12/19

#puzzle 1
def insertToGrid(x, y, char, distance):
    global originX
    global originY
    global currentPointX
    global currentPointY
    
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
    
    elif(y > len(grid[x])-1):
        #if position in right Y direction doesn't exist
        #append dots until Y reached
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

    else: #if position exists
        #put the char letter on the grid if empty spot available
        #don't put an 'x' on the same wire crossing with itself
        if(grid[x][y] == '.' or grid[x][y] == char):
            grid[x][y] = char
        #put an 'x' on an intersection (but not on the origin!)
        elif(grid[x][y] != 'O'):
            grid[x][y] = 'x'
            
def drawWire(directions, char):
    global originX
    global originY
    global currentPointX
    global currentPointY
    
    currentPointX = originX
    currentPointY = originY
    
    for d in directions: #insert 'char' to position Y+1 (in list X)
        if d[0] == 'R':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX, currentPointY+1, char, int(d[1:]))
                currentPointY += 1
              
        elif d[0] == 'L':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX, currentPointY-1, char, int(d[1:]))
                currentPointY -= 1
            
        elif d[0] == 'U':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX-1, currentPointY, char, int(d[1:]))
                currentPointX -= 1
            
        elif d[0] == 'D':
            for i in range(0, int(d[1:])):
                insertToGrid(currentPointX+1, currentPointY, char, int(d[1:]))
                currentPointX += 1

#read data from text file
f = open("puzzle_input/day3.txt", "r")
wire1 = [x.strip() for x in f.readline().split(',')] #x.strip gets rid of the \n character in the first line
wire2 = [x.strip() for x in f.readline().split(',')]
f.close()

#set up variables - grid, where wires start from (origin)
grid = [['O']]
originX = 0
originY = 0
currentPointX = originX
currentPointY = originY

#draw the two wires
drawWire(wire1, "1")
drawWire(wire2, "2")

#find intersections, then calculate distance from origin
currentClosest = 999999999

for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
        if(grid[x][y] == 'x'):
            if(originY > y):
                YDistance = originY - y
            else:
                YDistance = y - originY
            if(originX > x):
                XDistance = originX - x
            else:
                XDistance = x - originX

            totalDistance = XDistance + YDistance
            
            if(totalDistance < currentClosest):
                currentClosest = totalDistance

print(currentClosest)

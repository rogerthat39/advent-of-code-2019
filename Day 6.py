#day 6 - 17/3/20

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.right_child == None:
            self.right_child = value
        elif self.left_child == None:
            self.left_child = value
        else:
            print("This node already has two children")

    #iterate through the binary tree from the center of mass
    def countOrbits(self, count=0):
        global numOrbits
        numOrbits += count
        
        if self.left_child:
            self.left_child.countOrbits(count+1)

        if self.right_child:
            self.right_child.countOrbits(count+1)

def getPuzzleInput(file):
    reader = open(file, 'r')
    lst = [x.strip().split(')') for x in reader.read().split('\n')]
    reader.close()
    return lst

object_list = getPuzzleInput('puzzle_input/day6.txt')

dictionary = {}

#create a binary tree using the dictionary to store the objects
for obj in object_list:
    base_obj = obj[0]
    orbiting_obj = obj[1]

    #create base object if it doesn't exist in dict
    if(base_obj not in dictionary):
        dictionary[base_obj] = BinaryTree(base_obj)
    
    #create orbiting object if it doesn't exist in dict
    if(orbiting_obj not in dictionary):
        dictionary[orbiting_obj] = BinaryTree(orbiting_obj)
        
    #add orbiting object as a child of base object
    dictionary[base_obj].insert(dictionary[orbiting_obj])

#part one: find total number of direct and indirect orbits
numOrbits = 0
dictionary['COM'].countOrbits()
    
print(numOrbits)

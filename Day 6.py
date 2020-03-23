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


#return an array of nodes starting from the COM, going to the given value
def findPathToRoot(value):
    for node in dictionary.values():
        if node.left_child == value or node.right_child == value:
            arr = findPathToRoot(node)
            arr.append(node)
            return arr
    return []

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

#part two: find path between SAN and YOU
#create "queues" which hold parent nodes going back from the two nodes
path_back_from_san = findPathToRoot(dictionary['SAN'])
path_back_from_you = findPathToRoot(dictionary['YOU'])

#find the earliest part where the paths intersect
for node in reversed(path_back_from_san):
    if node in path_back_from_you:
        intersect = node
        break

#cut out the parts of each path that go back further than the intersect
index_san = path_back_from_san.index(intersect)
path_back_from_san = path_back_from_san[index_san:]

#cut out the extra intersect (otherwise will have a duplicate in final list)
index_you = path_back_from_you.index(intersect) + 1
#reverse the path since it currently reads forwards from COM
path_back_from_you = list(reversed(path_back_from_you[index_you:]))

#create the final path
path_from_you_to_san = path_back_from_you + path_back_from_san

#minus one from result as it includes the orbit 'YOU' is currently in
print(len(path_from_you_to_san) - 1)

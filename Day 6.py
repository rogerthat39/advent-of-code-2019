#day 6 - 17/3/20

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        elif self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            print("this node already has two children")

def getPuzzleInput(file):
    reader = open(file, 'r')
    lis = [x.strip() for x in reader.read().split('\n')]
    f.close()
    return lis

nodes = getPuzzleInput('puzzle_input/day6.txt')

print(nodes)

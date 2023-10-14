import cProfile
import re

def cd(arg):
    global currentDirectory
    arg = arg.replace("$ cd ", '')
    # print('cd to', arg)
    if arg == '/':
        currentDirectory = Base.childs['/']
    elif arg == '..':
        currentDirectory = currentDirectory.parent
    else:
        currentDirectory = currentDirectory.childs.get(arg)

def ls(_):
    pass

def dir(arg):
    global currentDirectory
    arg = arg.replace("dir ", '')
    # print("directory: ", arg)
    currentDirectory.childs[arg] = Directory(currentDirectory)

def file(arg):
    global currentDirectory
    # print('size ', arg)
    currentDirectory.size = currentDirectory.size + int(arg)
    parent = currentDirectory.parent
    while parent:
        parent.size = parent.size + int(arg)
        parent = parent.parent

function_dict = {
    "$ cd ": cd,
    "$ ls": ls,
    "dir ": dir,
    "file": file
}

class Directory:
    def __init__(self, parent):
        self.parent = parent
        self.childs = {}
        self.size = 0

Base = Directory(None)
Base.childs['/'] = Directory(Base)
currentDirectory = Base.childs['/']

class Decoder1:
    def __init__(self):  
        self.smallNodes = []   
        self.Nodes = {}
        self.findSmallNotes(Base)
        print(sum([size for size in self.smallNodes]))
        systemSize = 70000000
        requiredFreeSpace = 30000000
        freeSpace = systemSize - Base.size
        minimumRequiredFolderSize = requiredFreeSpace - freeSpace
        print("We need to free ", minimumRequiredFolderSize, " to apply the update")

        candidatefolder = '/'
        candidate = self.Nodes[candidatefolder]
        for folder,size in self.Nodes.items():
            if size > minimumRequiredFolderSize and size < candidate:
                candidate = size
                candidatefolder = folder
        print(candidatefolder, candidate)

    def findSmallNotes(self, node):
        if node.childs:     
            for child_item, child_node in node.childs.items():
                self.Nodes[child_item] =  child_node.size
                self.findSmallNotes(child_node)

        if  node.size < 100000:
                self.smallNodes.append(node.size)
            

class Decoder2:
    def __init__(self, seq):
        print (sum([ruleSet2[key] for key in seq]))


if __name__ == '__main__':

    f = open('Day7.txt', mode='r')
    seq = [line.strip() for line in f]

    for s in seq:
        pattern = r"^\d+"
        match = re.match(pattern, s)
        if match:
            function_dict['file'](match.group())
        else:
            for key in function_dict:
                if key in s:
                    function_dict[key](s)

    Decoder1()
    # Decoder2(seq)

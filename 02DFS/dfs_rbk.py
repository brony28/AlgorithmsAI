n = int(input("Enter no of nodes : "))

g={}
for i in range(n):
    sNode = input("Enter node => ")
    cNodes = input("Enter its child node => ").split()
    g[sNode] = cNodes

for key,val in g.items():
    print(f'{key} -> {val}')
# print(g)

class Nodes(object):
    def __init__(self, treeDict =None):
        
        if(treeDict is None):
            self.treeDict = {}
        else:
            self.treeDict = treeDict
            
    def showNodes(self):
        return list(self.treeDict.keys())

    def findPath(self, startNode, goalNode, stack, path=None, orderOfNodes = None,count = 0):
        if path == None:
            path = []
        if orderOfNodes == None:
            orderOfNodes = []
        tree = self.treeDict
        path = path + [startNode]
        print(stack)
        temp = stack.pop(0)
        orderOfNodes.append(temp)
        stack = tree[temp] + stack
        count+=1
        if startNode == goalNode:
            return path,count-1,orderOfNodes
        if startNode not in tree:
            return None
        for vertex in tree[startNode]:
            if vertex not in path:
                extended_path = self.findPath(vertex, goalNode, stack, path, orderOfNodes ,count)
                if extended_path: 
                    return extended_path
        return None

n = Nodes(g)
n.showNodes() # displays all nodes..

startNode = input("Enter start node : ")
goalNode = input("Enter goal node : ")
stack = [startNode]
print()

solnPath, Cost, ordor= n.findPath(startNode,goalNode,stack) #displays
print("Order of Nodes -> ",ordor)
print("Solution Path -> ",solnPath)
print("Cost -> ",Cost)

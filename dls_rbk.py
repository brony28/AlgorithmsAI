class Nodes(object):
    
#     orderOfNodes = [] 
    def __init__(self, treeDict =None):
        
        if(treeDict is None):
            self.treeDict = {}
        else:
            self.treeDict = treeDict
            
    def showNodes(self):
        return list(self.treeDict.keys())
    
    def findPath(self, limit, startNode, goalNode, stack=None, path=None, stackyStack=None, cost=0):
        if(path==None):
            path=[]
        if(stack==None):
            stack=[startNode]
        if(stackyStack==None):
            stackyStack=[]
        tree = self.treeDict
        if(startNode not in tree):
            return None
#         print(stack)
        path = path + [startNode]
        stackyStack.append(stack)
#         print(stack)
        if(startNode==goalNode):
            return path,cost,stackyStack
        temp = stack.pop(0)
        stack = tree[temp] + stack
        cost+=1
        
        for value in tree[startNode]:
            if(value not in path):
                extended_path = self.findPath(limit, value, goalNode, stack, path, stackyStack, cost)
                if extended_path: 
                    return extended_path
        return None


n = int(input("Enter no of nodes"))

g={}
for i in range(n):
    sNode = input("Enter node -> ")
    cNodes = input("Enter its child node -> ").split()
    g[sNode] = cNodes

for key,val in g.items():
    print(f'{key} -> {val}')
# print(g)


n = Nodes(g)
n.showNodes() # displays all nodes..

startNode = input("Enter start node ")
goalNode = input("Enter goal node ")
limit = int(input("Enter depth"))

pathy,costy,stackyStacky= n.findPath(limit,startNode,goalNode) #displays

if(limit>=costy):
    for i in stackyStacky:
        print(i)
    print("Pathy -> ",pathy)
    print("Costy -> ",costy)
else:
    print("Not reachable")

n = int(input("Enter no of nodes"))

g={}
for i in range(n):
    sNode = input("Enter node -> ")
    cNodes = input("Enter its child node").split()
    g[sNode] = cNodes
    

    
for key,val in g.items():
    print(f'{key} -> {val}')
# print(g)




 class Nodes(object):
    
#     orderOfNodes = []
    def __init__(self, treeDict =None):
        
        if(treeDict is None):
            self.treeDict = {}
        else:
            self.treeDict = treeDict
            
    def showNodes(self):
        return list(self.treeDict.keys())
    
    #implemented dfs for shortest path
    def solnPath(self, node, goalNode, path=None):
        if path == None:
            path = []
        treeS = self.treeDict
        path = path + [node]
        
        if node == goalNode:
            return True
        if node not in treeS:
            return False
        for val in treeS[node]:
            if val not in path:
                extended_path = self.solnPath(val, goalNode, path)
                if extended_path: 
                    return extended_path
        return None
        
    def findPath(self, startNode, goalNode, queue, orderOfPath=None, path=None, soluPathList = None,cost = 0):
        if path == None:
            path = []
        if orderOfPath == None:
            orderOfPath = []
        if soluPathList == None:
            soluPathList = []
        tree = self.treeDict
        if startNode not in tree:
            return None
#         print(queue)
        temp = queue.pop(0)
        if(self.solnPath(temp,goalNode)):
            cost+=1
#             print("Ho Ho") #flag checking
            soluPathList.append(temp)
        orderOfPath.append(temp)
        queue = queue + tree[temp]
        if startNode==goalNode:
            return "Reached", orderOfPath, soluPathList, cost-1
        print(queue)
        for val in queue:
            return self.findPath(val, goalNode, queue, orderOfPath, path, soluPathList, cost)








n = Nodes(g)
n.showNodes() # displays all nodes..




startNode = input("Enter start node ")
goalNode = input("Enter goal node ")
queue = [startNode]
print(queue)


checker, ordor, solPath, cost = n.findPath(startNode,goalNode,queue) #displays
print(checker)
# solnPaa = n.solnPath(startNode, goalNode)
print("Order of Nodes -> ",ordor)
print("Solution Path -> ",solPath)
print("Cost -> ",cost)
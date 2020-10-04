n = int(input("Enter no of nodes"))

g={}

for i in range(n):
    sNode = input("Enter node -> ")
    cNodes = input("Enter its child node and its cost -> ").split()
    temp=[]
    for i in range(0,len(cNodes),2):
        temp.append([cNodes[i],int(cNodes[i+1])])
    g[sNode] = temp    
for key,val in g.items():
    print(f'{key} -> {val}')
# print(g)

# g = {'s':[['a',6],['b',5],['c',10]],
#      'a':[['e',6]],
#      'b':[['e',6],['d',7]],
#      'c':[['d',6]],
#      'e':[['f',4]],
#      'd':[['f',6]],
#      'f':[['g',3]],
#      'g':[[]]}


# g = {'s':[['a',1],['g',12]],
#      'a':[['b',3],['c',1]],
#      'b':[['d',3]],
#      'c':[['d',1],['g',2]],
#      'd':[['g',3]],
#      'g':[[]]}







class Nodes(object):
    def __init__(self, treeDict =None):
        
        if(treeDict is None):
            self.treeDict = {}
        else:
            self.treeDict = treeDict
            
    def showNodes(self):
        return list(self.treeDict.keys())
    
    #TO BE TESTED
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
            if val[0] not in path:
                extended_path = self.solnPath(val[0], goalNode, path)
                if extended_path: 
                    return extended_path
        return None
    
        
    def findPath(self, startNode, goalNode, queue=None, orderOfPath=None,soluPathList=None,cost=0):
        if(queue==None):
            queue = [[startNode,0]]
        if(orderOfPath==None):
            orderOfPath = []
        if(soluPathList==None):
            soluPathList=[]
        tree = self.treeDict.copy()

        while(len(queue)!=0):
            queue.sort(key = lambda x:x[1])
            print(queue)
            temp = queue.pop(0)
            orderOfPath.append(temp[0])
            if(self.solnPath(temp[0],goalNode)):
                soluPathList.append(temp[0])
            cost = temp[1]
            if(temp[0]==goalNode):
                return "Reached",orderOfPath,soluPathList,cost
            tempTree = tree[temp[0]]
            ahem = tempTree.copy()
            ok = []
            for values in ahem:
                ok.append([values[0],values[1]+temp[1]])
            queue = queue + ok

        return self.findPath(startNode, goalNode, queue, orderOfPath,soluPathList,cost)




n = Nodes(g)
n.showNodes() # displays all nodes..



startNode = input("Enter start node ")
goalNode = input("Enter goal node ")
# print([[startNode,0]])
# que = PriorityQueue()
# que.put((0,startNode))
# print(que)
checker,ordor,solPath,cost = n.findPath(startNode,goalNode) #displays
print(checker)
# solnPaa = n.solnPath(startNode, goalNode)
print("Order of Nodes -> ",ordor)
print("Solution Path -> ",solPath)
print("Cost -> ",cost)
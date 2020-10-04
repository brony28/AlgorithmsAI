
g={}
hue = {}

n = int(input("Enter no of nodes"))


for i in range(n):
    sNode = input("Enter node -> ")
    hueVal = int(input("Enter the heuristic value -> "))
    cNodes = input("Enter its child node, heuristic value and its cost from parent node -> ").split()
    temp=[]
    for i in range(0,len(cNodes),2):
        temp.append([cNodes[i],int(cNodes[i+1])])
    g[sNode] = temp
    hue[sNode] = hueVal
for key,val in g.items():
    print(f'{key} -> {val}')

print("Heuristic Table")
for key,val in hue.items():
    print(f'{key} -> {val}')


# g = {'s':[['a',6],['b',5],['c',10]],
#      'a':[['e',6]],
#      'b':[['e',6],['d',7]],
#      'c':[['d',6]],
#      'e':[['f',4]],
#      'd':[['f',6]],
#      'f':[['g',3]],
#      'g':[[]]}
# hue = {
#     's':17,
#      'a':10,
#      'b':13,
#      'c':4,
#      'e':4,
#      'd':2,
#      'f':1,
#      'g':0
# }


class Nodes(object):
    def __init__(self, treeDict =None):
        
        if(treeDict is None):
            self.treeDict = {}
        else:
            self.treeDict = treeDict
            
    def showNodes(self):
        return list(self.treeDict.keys())
        
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

    def findPath(self, startNode, goalNode, hue, staque=None, path=None, solnPathList=None,cost=0):
        trees = self.treeDict
        if(staque==None):
            staque=[[startNode,hue[startNode],0]]
        if(path==None):
            path=[]
        if(solnPathList==None):
            solnPathList=[]
        print(staque)
        if startNode not in trees:
            return None
        if(startNode==goalNode):
            return "Reached",path+[goalNode],solnPathList+[goalNode],cost
        temp = staque.pop(0)
        path.append(temp[0])
        if(self.solnPath(temp[0],goalNode)):
            solnPathList.append(temp[0])
        for values in trees[temp[0]]:
            values[1]=values[1]+temp[2]
#             print(values)
#             print
        for values in trees[temp[0]]:
            staque.insert(0,[values[0],hue[values[0]],values[1]])
        staque.sort(key = lambda x:x[1])
        startNode = staque[0][0]
        cost = staque[0][2]
        return self.findPath(startNode, goalNode, hue, staque,path,solnPathList,cost)




n = Nodes(g)
n.showNodes() # displays all nodes..



startNode = input("Enter start node ")
goalNode = input("Enter goal node ")
print(hue)
checker,Path,solPathListy,costy = n.findPath(startNode,goalNode,hue) #displays
print(checker)
# print(staque)
print("Order of Nodes -> ",Path)
print("Solution Path -> ",solPathListy)
print("Cost -> ",costy)

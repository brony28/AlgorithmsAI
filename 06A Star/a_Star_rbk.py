g={}
hue = {}


# n = int(input("Enter no of nodes"))

# for i in range(n):
#     sNode = input("Enter node -> ")
#     hueVal = int(input("Enter the heuristic value -> "))
#     cNodes = input("Enter its child node, heuristic value and its cost from parent node -> ").split()
#     temp=[]
#     for i in range(0,len(cNodes),2):
#         temp.append([cNodes[i],int(cNodes[i+1])])
#     g[sNode] = temp
#     hue[sNode] = hueVal
# for key,val in g.items():
#     print(f'{key} -> {val}')
    
# print("Heuristic Table")
# for key,val in hue.items():
#     print(f'{key} -> {val}')



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



g = {'s':[['a',1],['g',10]],
     'a':[['b',2],['c',1]],
     'b':[['d',5]],
     'c':[['d',3],['g',4]],
     'd':[['g',2]],
     'g':[[]]}
hue = {
    's':5,
     'a':3,
     'b':4,
     'c':2,
     'd':6,
     'g':0
}




# g = {'s':[['a',5],['b',1]],
#      'a':[['g',1]],
#      'b':[['c',2]],
#      'c':[['g',2]],
#      'g':[[]]}

# hue = {
#     's':5,
#      'a':1,
#      'b':4,
#      'c':2,
#      'g':0
# }





class Nodes(object):
    def __init__(self, treeDict=None):
        if(treeDict is None):
            self.treeDict = {}
        else:
            self.treeDict = treeDict
            
    def showNodes(self):
        return list(self.treeDict.keys())
    
    def findPath(self, startNode, goalNode, hue, queue=None, path=None,cost=0):
        trees = self.treeDict
        if(queue==None):
            queue = [[startNode,0]]
        if(path==None):
            path=[]
        if startNode not in trees:
            return None
        
        while(len(queue)!=0):
            queue.sort(key = lambda x:x[1])
            print(queue)
            temp = queue.pop(0)
            path.append(temp[0])
            if(temp[1]!=0):
                cost = cost + temp[1] - hue[temp[0]]
            if(temp[0]==goalNode):
                return "Reached",cost,path
            tempTree = trees[temp[0]]
            ahem = tempTree.copy()
            ok = []
            for values in ahem:
                ok.append([values[0],values[1]+hue[values[0]]])
            queue = queue + ok
        return self.findPath(startNode, goalNode, hue, queue, path,cost)





n = Nodes(g)
n.showNodes() # displays all nodes..



startNode = input("Enter start node ")
goalNode = input("Enter goal node ")
print(hue)
checker,costy,Path = n.findPath(startNode,goalNode,hue) #displays
print(checker)
# print(staque)
print("Order of Nodes -> ",Path)
print("Solution Path -> ",Path)
print("Cost -> ",costy)



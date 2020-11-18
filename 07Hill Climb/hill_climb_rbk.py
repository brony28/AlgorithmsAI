g={}
hue = {}


### USER INPUT VALUES
n = int(input("Enter no of nodes : "))

for i in range(n):
    sNode = input("Enter node => ")
    hueVal = int(input("Enter the heuristic value => "))
    cNodes = input("Enter its child node => ").split()
    temp=[]
    for i in range(0,len(cNodes)):
        temp.append(cNodes[i])
    g[sNode] = temp
    hue[sNode] = hueVal
print()
for key,val in g.items():
    print(f'{key} -> {val}')
    
print("Heuristic Table")
for key,val in hue.items():
    print(f'{key} -> {val}')
# TO execute with hardcoded values, comment the lines from 'USER INPUT VALUES'
# and uncomment any of the below examples.

#HARDCODE eg1
# g = {'c':['b','t','o','e','p'],
#      'b':['a','r','s'],
#      't':[],
#      'o':['i','n'],
#      'e':['g'],
#      'p':['l','f','d'],
#      'a':[],
#      'r':[],
#      's':[],
#      'i':['z'],
#      'n':[],
#      'g':[],
#      'l':[],
#      'd':[],
#      'f':[],
#      'z':[]}

# hue = {'c':21,'b':14,'t':5,'o':7,'e':13,'p':15,'a':17,'r':20,'s':50,'i':4,'n':44,'g':51,'l':0,'d':10,'f':8,'z':0}



#HARDCODE eg2
# g = {'a':['b','c','u'],'b':['e','g'],'c':['g','i','j'],'u':['k','y'],'e':['g','m'],'g':['m'],'i':['m'],'j':['k'],'k':['j'],'y':['m'],'m':[]}
# hue = {'a':7,'b':5,'c':3,'u':4,'e':2,'g':3,'i':6,'j':2,'k':1,'y':2,'m':0}

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
            queue = [[startNode,hue[startNode]]]
            cost=hue[startNode]
        if(path==None):
            path=[]
        if startNode not in trees:
            return None
        
        while(len(queue)!=0):
            queue.sort(key = lambda x:x[1])
            print(queue)
            temp = queue.pop(0)
            path.append(temp[0])
            if(temp[1]==0):
                return "Global Optima Reached"
            
            if(temp[0]==goalNode and temp[1]<=cost):
                return "Reached",path
            tempTree = trees[temp[0]]
            if(len(tempTree)==0):
                return "Local Optima Reached",path
            if(temp[1]>cost):
                return "Dead End: Optima Reached",path[:-1]
            cost = temp[1]
            ahem = tempTree.copy()
            ok = []
            for values in ahem:
                ok.append([values,hue[values]])
            queue = ok.copy()
        return self.findPath(startNode, goalNode, hue, queue, path,cost)

n = Nodes(g)
n.showNodes() # displays all nodes..


startNode = input("Enter start node : ")
goalNode = input("Enter goal node : ")
print(hue)
checker,Path = n.findPath(startNode,goalNode,hue) #displays
print(checker)
print("Order of Nodes -> ",Path)
# print("Solution Path -> ",Path)
# print("Cost -> ",costy)

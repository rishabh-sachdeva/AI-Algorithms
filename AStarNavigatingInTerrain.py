#HOMEWORK 2 - NAVIGATING TERRAIN PROBLEM
#A* SEARCH BY RISHABH SACHDEVA

def solve(start,goal,matrix):
    gScore={} # cost to reach goal
    fScore={} # total cost = cost to reach node + heuristic value
    hScore={} # heuristic cost
    gScore[start]=0
    hScore[start]=0
    fScore[start]=hScore[start]
    costDict={'p':10,'m':100,'s':30} # costs corresponding to path,mountain and sand.
    calculateHeuristic(start,goal)
    openNodes=set()     #set of visited coordinates
    closedNodes=set()   #set of unvisited coordinates
    
    openNodes.add(start)
    cameFrom={}

    #s=start
    #minCost=fScore[s]
    #lastVisitedNode=start

    while(len(openNodes)>0):
        minCost=min(fScore[s] for s in openNodes)
        for node in openNodes:
            if(fScore[node]==minCost):
                minCostNode=node
                break
        minCost=fScore[minCostNode]
        if minCostNode==goal:              
            return structurePath(cameFrom, start, goal, matrix, costDict);  #GOAL TEST
        openNodes.remove(minCostNode)
        closedNodes.add(minCostNode)
        northNeighbor=None
        southNeighbor=None
        eastNeighbor=None
        westNeighbor=None
        
        #Expanding the minimum valued node
        if(minCostNode[0]!=0):
            northNeighbor = (minCostNode[0]-1,minCostNode[1])
            if(northNeighbor not in closedNodes):
                openNodes.add(northNeighbor)
                tentative_cost=calculateF(goal, matrix, gScore, fScore, hScore, costDict, northNeighbor,cameFrom,minCostNode)
                if northNeighbor in fScore.keys() and fScore[northNeighbor]>tentative_cost:
                    cameFrom[northNeighbor]=minCostNode
                    fScore[northNeighbor]=tentative_cost
                    gScore[northNeighbor] = costDict[matrix[northNeighbor[0]][northNeighbor[1]]] + gScore[minCostNode]
                elif northNeighbor not in fScore.keys():
                    cameFrom[northNeighbor]=minCostNode
                    fScore[northNeighbor]=tentative_cost
                    gScore[northNeighbor] = costDict[matrix[northNeighbor[0]][northNeighbor[1]]] + gScore[minCostNode]

        if(len(matrix)-1  != minCostNode[0]):
            southNeighbor = (minCostNode[0]+1,minCostNode[1])
            if(southNeighbor not in closedNodes):
                openNodes.add(southNeighbor)
                tentative_cost=calculateF(goal, matrix, gScore, fScore, hScore, costDict, southNeighbor,cameFrom,minCostNode)
                if southNeighbor in fScore.keys() and fScore[southNeighbor]>tentative_cost:
                    cameFrom[southNeighbor]=minCostNode
                    fScore[southNeighbor]=tentative_cost
                    gScore[southNeighbor] = costDict[matrix[southNeighbor[0]][southNeighbor[1]]] + gScore[minCostNode]
                elif southNeighbor not in fScore.keys():
                    cameFrom[southNeighbor]=minCostNode
                    fScore[southNeighbor]=tentative_cost
                    gScore[southNeighbor] = costDict[matrix[southNeighbor[0]][southNeighbor[1]]] + gScore[minCostNode]

        if(len(matrix)-1  != minCostNode[1]):
            eastNeighbor = (minCostNode[0],minCostNode[1]+1)
            if(eastNeighbor not in closedNodes):
                openNodes.add(eastNeighbor)
                tentative_cost=calculateF(goal, matrix, gScore, fScore, hScore, costDict, eastNeighbor,cameFrom,minCostNode)
                if eastNeighbor in fScore.keys() and fScore[eastNeighbor]>tentative_cost:
                    cameFrom[eastNeighbor]=minCostNode
                    fScore[eastNeighbor]=tentative_cost
                    gScore[eastNeighbor] = costDict[matrix[eastNeighbor[0]][eastNeighbor[1]]] + gScore[minCostNode]
                elif eastNeighbor not in fScore.keys():
                    cameFrom[eastNeighbor]=minCostNode
                    fScore[eastNeighbor]=tentative_cost
                    gScore[eastNeighbor] = costDict[matrix[eastNeighbor[0]][eastNeighbor[1]]] + gScore[minCostNode]

        if(minCostNode[1]!=0):
            westNeighbor = (minCostNode[0],minCostNode[1]-1)
            if(westNeighbor not in closedNodes):
                openNodes.add(westNeighbor)
                tentative_cost=calculateF(goal, matrix, gScore, fScore, hScore, costDict, westNeighbor,cameFrom,minCostNode)
                if westNeighbor in fScore.keys() and fScore[westNeighbor]>tentative_cost:
                    cameFrom[westNeighbor]=minCostNode
                    fScore[westNeighbor]=tentative_cost
                    gScore[westNeighbor] = costDict[matrix[westNeighbor[0]][westNeighbor[1]]] + gScore[minCostNode]
                elif westNeighbor not in fScore.keys():
                    cameFrom[westNeighbor]=minCostNode
                    fScore[westNeighbor]=tentative_cost
                    gScore[westNeighbor] = costDict[matrix[westNeighbor[0]][westNeighbor[1]]] + gScore[minCostNode]

def structurePath(cameFrom,startNode,goalNode,matrix,costDict):
    node=goalNode
    path=""
    while(node != startNode):
        pNode=cameFrom[node]
        if pNode[1]-node[1]==-1:
            path=path +'E'
        elif pNode[1]-node[1]==1:
            path=path +'W'
        elif pNode[0]-node[0]==-1:
            path = path + 'S'
        else:
            path=path +'N'
        node=pNode
    return path[::-1] # reverse generated path.
    
def calculateF(goal, matrix, g, f, h, costDict, neighbor, cameFrom, minCostNode):
    gVal=costDict[matrix[neighbor[0]][neighbor[1]]] + g[minCostNode]
    h[neighbor] = calculateHeuristic(neighbor, goal)
    return gVal + h[neighbor]
    
def calculateHeuristic(start,goal):
    xDist=abs(goal[0]-start[0])   #minimum x steps required.
    yDist=abs(goal[1]-start[1])   #minimum y steps required.
    return (xDist+yDist)*10  # return Manhattan distance-heuristic   
    

#k= solve((2,2),(0,0),[['m','m','m','s'],['m','m','m','s'],['m','m','m','s'],['p','p','p','p']])
k= solve((1,0),(2,2),[['p','p','p'],['p','m','p'],['s','s','s']])
print(k)

#MAIN CODE FOR SHORTES ROUTE
import subprocess

answer = "null"



def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """    
    # a few sanity checks
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')    
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        global answer
        answer = 'shortest path: '+str(path)+"Distance: "+str(distances[dest])+"m"
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)


#Get start and finish
start = raw_input("Start Location: ")
end = raw_input("End Location: ")

#Graph:
graph = {'A1': {'A2': 10, 'A20': 41, 'A24': 33.5},
    'A2': {'A1': 10, 'A7': 59.25},
    'A7': {'A2': 59.25, 'A14': 47, 'A8': 15},
    'A8': {'A9': 4.75, 'A7': 15},
    'A9': {'A10': 7, 'A9': 4.75},
    'A10': {'A11': 26.25, 'A9': 7, 'A36': 31},
    'A11': {'A12': 7, 'A10': 29.25},
    'A12': {'A37': 23.50, 'A13': 14, 'A11': 7},
    'A13': {'A12': 14, 'A14': 11.25},
    'A14': {'A7': 47, 'A15': 9.75},
    'A15': {'A14': 9.75, 'A16': 10},
    'A16': {'A17': 10, 'A15': 10},
    'A17': {'A16': 10, 'A18': 10},
    'A18': {'A17': 10, 'A19': 16.75, 'A43': 21.75, 'A2': 49.75},
    'A19': {'A18': 17, 'A20': 10},
    'A20': {'A19': 10, 'A22': 20},
    'A22': {'A20': 20},
    'A23': {'A24': 2.75, 'A47': 41},
    'A24': {'A25': 17, 'A23': 2.75},
    'A25': {'A26': 10, 'A24': 17},
    'A26': {'A27': 10, 'A25': 10},
    'A27': {'A25': 10, 'A28': 10},
    'A28': {'A27': 10, 'A30': 20},
    'A30': {'A28': 20}}


#Runs dijkstra function (which prints data)
dijkstra(graph, end, start)

print answer

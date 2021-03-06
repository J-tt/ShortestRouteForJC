#MAIN CODE FOR SHORTEST ROUTE ALPHA 1.2


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
        answer = 'Route'+str(path)+'Distance: '+str(distances[dest])+'m'
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

def cls(): print "\n" * 100

#Graph:
graph = {'A1': {'A2': 10, 'A20': 41, 'A24': 33.5, 'E1': 59.25},
    'A2': {'A1': 10, 'A7': 59.25, 'A18': 49.75},
    'A7': {'A2': 59.25, 'A14': 47, 'A8': 15},
    'A8': {'A9': 4.75, 'A7': 15},
    'A9': {'A10': 7, 'A9': 4.75, 'B1': 22.25},
    'A10': {'A11': 26.25, 'A9': 7, 'A36': 31, 'A30': 49.75},
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
    'A22': {'A20': 20, 'E6': 23.5},
    'A23': {'A24': 2.75, 'A47': 41},
    'A24': {'A25': 17, 'A23': 2.75},
    'A25': {'A26': 10, 'A24': 17},
    'A26': {'A27': 10, 'A25': 10},
    'A27': {'A25': 10, 'A28': 10},
    'A28': {'A27': 10, 'A30': 20},
    'A30': {'A28': 20, 'A31': 5.75, 'A10': 49.75},
    'A31': {'A32': 16.5, 'A30': 5.75},
    'A32': {'A31': 16.5, 'A33': 16.75},
    'A33': {'A32': 16.75, 'A34': 4.25},
    'A34': {'A33': 4.25, 'A35': 6.25},
    'A35': {'A34': 6.25, 'A36': 20.25},
    'A36': {'A35': 20.25, 'A37': 13.25},
    'A37': {'A36': 13.25, 'A38': 14},
    'A38': {'A37': 14, 'A39': 10},
    'A39': {'A38': 10, 'A40': 10},
    'A40': {'A39': 10, 'A41': 20.25},
    'A41': {'A40': 20, 'A42': 10},
    'A42': {'A40': 20, 'A43': 10},
    'A43': {'A41': 20, 'A44': 16.25},
    'A44': {'A43': 16.25, 'A45': 10},
    'A45': {'A44': 10, 'A46': 10},
    'A46': {'A45': 10, 'A47': 10},
    'A47': {'A48': 6.75, 'A49': 3, 'A23': 41},
    'A48': {'A47': 6.75, 'A49': 4.25},
    'A49': {'A47': 3, 'A48': 4.25},
    'E6': {'D1': 53.5, 'A22': 23.5},
    'E1': {'A1': 59.25},
    'D1': {'E6': 53.5},
    'B1': {'A9': 22.25},
    'B2': {'B1': 24}}

print('Please read attached instructions before continuing!')
print "Press any key to continue"
a=raw_input()
loopCont = '1'
while loopCont == '1':
    cls()
    start = raw_input("Start Location: ")
    end = raw_input("End Location: ")
    dijkstra(graph, end, start)
    print(answer)
    print "Press any key to continue"
    a=raw_input()

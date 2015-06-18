"""Main Code For Shortest Route"""
import fuckit
import tkinter as tk
import subprocess





#CODE BY http://geekly-yours.blogspot.com.au/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html


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
        print('shortest path: '+str(path)+" cost="+str(distances[dest])) 
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

#END CODE BY GEEKLY

print('You are at A1, you can go to: A2, A3 or A4')
end = input('Which one do you choose: ')

#SAMPLE DATA
graph = {'A1': {'A2': 2, 'A3': 2, 'A4': 4},
    'A2': {'A1': 2, 'A4': 2},
    'A3': {'A1': 2, 'A4': 1},
    'A4': {'A2': 2, 'A3': 1}}

dijkstra(graph, end, 'A1')

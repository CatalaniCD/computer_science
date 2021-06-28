#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:17:30 2021

@author: q

Goal : Develop an implementation for graphs

    - Create a graph from an adjacency matrix
    
    - Apply Depth First Search
    
    - Apply Breadth First Search
    
    - Apply Cycle Detection
    
    - Apply Shortest Path

"""
   
def DFS(graph, start, end, path = []):
    """ Depth First Search """
    path += [start]
    # path found
    if start == end:
        return path    
    # check if start not in edge
    if not start in graph.keys():
        return None
    # explore nodes
    for node in graph[start]:   
        # avoid cycles
        if node not in path:        
            # step to the next edge until Termination Case
            newpath = DFS(graph, node, end, path)
            # after Termination Case
            if newpath: 
                return newpath  
    return None

def depth_first_search(graph, start, end):
       return DFS(graph, start, end, path = []) 

def DFS_Shortest_Path(graph, start, end, path = [], shortest = None):
    """ Depth First Search to find the shortest path """
    path = path + [start]
    # path found - termination case
    if start == end:
        return path
    # check if start not in edge
    if not start in graph.keys():
        return None
    # explore nodes
    for node in graph[start]:
        #avoid cycles
        if node not in path: 
            # check if no shortes or path_length < shortest_path
            if shortest == None or len(path) < len(shortest):
                # step until termination case
                newPath = DFS_Shortest_Path(graph, node, end, path, shortest)
                # after termiantion case
                if newPath != None:
                    shortest = newPath 
                    
    return shortest


def find_shortest_path(graph, start, end):
    return DFS_Shortest_Path(graph, start, end)


def BFS(graph, start, end, path = [], toPrint = False):
    """ Breadth First Search """
    # create the initial path
    initPath = [start]
    # queue of paths
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        # remove the oldest element in path queue
        tmpPath = pathQueue.pop(0)
        # keep track of last node in the path
        lastNode = tmpPath[-1]
        # check last node is the search element
        if lastNode == end:
            return tmpPath
        for nextNode in graph[lastNode]:
            if nextNode not in tmpPath:
                # add new step to the search paths
                newPath = tmpPath + [nextNode]
                # add new path to eval in the next iteration
                pathQueue.append(newPath)
    
    return None


def breadth_first_search(graph, start, end):
    return BFS(graph, start, end)


def graph_from_matrix(matrix):    
    """ Create a graph from an adjacency matrix """
    rows = range(len(matrix))
    columns = range(len(matrix[0]))
            
    graph = { x : [] for x in rows }
    
    for row in rows:
        for column in columns:
            if matrix[row][column]:
                graph[row] += [column]
    
    return graph
    

def DFS_cycle(graph, start, path = []):
    """ Detect Cycles with a Depth First Search """
    # append to path
    path = path + [start]
    
    # graph start
    for node in graph[start]:
        # check if node != path init        
        if node not in path:          
            
            # return true after termination case
            if DFS_cycle(graph, node, path):
                return True      
            
        # return true before termination case
        elif node == path[0]:
            return True
    
def detect_cycle(graph):
    nodes = { x : False for x in graph.keys() }     
    for node in graph.keys():
        nodes[node] = DFS_cycle(graph, start = node)
    return nodes 
 
    
if __name__ == '__main__':
    
    # create a graph from an adjacency matrix
    WIDE = True

    if WIDE:
    
        matrix = [ [False, False, False, True,  False ], 
                    [False, True,  True,  True,  False ],
                    [False, True,  False, False, True  ],
                    [False, True,  True,  False, True  ],
                    [False, True,  False, True,  True  ] ]
    else:

        matrix = [ [False, False, True,], 
                   [False, True,  True, ],
                   [False, True,  False,] ]
                   
    graph = graph_from_matrix(matrix)
        
    print(f'\n=== graph ===\n{graph}\n')

    print(f'\n=== detect cycles ===\n{detect_cycle(graph)}\n')     
        
    print(f'\n=== depth first search ===\npath : {depth_first_search(graph, 2, 4)}\n')
    
    print(f'\n=== breadth first search / shortest path BFS ===\npath : {breadth_first_search(graph, 2, 4)}\n')

    print(f'\n=== find shortest path DFS ===\npath : {find_shortest_path(graph, 2, 4)}\n')
        
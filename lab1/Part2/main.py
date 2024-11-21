import openpyxl
from Algorithms import *
import time

def thisGraphComparator(newNode:tuple,node:tuple):
    return newNode[1]>=node[1]
def thisHeuristicComparator(newNode:tuple, node:tuple):
    return newNode[3]>=node[3]
def thisFComparator(newNode:tuple, node:tuple):
    return newNode[4]>=node[4]
def main():
    heuristicPath = "/home/diggsy/UVG/UVGIA/Documents/heuristica.xlsx"
    costPath = "/home/diggsy/UVG/UVGIA/Documents/funcion_de_costo.xlsx"
    wb_heuristic = openpyxl.load_workbook(heuristicPath)
    wb_cost = openpyxl.load_workbook(costPath)
    # Get the first sheet 
    sheet = wb_heuristic.worksheets[0] 
    heuristicFunction = {}
    for i, row in enumerate(sheet):
        if i == 0 : continue
        # Nombre del nodo
        node_name =row[0].value
        # Funcion euristica
        heuristicValue=row[1].value
        heuristicFunction[node_name]=heuristicValue        
    sheet = wb_cost.worksheets[0] 
    graph = {}
    for i, row in enumerate(sheet): 
        # Skip the first row (the row with the column names) 
        if i == 0: continue
        # Nombre del nodo
        node_name =row[0].value
        # Direccion
        direction = row[1].value
        # Costo
        cost = row[2].value
        # Si ya fue aniadido el nodo al diccionario entonces solo se aniade el destino y el costo
        if graph.get(node_name) is not None:
            graph[node_name].append((direction,cost))
        # Es un nuevo nodo
        else:
            graph[node_name]=[(direction,cost)]
            
    # print(graph)
    # print(heuristicFunction)
    
    print("Breadth First Search without a final node", end=":\n")
    start_time = time.time()
    BreadthFirstSearch(graph,"Warm-up activities")
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nBreadth First Search with a final node", end=":\n")
    start_time = time.time()
    BreadthFirstSearch(graph,"Warm-up activities", "Stretching")
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nDepth First Search without a final node", end=":\n")
    start_time = time.time()
    DepthFirstSearch(graph,  "Warm-up activities")
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")

    print("\n\nDepth First Search with a final node", end=":\n")
    start_time = time.time()
    DepthFirstSearch(graph,  "Warm-up activities", "Stretching")
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nUniform Cost Search with a final node", end=":\n")
    start_time = time.time()
    UniformCostSearch(thisGraphComparator, graph,  "Warm-up activities", "Stretching")
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    print("\n\nGreedy Best First Search with a final node", end=":\n")
    start_time = time.time()
    GreedyBestFirstSearch(thisHeuristicComparator, graph,  "Warm-up activities", "Stretching", heuristicFunction)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    print("\n\nA* Search with a final node", end=":\n")
    start_time = time.time()
    AStarSearch(thisFComparator, graph,  "Warm-up activities", "Stretching", heuristicFunction)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
# Using the special variable
# __name__
if __name__=="__main__":
    main()
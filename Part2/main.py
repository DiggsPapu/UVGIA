import openpyxl
from Algorithms import *

def thisGraphComparator(newNode:tuple,node:tuple):
    return newNode[1]>=node[1]
def main():
    heuristicPath = "/home/diggsy/UVG/UVGIA/Documents/heuristica.xlsx"
    costPath = "/home/diggsy/UVG/UVGIA/Documents/funcion_de_costo.xlsx"
    wb_heuristic = openpyxl.load_workbook(heuristicPath)
    wb_cost = openpyxl.load_workbook(costPath)
    # Get the first sheet 
    # sheet = wb_heuristic.worksheets[0] 
    sheet = wb_cost.worksheets[0] 
    graph = {}
    for i, row in enumerate(sheet): 
        # Skip the first row (the row with the column names) 
        if i == 0: 
            continue
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
            
    print(graph)
    print("Breadth First Search without a final node", end=":\n")
    BreadthFirstSearch(graph,"Warm-up activities")
    
    print("\n\nBreadth First Search with a final node", end=":\n")
    BreadthFirstSearch(graph,"Warm-up activities", "Incline Bench")
    
    print("\n\nDepth First Search without a final node", end=":\n")
    DepthFirstSearch(graph,  "Warm-up activities")
    
    print("\n\nDepth First Search with a final node", end=":\n")
    DepthFirstSearch(graph,  "Warm-up activities", "Skipping Rope")
    
    print("\n\nUniform Cost Search with a final node", end=":\n")
    UniformCostSearch(thisGraphComparator, graph,  "Warm-up activities", "Stretching")
    
# Using the special variable
# __name__
if __name__=="__main__":
    main()
import openpyxl
from Algorithms import *
import time
from Labyrinth import *
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
# if __name__=="__main__":
#     main()
matrix = generateBasicLabyrinth()
graph = {}
entranceNode = None
objectiveNode = None
for i in range(0,len(matrix)): 
    for j in range(0,len(matrix[0])):    
        # Si es pared no se aniadira como nodo 
        if matrix[i][j]!=0:
            # Nombre del nodo
            node_name = str(i)+"-"+str(j)
            # Se agarra la direccion derecha, izquierda, arriba y abajo
            directions = []
            # No se puede mover a la izquierda si es el primer nodo de cada fila
            if j!=0 and matrix[i][j-1]!=0:
                directions.append((str(i)+"-"+str(j-1),1))
            # No se puede mover a la derecha si es el ultimo nodo de cada fila
            if j!=len(matrix[0])-1 and matrix[i][j+1]!=0:
                directions.append((str(i)+"-"+str(j+1),1))
            # No se puede mover hacia arriba si es alguno de los nodos de la fila 0
            if i!=0 and matrix[i-1][j]!=0:
                directions.append((str(i-1)+"-"+str(j),1))
            # No se puede mover hacia abajo si es alguno de los nodos de la fila 64    
            if i!=len(matrix)-1 and matrix[i+1][j]!=0:
                directions.append((str(i+1)+"-"+str(j),1))
            graph[node_name]=[]
            for direction in directions:
                graph[node_name].append(direction)
        if matrix[i][j]==3:
            finalNode = str(i)+"-"+str(j)
        if matrix[i][j]==2:
            entranceNode = str(i)+"-"+str(j)
            
print("\n\nBreadth First Search with a final node", end=":\n")
start_time = time.time()
BreadthFirstSearch(graph=graph, init_node=entranceNode, goal_node=finalNode)
elapsed_time = -start_time + time.time()
print("Elapsed time:", elapsed_time, " s")
    
        

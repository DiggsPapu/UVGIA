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

    print("Breadth First Search without a final node", end=":\n")
    start_time = time.time()
    BreadthFirstSearch(graph,entranceNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nBreadth First Search with a final node", end=":\n")
    start_time = time.time()
    BreadthFirstSearch(graph,entranceNode,finalNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nDepth First Search without a final node", end=":\n")
    start_time = time.time()
    DepthFirstSearch(graph,entranceNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")

    print("\n\nDepth First Search with a final node", end=":\n")
    start_time = time.time()
    DepthFirstSearch(graph,  "Warm-up activities", "Stretching")
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nUniform Cost Search with a final node", end=":\n")
    start_time = time.time()
    UniformCostSearch(thisGraphComparator, graph,entranceNode,finalNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    # print("\n\nGreedy Best First Search with a final node", end=":\n")
    # start_time = time.time()
    # GreedyBestFirstSearch(thisHeuristicComparator, graph,entranceNode,finalNode, heuristicFunction)
    # elapsed_time = -start_time + time.time()
    # print("Elapsed time:", elapsed_time, " s")
    
    # print("\n\nA* Search with a final node", end=":\n")
    # start_time = time.time()
    # AStarSearch(thisFComparator, graph,entranceNode,finalNode, heuristicFunction)
    # elapsed_time = -start_time + time.time()
    # print("Elapsed time:", elapsed_time, " s")
# Using the special variable
__name__
if __name__=="__main__":
    main()
    
        

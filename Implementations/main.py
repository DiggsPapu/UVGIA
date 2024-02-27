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
    matrix_path = "./test_maze.txt"
    matrix = []
    with open(matrix_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
        for  line in file_contents.split('\n'):
            matrix.append([int(item) for item in list(line)])
    # matrix = generateBasicLabyrinth()
    graph = {}
    entranceNode = None
    finalNode = None
    for i in range(0,len(matrix)): 
        for j in range(0,len(matrix[0])):    
            # Si es pared no se aniadira como nodo 
            if matrix[i][j]>0:
                # Nombre del nodo
                node_name = str(i)+"-"+str(j)
                # Se agarra la direccion derecha, izquierda, arriba y abajo
                directions = []
                # No se puede mover a la izquierda si es el primer nodo de cada fila
                if j!=0 and matrix[i][j-1]>=1:
                    directions.append((str(i)+"-"+str(j-1),1))
                # No se puede mover a la derecha si es el ultimo nodo de cada fila
                if j!=len(matrix[0])-1 and matrix[i][j+1]!=0:
                    directions.append((str(i)+"-"+str(j+1),1))
                # No se puede mover hacia arriba si es alguno de los nodos de la fila 0
                if i!=0 and matrix[i-1][j]>=1:
                    directions.append((str(i-1)+"-"+str(j),1))
                # No se puede mover hacia abajo si es alguno de los nodos de la fila 64    
                if i!=len(matrix)-1 and matrix[i+1][j]>=1:
                    directions.append((str(i+1)+"-"+str(j),1))
                graph[node_name]=[]
                for direction in directions:
                    graph[node_name].append(direction)
            if matrix[i][j]==3:
                finalNode = str(i)+"-"+str(j)
            if matrix[i][j]==2:
                entranceNode = str(i)+"-"+str(j)
    keys_list = list(graph.keys())
    euclideanHeuristic = {}
    manhattanHeuristic = {}
    fI, fJ = finalNode.split( "-")
    for key in keys_list:
        i, j = key.split("-")
        node_name =key
        # Funcion euristica euclideana
        euclideanValue= ((int(fI)-int(i))**2+(int(fJ)-int(j))**2)**(0.5)
        euclideanHeuristic[node_name]=euclideanValue
        # Funcion euristica manhattan
        manhattanValue= abs(int(fI)-int(i))+abs(int(fJ)-int(j))
        euclideanHeuristic[node_name]=manhattanValue
        manhattanHeuristic[node_name]=manhattanValue
    print("Breadth First Search without a final node", end=":\n")
    start_time = time.time()
    BreadthFirstSearch(graph, entranceNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nBreadth First Search with a final node", end=":\n")
    start_time = time.time()
    BreadthFirstSearch(graph, entranceNode, finalNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    
    print("\n\nDepth First Search without a final node", end=":\n")
    start_time = time.time()
    DepthFirstSearch(graph, entranceNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")

    print("\n\nDepth First Search with a final node", end=":\n")
    start_time = time.time()
    DepthFirstSearch(graph, entranceNode, finalNode)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    print("\n\nDepth Limited Search", end=":\n")
    start_time = time.time()
    DepthDelimitedSearch(graph, entranceNode, finalNode,300)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    print("\n\nGreedy Best First Search with euclidean heuristic", end=":\n")
    start_time = time.time()
    GreedyBestFirstSearch(thisHeuristicComparator, graph,entranceNode,finalNode, euclideanHeuristic)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    print("\n\nGreedy Best First Search with manhattan heuristic", end=":\n")
    start_time = time.time()
    GreedyBestFirstSearch(thisHeuristicComparator, graph,entranceNode,finalNode, manhattanHeuristic)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    print("\n\nA* Search with a euclidean heuristic", end=":\n")
    start_time = time.time()
    AStarSearch(thisFComparator, graph,entranceNode,finalNode, euclideanHeuristic)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
    
    print("\n\nA* Search with a manhattan heuristic", end=":\n")
    start_time = time.time()
    AStarSearch(thisFComparator, graph,entranceNode,finalNode, euclideanHeuristic)
    elapsed_time = -start_time + time.time()
    print("Elapsed time:", elapsed_time, " s")
# Using the special variable
__name__
if __name__=="__main__":
    main()
    
        

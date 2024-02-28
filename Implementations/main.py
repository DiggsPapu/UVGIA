from Algorithms import *
import time
import pygame
from Labyrinth import *
def thisGraphComparator(newNode:tuple,node:tuple):
    return newNode[1]>=node[1]
def thisHeuristicComparator(newNode:tuple, node:tuple):
    return newNode[3]>=node[3]
def thisFComparator(newNode:tuple, node:tuple):
    return newNode[4]>=node[4]
def createRoute(path, route):
    route = []
    for nodeName in path:
        i, j = nodeName.split("-")
        route.append((i, j))
    return route
def main():
    # matrix_path = "./test_maze.txt"
    # matrix = []
    # with open(matrix_path, 'r') as file:
    #     # Read the contents of the file
    #     file_contents = file.read()
    #     for  line in file_contents.split('\n'):
    #         matrix.append([int(item) for item in list(line)])
    # matrix = generateBasicLabyrinth()
    matrix = generate_labyrinth(64, 64)
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
    
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = 800, 800  # Set the window dimensions
    CELL_SIZE = WIDTH // 64
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labyrinth")
    isRunning = True
    route = []
    algorithm_name = None
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
            # Exit
                if event.key == pygame.K_ESCAPE:
                    isRunning = False
                # bfs1P
                if event.key == pygame.K_1:
                    print("Breadth First Search without a final node", end=":\n")
                    start_time = time.time()
                    bfs1P = BreadthFirstSearch(graph, entranceNode)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(bfs1P, route)
                    algorithm_name = "bfs1P"
                elif event.key == pygame.K_2:
                    print("\n\nBreadth First Search with a final node", end=":\n")
                    start_time = time.time()
                    bfs2P = BreadthFirstSearch(graph, entranceNode, finalNode)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(bfs2P, route)
                    algorithm_name = "bfs2P"
                elif event.key == pygame.K_3:
                    print("\n\nDepth First Search without a final node", end=":\n")
                    start_time = time.time()
                    dfs1P = DepthFirstSearch(graph, entranceNode)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(dfs1P, route)
                    algorithm_name = "dfs1P"
                elif event.key == pygame.K_4:
                    print("\n\nDepth First Search with a final node", end=":\n")
                    start_time = time.time()
                    dfs2P = DepthFirstSearch(graph, entranceNode, finalNode)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(dfs2P, route)
                    algorithm_name = "dfs2P"
                elif event.key == pygame.K_5:
                    print("\n\nDepth Limited Search", end=":\n")
                    start_time = time.time()
                    ddsP = DepthDelimitedSearch(graph, entranceNode, finalNode,1000)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(ddsP, route)
                    algorithm_name = "ddsP"
                elif event.key == pygame.K_6:
                    print("\n\nGreedy Best First Search with euclidean heuristic", end=":\n")
                    start_time = time.time()
                    gbfsEP = GreedyBestFirstSearch(thisHeuristicComparator, graph,entranceNode,finalNode, euclideanHeuristic)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(gbfsEP, route)
                    algorithm_name = "gbfsEP"
                elif event.key == pygame.K_7:
                    print("\n\nGreedy Best First Search with manhattan heuristic", end=":\n")
                    start_time = time.time()
                    gbfsMP = GreedyBestFirstSearch(thisHeuristicComparator, graph,entranceNode,finalNode, manhattanHeuristic)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(gbfsMP, route)
                    algorithm_name = "gbfsMP"
                elif event.key == pygame.K_8:
                    print("\n\nA* Search with a euclidean heuristic", end=":\n")
                    start_time = time.time()
                    assEP = AStarSearch(thisFComparator, graph,entranceNode,finalNode, euclideanHeuristic)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(assEP, route)
                    algorithm_name = "assEP"
                elif event.key == pygame.K_9:
                    print("\n\nA* Search with a manhattan heuristic", end=":\n")
                    start_time = time.time()
                    assMP = AStarSearch(thisFComparator, graph,entranceNode,finalNode, manhattanHeuristic)
                    elapsed_time = -start_time + time.time()
                    print("Elapsed time:", elapsed_time, " s")
                    route = createRoute(assMP, route)
                    algorithm_name = "assMP"
                elif event.key == pygame.K_0:
                    route = []
                    algorithm_name = None
        if algorithm_name is None:
            window.fill((0, 0, 0))  # Fill the window with a black color
            for i in range(64):
                for j in range(64):
                    color = (0, 0, 0) if matrix[i][j] == 0 else (255, 255, 255)
                    pygame.draw.rect(window, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
            for i in range(64):
                for j in range(64):
                    if matrix[i][j] == 2:
                        pygame.draw.rect(window, (0, 255, 0), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    elif matrix[i][j] == 3:
                        pygame.draw.rect(window, (255, 0, 0), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        else:            
            for i, j in route:
                pygame.draw.rect(window, (255, 165, 0), (int(j) * CELL_SIZE, int(i) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.display.flip()  # Update the display after each node
                pygame.time.delay(2)  # Add a delay between nodes
                
            if algorithm_name is not None:
                pygame.image.save(window, algorithm_name+".png")
        pygame.display.flip()
        clock.tick(60)  # Limit frames per second
# Using the special variable
__name__
if __name__=="__main__":
    main()
    
        

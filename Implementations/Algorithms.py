from DataStructures import *
def BreadthFirstSearch(graph: dict, init_node:str, goal_node:str=None):
    iteration = 0
    # Inicializo mi cola fifo junto con un array de nodos visitados
    queue = fifo([])
    visited = []
    # Aniado el nodo inicial a los nodos visitados y lo inserto en la cola
    visited.append(init_node)
    queue.insert(init_node)
    path = []
    # se efectua mientras no este vacia la cola
    while queue.empty()==False:
        iteration +=1
        neighbours = graph.get(queue.first())
        if goal_node is not None and queue.first()==goal_node:
            nnode = queue.remove_first()
            print(nnode)
            path.append(nnode)
            break
        else:
            nnode = queue.remove_first()
            print(nnode, end=" -> ")
            path.append(nnode)
            if neighbours is not None:
                # Se visitan los vecinos y se insertan en la cola para ser explorados
                for node in neighbours:
                    node_name = node[0]
                    if visited.count(node_name)<1:
                        queue.insert(node_name)
                        visited.append(node_name)
    print("\nIteraciones en el while: "+str(iteration))
    return path

def DepthFirstSearch(graph:dict, init_node:str, goal_node:str=None):
    iteration = 0
    # Inicializo mi cola lifo junto con un array de nodos visitados
    queue = lifo([])
    visited = []
    queue.insert(init_node)
    path = []
    # Mientras que no este vacia la cola se realiza esto
    while queue.empty()==False:
        iteration +=1
        # Se remueve el nodo de la cola
        peek_node = queue.remove_first()
        if goal_node is not None and peek_node==goal_node:
            print(peek_node)
            path.append(peek_node)
            break
        print(peek_node, end=" -> ")
        path.append(peek_node)
        # Se obtienen los nodos adyacentes
        set_adjacent = graph.get(peek_node)
        if peek_node not in visited:
            # Se marca como nodo visitado
            visited.append(peek_node)
            if set_adjacent is not None:
                # Se aniaden todos los nodos adyacentes que no han sido visitados a la cola
                for node in set_adjacent:
                    # Si no ha sido visitado se aniade a la cola
                    if visited.count(node[0])<1:
                        queue.insert(node[0])
    print("\nIteraciones en el while: "+str(iteration))
    return path
    
def DepthDelimitedSearch(graph:dict, init_node:str, goal_node:str=None, limit_depth=50):
    iteration = 0
    # Inicializo mi cola lifo junto con un array de nodos visitados
    queue = lifo([])
    visited = []
    current_depth = 0
    queue.insert((init_node, current_depth))
    ya = False
    path = []
    # Mientras que no este vacia la cola se realiza esto
    while queue.empty()==False:
        iteration +=1
        # Se remueve el nodo de la cola
        peek_node, current_depth = queue.remove_first()
        if goal_node is not None and peek_node==goal_node:
            print(peek_node)
            path.append(peek_node)
            ya = True
            break
        print(peek_node, end=" -> ")
        path.append(peek_node)
        # Se obtienen los nodos adyacentes
        set_adjacent = graph.get(peek_node)
        if peek_node not in visited and current_depth<limit_depth:
            # Se marca como nodo visitado
            visited.append(peek_node)
            if set_adjacent is not None:
                # Se aniaden todos los nodos adyacentes que no han sido visitados a la cola
                for node in set_adjacent:
                    # Si no ha sido visitado se aniade a la cola
                    if visited.count(node[0])<1:
                        queue.insert((node[0],current_depth+1))
                
    print("\nIteraciones en el while: "+str(iteration))
    if (ya == False):
        print("No se encontró el nodo objetivo")
    else:
        print("Se encontró el nodo objetivo")
    return path
     
def UniformCostSearch(comparator, graph:dict, init_node:str, goal_node:str):
    iteration = 0
    queue = priority([],comparator)
    visited = []
    # los nodos almacenados en la cola sera el nombre del nodo, su costo y su trayecto
    queue.insert((init_node,0,[init_node]))
    while queue.empty()==False:
        iteration +=1
        peek_node = queue.remove_first()
        # Siempre y cuando no se hayan visitado ya los nodos, se van a explotar
        if peek_node[0] not in visited:
            # Se aniade el nodo a la lista de los nodos visitados
            visited.append(peek_node)
            # En caso de que sea el nodo objetivo se termina el ciclo
            if peek_node[0] == goal_node:
                for  i in range(len(peek_node[2])):
                    print(peek_node[2][i],end='->')
                print(str(peek_node[1]))
                break
            else:
                # Selecciono los nodos adyacentes del grafo
                children = graph[peek_node[0]]
                # Siempre y cuando lleve a algun lado
                if children is not None:
                    # Se va a recorrer todos los nodos hijos
                    for child in children:
                        route = []
                        route.extend(peek_node[2])
                        route.append(child[0])
                        # Se encola y se calcula el costo total hasta ese nodo, ademas de que se realiza el trayecto hasta ese nodo
                        queue.insert((child[0],child[1]+peek_node[1],route))
    print("\nIteraciones en el while: "+str(iteration))
    # return path

def GreedyBestFirstSearch(comparator, graph:dict, init_node:str, goal_node:str, heuristicFunction:dict):
    iteration = 0
    queue = priority([], comparator)
    visited = []
    # los nodos almacenados en la cola sera el nombre del nodo, su costo, su trayecto y la funcion heuristica
    queue.insert((init_node,0,[init_node],heuristicFunction[init_node]))
    path = None
    while queue.empty() == False:
        iteration +=1
        # Se saca el nodo con el valor que determinamos en la heuristica y el comparator
        peek_node = queue.remove_first()
        # En caso de que sea el nodo objetivo se termina el ciclo
        if peek_node[0] not in visited:
            visited.append(peek_node[0])
            if peek_node[0] == goal_node:
                for  i in range(len(peek_node[2])):
                    print(peek_node[2][i],end='->')
                print(str(peek_node[1]))
                path = peek_node[2]
                path.append(peek_node[0])
                break       
            else:
                # Selecciono los nodos adyacentes del grafo
                children = graph[peek_node[0]]
                # Siempre y cuando lleve a algun lado
                if children is not None:
                    # Se va a recorrer todos los nodos hijos
                    for child in children:
                        route = []
                        route.extend(peek_node[2])
                        route.append(child[0])
                        # Se encola y se calcula el costo total hasta ese nodo, ademas de que se realiza el trayecto hasta ese nodo
                        queue.insert((child[0],child[1]+peek_node[1],route,heuristicFunction[child[0]]))
    print("\nIteraciones en el while: "+str(iteration)) 
    return path
       
def AStarSearch(comparator, graph: dict, init_node: str, goal_node: str, heuristicFunction: dict):
    iteration = 0
    queue = priority([], comparator)
    visited = []
    queue.insert((init_node, 0, [init_node], heuristicFunction[init_node]))
    path = None
    while not queue.empty():
        iteration += 1
        peek_node = queue.remove_first()
        if peek_node[0] not in visited:
            visited.append(peek_node[0])
            if peek_node[0] == goal_node:
                for i in range(len(peek_node[2])):
                    print(peek_node[2][i], end='->')
                print(str(peek_node[1]))
                path = peek_node[2]
                path.append(peek_node[0])
                break
            children = graph.get(peek_node[0])
            if children is not None:
                for child in children:
                    route = peek_node[2] + [child[0]]
                    total_cost = peek_node[1] + child[1]
                    f_value = total_cost + heuristicFunction[child[0]]
                    queue.insert((child[0], total_cost, route, heuristicFunction[child[0]], f_value))
    print("\nIterations:", iteration)
    return path
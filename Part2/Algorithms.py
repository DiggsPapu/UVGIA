from DataStructures import *

def BreadthFirstSearch(graph: dict, init_node:str, goal_node:str=None):
    # Inicializo mi cola fifo junto con un array de nodos visitados
    queue = fifo([])
    visited = []
    # Aniado el nodo inicial a los nodos visitados y lo inserto en la cola
    visited.append(init_node)
    queue.insert(init_node)
    # se efectua mientras no este vacia la cola
    while queue.empty()==False:
        neighbours = graph.get(queue.first())
        if goal_node is not None and queue.first()==goal_node:
            print(queue.remove_first())
            break
        print(queue.remove_first(), end=" -> ")
        if neighbours is not None:
            # Se visitan los vecinos y se insertan en la cola para ser explorados
            for node in neighbours:
                node_name = node[0]
                if visited.count(node_name)<1:
                    queue.insert(node_name)
                    visited.append(node_name)

def DepthFirstSearch(graph:dict, init_node:str, goal_node:str=None):
    # Inicializo mi cola lifo junto con un array de nodos visitados
    queue = lifo([])
    visited = []
    queue.insert(init_node)
    # Mientras que no este vacia la cola se realiza esto
    while queue.empty()==False:
        # Se remueve el nodo de la cola
        peek_node = queue.remove_first()
        if goal_node is not None and peek_node==goal_node:
            print(peek_node)
            break
        print(peek_node, end=" -> ")
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

    
def UniformCostSearch(comparator, graph:dict, init_node:str, goal_node:str):
    queue = priority([],comparator)
    visited = []
    # los nodos almacenados en la cola sera el nombre del nodo, su costo y su trayecto
    queue.insert((init_node,0,[init_node]))
    while queue.empty()==False:
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
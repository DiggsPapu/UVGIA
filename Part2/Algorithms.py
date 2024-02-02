from DataStructures import *

def BreadthFirstSearch(graph: dict, init_node:str):
    # Inicializo mi cola fifo junto con un array de nodos visitados
    queue = fifo([])
    visited = []
    # Aniado el nodo inicial a los nodos visitados y lo inserto en la cola
    visited.append(init_node)
    queue.insert(init_node)
    # se efectua mientras no este vacia la cola
    while queue.empty()==False:
        neighbours = graph.get(queue.first())
        print(queue.remove_first(), end=" -> ")
        if neighbours is not None:
            # Se visitan los vecinos y se insertan en la cola para ser explorados
            for node in neighbours:
                node_name = node[0]
                if visited.count(node_name)<1:
                    queue.insert(node_name)
                    visited.append(node_name)

def DepthFirstSearch(graph:dict, init_node:str):
    # Inicializo mi cola lifo junto con un array de nodos visitados
    queue = lifo([])
    visited = []
    queue.insert(init_node)
    # Mientras que no este vacia la cola se realiza esto
    while queue.empty()==False:
        # Se remueve el nodo de la cola
        peek_node = queue.remove_first()
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

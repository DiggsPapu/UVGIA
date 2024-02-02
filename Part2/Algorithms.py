from DataStructures import *

def BreadthFirstSearch(graph: dict, init_node:str, final_node:str):
    # Inicializo mi cola fifo junto con un array de nodos visitados
    queue = fifo([])
    visited = []
    # Aniado el nodo inicial a los nodos visitados y lo inserto en la cola
    visited.append(init_node)
    queue.insert(init_node)
    # se efectua mientras no este vacia la cola
    while queue.empty()==False:
        neighbours = graph.get(queue.first())
        # En caso de llegar al destino final se para
        if (queue.first()==final_node):
            print(queue.remove_first(), end="\n")    
            break
        print(queue.remove_first(), end=" -> ")
        # Se visitan los vecinos y se insertan en la cola para ser explorados
        for node in neighbours:
            node_name = node[0]
            queue.insert(node_name)
            visited.append(node_name)

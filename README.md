# Proyecto 1
## ¿Qué se hizo?
Esta branch contiene el proyecto 1 de inteligencia artificial, en la cuál se realizó una implementación propia de los algoritmos de:

* Breadth First Search: que se dedica a explotar cada nivel de un árgol hasta encontrar el nodo deseado.
* Depth First Search: que se dedica a explotar una rama del árbol hasta el fondo, y encontrar el nodo en cuestión.
* Depth Delimited Search: que se diferencia del anterior algoritmo porque en vez de llegar hasta el fondo de la rama, llega hasta cierta profundidad en el árbol.
* Greedy Best First Search: que a partir de una función heurística decidirá cuál es el nodo más prometedor entre los nodos hijos del nodo actual.
* A Star Search: este algoritmo busca utilizar las ventajas de la heurística con la búsqueda de costo uniforme.

Nota: para este proyecto se utilizaron dos funciones heurísticas para resolver el laberinto, una heurística basada en la distancia euclideana y otra heurística basada en la distancia manhattan.
## ¿Qué desafíos se tuvieron?
Realmente no se tuvieron desafíos de programación realmente graves. Sin embargo, esta sería una lista con los desafíos que se enfrentaron:
* Discernir cuáles serían las mejores estructuras de datos a utilizar para almacenar los nodos, en este caso se utilizaron diccionarios. Así mismo, para las llaves en este proyecto se utilizaron las posiciones j, i dentro de la matriz dado que eran valores únicos.
* ¿Cómo se implementaría la lectura del archivo de texto para la matriz?, de manera que estaba compuesto por 0, 1, 2 y 3 pero cómo adaptaríamos esta información a los diccionarios que almacenarían los nodos. En este caso se realizaría una lectura y pues se utilizarían los i, j como llaves, así mismo, los costos para moverse entre nodos sería 1. A su vez, se ignorarían todos aquellos nodos de la matriz en la cuál fuera un 0 dado que eso significa paredes.
* Desarrollar una función comparadora para ordenar las colas de prioridad y la heurística. Esto fue, particularmente complejo dado que tenía que tomarse en cuenta cómo es que estaba programada la cola de prioridad de manera que el primer valor sería el peek mientras que el último valor sería el bottom del stack.
* Comprender y diferenciar el algoritmo de Depth First Search del Depth Delimited Search. Esto se debió realizar dado que no se comprendía sí existía diferencia alguna, cosa que sí había ya que lo que los diferenciaba era el límite, y explotar o no explotar completamente una rama.
* Implementar un modelo gráfico para desarrollar el laberinto, qué herramientas se utilizarían, se utilizarían inputs para cambiar entre algoritmos, etc. De manera que se utilizó pygame dado que es un módulo para el desarrollo de video juegos y a partir de inputs [0-9] se haría el cambio entre algoritmos, finalmente se utilizó una función para tomar screenshots del cambio en el algoritmo gráficamente.
* Si se debería de hacer algún tipo de retorno de los algoritmos de búsqueda o no, la respuesta fue que sí dado que se necesitaba el path para graficar los algoritmos en cuestión.
## ¿En qué casos es mejor para cada algoritmo?
* Breadth First Search: 
* Depth First Search: 
* Depth Delimited Search: 
* Greedy Best First Search: 
* A Star Search: 
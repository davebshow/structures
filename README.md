Structures
==========
This is my repo for all the neat code I have written in my computer science classes and other data structures/algorithms that I want to save. Currently it only contains a graph data structure and supporting data types:

CS 2121/9634b
-------------
David Brown
-----------
Final Project
-------------

AGraph 
======
AGraph is an undirected adjacency list style graph data structure. All classes and data structures were written/modified according to the needs of the AGraph class. 

Nodes
=====
The most basic unit of AGraph is the node. The node has 3 attributes: .data - the information contained in the node--set at instantiation. .id- an id number corresponding to the index of the array in which it is stored--set upon addition to the graph structure. .edges - a doubly linked list--instantiated upon the creation of the node object. Furthermore, nodes have an attribute neighbors, which will be shown later while discussing the graph.
```python
>>> n = Node("palta")

>>> n.data
>>> 'palta'

>>> n.id

>>> n.edges
>>> <__main__.LinkedList at 0x8b92e4c>
```
The nodes are stored in a specialized node array. While generally a standard implementation of a 1D array using ctypes.py_objects, it has an interesting method used for adding nodes that has three primary uses: 1) It automatically assigns node id to correspond with the array index. 2) It provides an option to control id and index assignment, used during traversals to determine if all nodes have been visited. 3) If the array is full, it automatically creates a new array twice the size of the original, and copies the contents of the original array into the new array:
```python
def add_node(self, data, ndx=None, edge=None):
    node = Node(data)
    if ndx:
        node.id = ndx
        self._items[ndx] = node
        self._count += 1
    elif self._count < self._size:
        node.id = self._count
        self._items[self._count] = node
        self._count += 1
    else:
        print "Array Resized"
        resize = self._size * 2
        n_arr = NodeArray(resize)
        n_arr.copy(self._items)
        self._items = n_arr
        self._items[self._count] = node
        self._size = resize
        self._count += 1
```
The use case is as follows:
```python
>>> a = NodeArray(size=1)

>>> a.add_node('palta')

>>> a[0].data
>>> 'palta'

>>> a[0].id
>>> 0

>>> a.add_node('parcha')
Array Resized

>>> a.size
>>> 2

>>> a[1].data
>>> 'parcha'

>>> a[1].id
>>> 1
```
Linked List Nodes
=================
The graph's nodes are of course connected by edges. An edge is created by first adding a linked list node to a graph node's edge list. The linked list node has three attributes: .data - which is the id number of the destination node of the edge--assigned upon instantiation. .prev and .next - linked list references-- determined when nodes are added to the list. Finally the optional .edge_reference - which points to an edge object--determined upon the instantiation of the linked:
```python
>>> l = LinkedListNode("2",edge_reference="SomeEdge")

>>> l.data
>>> '2'

>>> l.prev

>>> l.next

>>> l.edge_reference
>>> 'SomeEdge'
```

Edges
=====
Finally we have the actual edge object. The edge object has three attributes: .data - any data stored in the edge--assigned upon instantiation of the object. .source and .target - which are references to linked list nodes in the edge list of the corresponding adjacent nodes--assigned upon addition to the graph:
```python
>>> e = Edge("LatAmerFruits")

>>> e.data
>>> 'LatAmerFruits'

>>> e.source

>>> e.target
```

AGraph
======
The combination of these structures results in a graph data type that features the following time complexities:

incident edges(neighbors) = O(deg(v))
adjacent nodes = O(deg(v)) -v is first node passed as params.
add node = O(1)
add edge = O(1)
remove node = O(deg(v)) -v is first node passed as params
remove edge = O(1) # however find edge is O(deg(v))

AGraph provides the following attributes and methods:
`size` the size of the graph.             
`node_dict` a dictionary of node id's and node data.     
`create_node` and `create_edge` for building a graph.
`adjacent_node` determine if two nodes are adjacent.
`search_edge` find and return an edge object.
`destroy_node` and `destroy_edge` to remove node and edge objects
`is_connected` determine if graph is connected
`traversal` and `recursive_traversal` visit all nodes and edges
`breadth_search` and `recursive_breadth_search` breadth first search
`neighbors_traversal` and `recursive_neighbors_traversal` finds all neighbors of a node to a certain degree of separation.
`generate_random` generates a random graph with a certain number of nodes and a certain probability that the are connected. Quadratic.

The AGraph API is used as follows:
----------------------------------
Create and Destroy Nodes
========================
```python
>>> from structures import AGraph

>>> G = AGraph()

>>> G.create_node("palta")

>>> G.nodes[0].data
>>> 'palta'

>>> G.nodes[0].id
>>> 0

>>> G.create_node("parcha")

>>> G.nodes[1].data
>>> 'parcha'

>>> G.nodes[1].id
>>> 1

>>> G.size
>>> 2

>>> G.node_dict
>>> {0: 'palta', 1: 'parcha'}

>>> G.create_edge("LatAmerFruit",0,1)

>>> G.adjacent(0,1)
>>> True

>>> G.nodes[0].neighbors
>>> set([1])

>>> G.nodes[1].neighbors
>>> set([0])

>>> G.destroy_node(0)

>>> G.nodes[1].neighbors
>>> set([])
```
Generate a Random Graph for Testing
===================================
```python

>>> G = AGraph.generate_random(10,0.4)

>>> G.nodes[0].neighbors
>>> set([8, 1, 5, 9])

>>> G.destroy_node(0)

>>> G.nodes[8].neighbors
>>> set([9, 3, 6])

>>> G.nodes[1].neighbors
>>> set([2, 3, 4, 6])
```

Find an Edge and Destroy it
===========================
```python

>>> e = G.search_edge(1,4)

>>> e
>>> <graphs.graph_data_structures.Edge at 0x992e4ec>

>>> G.destroy_edge(e)

>>> G.nodes[1].neighbors
>>> set([2, 3, 6])

>>> G.nodes[4].neighbors
>>> set([2, 6])
```

Traverse the Graph
==================
```python

>>> G = AGraph.generate_random(10,0.3)

>>> G.traversal(0)
# node.id : node.data
0 : 0
2 : 2
4 : 4
6 : 6
7 : 7
8 : 8
1 : 1
9 : 9
5 : 5
>>> False # Not connected

>>> G.nodes[3].neighbors
>>> set([])

>>> G = AGraph.generate_random(10,0.4)

>>> G.traversal(0)
0 : 0
6 : 6
7 : 7
8 : 8
1 : 1
4 : 4
9 : 9
3 : 3
2 : 2
5 : 5
>>> True #full traversal

>>> G.recursive_traversal(0)
0 : 0
6 : 6
1 : 1
4 : 4
2 : 2
5 : 5
7 : 7
8 : 8
9 : 9
3 : 3
>>> True #full traversal
```

Perform a Breadth First Search
==============================
```python

>>> G.breadth_search(0,9)
9 4 1 8 7 6 0 

>>> True

>>> G.recursive_breadth_search(0,9)
0 6 1 4 2 5 7 8 9 

>>> True
```

Perform a Neighbors Traversal
=============================
```python

>>> G.recursive_neighbors_traversal(4,2)
>>> set([0, 1, 2, 3, 4, 5, 6, 8, 9])

>>> G.nodes[7].neighbors
>>> set([0, 5, 6])

>>> G.nodes[0].neighbors
>>> set([8, 6, 7])

>>> G.nodes[5].neighbors
>>> set([2, 6, 7])

>>> G.nodes[6].neighbors
>>> set([0, 1, 2, 3, 5, 7, 8])

```
Recursive vs. Non-Recursive Traversal Speed
>>> % timeit a.traversal(0)
1000 loops, best of 3: 270 us per loop

>>> % timeit a.recursive_traversal(0)
1000 loops, best of 3: 731 us per loop

>>> % timeit a.breadth_search(0,19)
10000 loops, best of 3: 94.4 us per loop

>>> % timeit a.recursive_breadth_search(0,19)
1000 loops, best of 3: 351 us per loop

>>> %timeit a.neighbors_traversal(0,2)
10000 loops, best of 3: 103 us per loop

>>> %timeit a.recursive_neighbors_traversal(0,2)
10000 loops, best of 3: 117 us per loop






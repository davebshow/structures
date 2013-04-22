Structures
==========

AGraph 
-----------------------

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

>>> G = AGraph.generate_randoG(10,0.58)

>>> G.nodes[6].neighbors
>>> set([0, 1, 3, 4, 5, 8, 9])

>>> G = AGraph.generate_randoG(10,0.58)

>>> G = AGraph.generate_randoG(10,0.58)

>>> G.nodes[6].neighbors
>>> set([0, 8, 5, 7])

>>> G = AGraph.generate_randoG(10,0.3)

>>> G.nodes[0].neighbors
>>> set([])

>>> G = AGraph.generate_randoG(10,0.5)

>>> G.nodes[0].neighbors
>>> set([1, 2, 4, 5, 6, 8, 9])

>>> G = AGraph.generate_randoG(10,0.4)

>>> G.nodes[0].neighbors
>>> set([8, 1, 5, 9])

>>> G.nodes[8].neighbors
>>> set([0, 9, 3, 6])

>>> G.nodes[1].neighbors
>>> set([0, 2, 3, 4, 6])

>>> G.destroy_node(0)

>>> G.nodes[8].neighbors
>>> set([9, 3, 6])

>>> G.nodes[1].neighbors
>>> set([2, 3, 4, 6])

>>> e = G.search_edge(1,4)

>>> e
>>> <graphs.graph_data_structures.Edge at 0x992e4ec>

>>> G.destroy_edge(e)

>>> G.nodes[1].neighbors
>>> set([2, 3, 6])

>>> G.nodes[4].neighbors
>>> set([2, 6])

>>> G = AGraph.generate_randoG(10,0.3)

>>> G.traversal(0)
0 : 0
2 : 2
4 : 4
6 : 6
7 : 7
8 : 8
1 : 1
9 : 9
5 : 5
>>> False

>>> G.nodes[3].neighbors
>>> set([])

>>> G = AGraph.generate_randoG(10,0.4)

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
>>> True

>>> G.rec_traversal(0)
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
>>> True

>>> G.breadth_search(0,9)
9 4 1 8 7 6 0 

>>> True

>>> G.rec_breadth_search(0,9)
0 6 1 4 2 5 7 8 9 

>>> True

>>> G.rec_neighbors_traversal(4,2)
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






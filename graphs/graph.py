
import random 
import itertools
from graph_data_structures import *

class GraphJunior(object):
    """Graph with stable number of nodes and super fast edge creation
    Nodes kept in an array with pointers to linked edge lists."""

    @staticmethod
    def generate_random(size, prob):
        """ Exponential. 5,000 at 0.1 crashed by compu. size < 2500. prob < 1"""
        G = Graph()
        for x in range(size):
            G.add_node(x)
        edges = itertools.combinations(range(size),2)
        for edge in edges:
            if random.random() < prob:
                G.add_edge("edge",edge[0],edge[1])
        return G

    def __init__(self,size=None):
        if size:
            self.nodes = NodeArray(size)
            self.array = size
        else:
            self.nodes = NodeArray(1000)
            self.array = 1000
        self.size = 0
        
    def __len__(self):
        return self.size

    def _get_node_dict(self):
        nodes = {}
        for ndx in range(self.nodes._count):
            node = self.nodes[ndx]
            nodes[node.id] = node.data
        return nodes

    node_dict = property(_get_node_dict)

    def add_node(self, data):
        self.size += 1
        self.nodes.add_node(data)

    def remove_node(self, ndx):
        self.nodes[ndx] = None
        self.size -= 1

    def remove_edge(self,source,target):
        self.nodes[source].edges.remove(target)
        self.nodes[target].edges.remove(source)
        
    def add_edge(self, data, source, target):
        """ can this be faster? """
        node1 = self.nodes[source]
        node2 = self.nodes[target]
        node1.edges.add_edge(data, node1.id, node2.id)
        node2.edges.add_edge(data, node2.id, node1.id)

    def adjacent(self, node1, node2):
        for edge in self.nodes[node1].edges:
            if edge.target == node2:
                return True
        return False

    def is_connected(self):
        return self.traversal()

    def traversal(self, start):
        node = self.nodes[start]
        visited = NodeArray(size=self.size)
        visited.add_node(True, ndx=node.id)
        stack = Stack()
        stack.push(node.id)
        print "%i : %s" % (node.id,node.data)
        while not visited.full():
            if node._valid_neighbors(visited):
                for neighbor in node.edges:
                    if not visited[neighbor.target]:
                        node = self.nodes[neighbor.target]
                        stack.push(neighbor.target)
                        visited.add_node(True, ndx=neighbor.target)  
                        print "%i : %s" % (node.id,node.data)       
            else:
                stack.pop()
                if len(stack) == 0:
                    return False
                else:
                    node = self.nodes[stack.peek()]
        return True

    def rec_traversal(self, start, visited=None):
        """this breaks down on big graphs"""
        node = self.nodes[start]
        if visited == None:
            visited = NodeArray(size=self.size)
            print "%i : %s" % (node.id, node.data)
        visited.add_node(True, ndx=node.id)
        if visited.full():
            return True
        elif node._valid_neighbors(visited):
            for neighbor in node.edges:
                if not visited[neighbor.target]:
                    print "%i : %s" % (self.nodes[neighbor.target].id,self.nodes[neighbor.target].data)
                    n_traversal = self.rec_traversal(neighbor.target,visited=visited)
                    if n_traversal:
                        return True
        return False

    def breadth_search(self, start, finish):
        node = self.nodes[start]
        stack = Stack()
        stack.push(node.id)
        visited = NodeArray(size=self.size)
        visited[node.id] = node
        while True:
            if node.id == finish:
                print stack
                return True
            elif node._valid_neighbors(visited):
                for neighbor in node.edges:
                    if not visited[neighbor.target]:
                        node = self.nodes[neighbor.target]
                        stack.push(neighbor.target)
                        visited[neighbor.target] = node
            else:
                stack.pop()
                if len(stack) == 0:
                    return False
                else:
                    node = self.nodes[stack.peek().data]

    def rec_breadth_search(self, start, finish, path=None):
        """don't really like this"""
        if not path:
            path = LinkedList()
        node = self.nodes[start]
        path.add_node(start)
        if start == finish:
            for node in path:
                print node.data,
            return True
        for neighbor in node.edges:
            if neighbor.target not in path:
                n_path = self.rec_breadth_search(neighbor.target,finish,path)
                if n_path:
                    return True
        return False

    def neighbors_traversal(self,node,degree_sep):
        pass
   
    def rec_neighbors_traversal(self, start, degree_sep, visited=None):
        """doesn't really work for big dense graphs or degree_sep > 6"""
        node = self.nodes[start]
        if visited ==  None:
            visited = NodeArray(size=self.size)
        visited.add_node(True, ndx=node.id)
        traversal_neighbors = set(node.neighbors)
        if degree_sep > 1:
            for neighbor in node.edges:
                if not visited[neighbor.target]:
                    n_neighbors = self.rec_neighbors_traversal(neighbor.target, degree_sep-1, 
                                                            visited=visited)
                    traversal_neighbors.update(n_neighbors)
        return traversal_neighbors
             



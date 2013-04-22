
import random 
import itertools
from graph_types.data_structures import *

class AGraph(object):
    """An adjacency list style graph with constant time node and edge creation, 
    constant time edge destruction, edge search, node deletion and neighbors 
    retrieval O(deg(v)). Includes traversals, breadth search, and neighbors
    traversals."""

    @staticmethod
    def generate_random(size, prob):
        """ Exponential. 5,000 at 0.1 crashed by compu. size < 2500. prob < 1"""
        G = AGraph(size)
        for x in range(size):
            G.create_node(x)
        edges = itertools.combinations(range(size),2)
        for edge in edges:
            if random.random() < prob:
                G.create_edge("edge",edge[0],edge[1])
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

    def create_node(self, data):
        self.size += 1
        self.nodes.add_node(data)

    def destroy_node(self, ndx):
        for node in self.nodes[ndx].edges:
            self.destroy_edge(node.edge_ref)   
        self.nodes[ndx] = None
        self.size -= 1

    def destroy_edge(self,edge):
        if edge.target is self.nodes[edge.source.data].edges.head:
            self.nodes[edge.source.data].edges.head = self.nodes[edge.source.data].edges.head.next
            edge.target.next = None
        elif edge.target is self.nodes[edge.source.data].edges.tail:
            self.nodes[edge.source.data].edges.head = self.nodes[edge.source.data].edges.head.next
            edge.target.prev = None
        else:
            edge.target.prev.next = edge.target.next
            edge.target.next.prev = edge.target.prev
            edge.target.prev = None
            edge.target.next = None
        if edge.source is self.nodes[edge.target.data].edges.head:
            self.nodes[edge.target.data].edges.head = self.nodes[edge.target.data].edges.head.next
            edge.source.next = None
        elif edge.target is self.nodes[edge.target.data].edges.tail:
            self.nodes[edge.target.data].edges.head = self.nodes[edge.target.data].edges.head.next
            edge.source.prev = None
        else:
            edge.source.prev.next = edge.source.next
            edge.source.next.prev = edge.source.prev
            edge.source.prev = None
            edge.source.next = None
        edge.target = None
        edge.source = None

    def search_edge(self,source,target):
        for node in self.nodes[source].edges:
            if node.data == target:
                return node.edge_ref
  
    def create_edge(self, data, source, target):
        """ can this be faster? """
        node1 = self.nodes[source]
        node2 = self.nodes[target]
        edge = Edge(data)
        node1.edges.add_node(target,edge_ref=edge)
        node2.edges.add_node(source,edge_ref=edge)
        edge.source = node1.edges.tail
        edge.target = node2.edges.tail
        
    def adjacent(self, node1, node2): # check
        for edge in self.nodes[node1].edges:
            if edge.data == node2:
                return True
        return False

    def is_connected(self):
        return self.traversal(0)

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
                    if not visited[neighbor.data]:
                        node = self.nodes[neighbor.data]
                        stack.push(neighbor.data)
                        visited.add_node(True, ndx=neighbor.data)  
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
                if not visited[neighbor.data]:
                    print "%i : %s" % (self.nodes[neighbor.data].id,self.nodes[neighbor.data].data)
                    n_traversal = self.rec_traversal(neighbor.data,visited=visited)
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
                for x in range(len(stack)):
                    pop = stack.pop()
                    print pop.data,
                print "\n"
                return True
            elif node._valid_neighbors(visited):
                for neighbor in node.edges:
                    if not visited[neighbor.data]:
                        node = self.nodes[neighbor.data]
                        stack.push(neighbor.data)
                        visited[neighbor.data] = node
            else:
                stack.pop()
                if len(stack) == 0:
                    return False
                else:
                    node = self.nodes[stack.peek()]

    def rec_breadth_search(self, start, finish, path=None):
        """don't really like this"""
        if not path:
            path = LinkedList()
        node = self.nodes[start]
        path.add_node(start)
        if start == finish:
            for node in path:
                print node.data,
            print "\n"
            return True
        for neighbor in node.edges:
            if neighbor.data not in path:
                n_path = self.rec_breadth_search(neighbor.data,finish,path)
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
                if not visited[neighbor.data]:
                    n_neighbors = self.rec_neighbors_traversal(neighbor.data, degree_sep-1, 
                                                            visited=visited)
                    traversal_neighbors.update(n_neighbors)
        return traversal_neighbors
             



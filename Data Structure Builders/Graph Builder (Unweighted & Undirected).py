#Name: Terry Su
#Date: June 9, 2021
#Purpose: Building an unweighted and undirected graph from scratch

class Graph:

    def __init__(self, number_of_nodes = 0, adjacent_list= {}):
        
        self.number_of_nodes = number_of_nodes
        self.adjacent_list = adjacent_list #one of three ways to model a graph besides an edge list or adjacency matrix

    def add_vertex(self,node):
        
        if node in self.adjacent_list:
            return #'node already in graph'

        self.adjacent_list[node] = []
        self.number_of_nodes += 1
        return

    def add_edge(self,node1,node2): #assuming both nodes already exist

        if (node2 in self.adjacent_list[node1]) or (node1 == node2):
            return #'connection exists already'

        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)
        return

    def show_connections(self):
        for node in self.adjacent_list:
            print(node, self.adjacent_list[node])
        return
            
my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_edge(1,3)
my_graph.add_edge(1,5)
my_graph.add_edge(4,3)
my_graph.add_edge(1,5)
my_graph.add_edge(2,2)
my_graph.show_connections()

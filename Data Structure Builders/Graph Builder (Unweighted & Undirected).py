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
            
    def bfs_traversal(self,start_node):

        visited = []
        queue = [start_node] 

        while len(queue) != 0: 
            
            for connection in self.adjacent_list[queue[0]]: #adding connections/edges of current node into queue
                
                if connection not in visited:
                    queue.append(connection)

            visited.append(queue[0]) #adding current node into visited and moving onto next node in queue
            queue.pop(0)

        return print(visited)

    def bfs_traversal2(self,start_node): #also gives layer of BFS

        visited = []
        queue = [(start_node,1)] #node, depth of BFS

        while len(queue) != 0: 
            
            for connection in self.adjacent_list[queue[0][0]]:
                
                if connection not in [x[0] for x in visited]:
                    queue.append((connection,queue[0][1]+1))

            visited.append(queue[0])
            queue.pop(0)

        return print(visited)

    def dfs_traversal(self,start_node):

        visited = []

        def traverse(curr): #start with the initial node

            visited.append(curr)
            
            for connection in self.adjacent_list[curr]: #go down one path as deep as possible from initial, then explore connections starting from deepest children
                if connection not in visited:
                    traverse(connection)
            
            return visited

        return print(traverse(start_node))

        


        
        
        
            
my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_edge(1,3)
my_graph.add_edge(3,5)
my_graph.add_edge(3,4)
my_graph.add_edge(1,2)
my_graph.add_edge(1,4)

my_graph.show_connections()
my_graph.dfs_traversal(1)

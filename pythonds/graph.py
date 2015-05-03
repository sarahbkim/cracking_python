'''
The Graph ADT
--------------
* Graph() creates a new, empty graph
* addVertex(vert) adds an instance of Vertex to the graph
* addEdge(fromVert, toVert) adds a new directed edge to graph that connects 2 vertices
* addEdge(fromVert, toVert, weight) adds a new weighted, directed edge to graph that connects 2 vertices
* getVertext(vertKey) finds the vertex in graph named vertKey
* getVertices() returns list of all vertices in graph 
* in returns True if `vertex in graph` if a given vertex is in the graph, False otherwise
'''

# Implementation
class Vertex:
    '''
    Vertex  * holds all the information of a single vertext 
            * uses a dictionary to keep track of vertices to which it is connected
    '''
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white' #default color
        self.distance = 0
        self.pred = None

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connected_to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def set_color(self, color):
        self.color = color
        return color

    def get_color(self):
        return self.color

    def set_distance(self, dist):
        self.distance = dist 

    def set_pred(self, pred):
        if self.pred == None:
            self.pred = pred
        return pred

class Graph:
    '''
    Graph contains: * a dictionary that maps vertex names to vertex objects
                    * a method for adding vertices to a graph and connecting one vertext to another 
    '''
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def get_vertices(self):
        return self.vert_list.keys()

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def __iter__(self):
        return iter(self.vert_list.values())


# g = Graph()
# for i in range(6):
#     g.add_vertex(i)
# g.vert_list
# g.add_edge(0,1,5)
# g.add_edge(0,5,2)
# g.add_edge(1,2,4)
# g.add_edge(2,3,9)
# g.add_edge(3,4,7)
# g.add_edge(3,5,3)
# g.add_edge(4,0,1)
# g.add_edge(5,4,8)
# g.add_edge(5,2,1)
# for v in g:
#     for w in g.get_connections():
#         print("(%s, %s)" % (v.get_id(), w.get_id()))



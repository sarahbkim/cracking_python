from pythonds.graph import Graph, Vertex
# from pythonds import Queue

def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.get_connections():
            if (nbr.get_color() == 'white'):
                nbr.set_color('gray')
                nbr.set_distance(currentVert.getDistance() + 1)
                nbr.set_pred(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.set_color('black')

def build_graph():
    

'''
run time is O(V) where V is the vertex 
'''
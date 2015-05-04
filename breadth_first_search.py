# from pythonds.graph import Graph, Vertex
# from pythonds import Queue
from collections import deque


# '''
# run time is O(V) where V is the vertex 
# '''
# def bfs(g, start):
#     start.set_distance(0)
#     start.set_pred(None)
#     vertQueue = Queue()
#     vertQueue.enqueue(start)

#     while vertQueue.size() > 0:
#         currentVert = vertQueue.dequeue()
#         for nbr in currentVert.get_connections():
#             if (nbr.get_color() == 'white'):
#                 nbr.set_color('gray')
#                 nbr.set_distance(currentVert.getDistance() + 1)
#                 nbr.set_pred(currentVert)
#                 vertQueue.enqueue(nbr)
#             currentVert.set_color('black')

# def build_graph(word_file):
#     d = {}
#     g = Graph()
#     wfile = open(word_file, 'r')

#     # create buckets of words that differ by 1 letter
#     for line in wfile:
#         word = line[:-1]
#         for i in range(len(word)):
#             bucket = word[:i] + '_' + word[i+1:]
#             if bucket in d:
#                 d[bucket].append(word)
#             else:
#                 d[bucket] = [word]
    
#     #  vertices and edges for words in same bucket
#     for bucket in d.keys():
#         for word1 in d[bucket]:
#             for word2 in d[bucket]:
#                 if word1 != word2:
#                     g.add_edge(word1, word2)


# build_graph('dictionary.txt')

# another example
graph = {'A': ['B','E','C'],
         'B': ['A','C'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F','D'],
         'F': ['C']}


def my_bfs(graph, start, end):
    q = deque()
    q.append(start)
    path = []

    # while queu is not empty... 
    while q:
        curr = q.popleft()
        path.append(curr)
        # check each vertex connected to the current
        for item in graph[curr]:
            if item not in path:
                path.append(item)
                last_node = path[len(path)-1]
                # return the path if I find the right end
                if last_node == end:
                    return path
                # otherwise, append this item to the queue and start again
                path = []
                path.append(start)
                q.append(item)


# print my_bfs(graph, 'A', 'E')
# print my_bfs(graph, 'B', 'D')
# print my_bfs(graph, 'A', 'F')

graphB = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



def my_dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            stack.extend(set(graph[curr])-visited)
    return visited

# print my_dfs(graphB, 'A')

# all possible paths for A:
# [A, B, D]
# [A, C]
# [A, B, E, F]


def my_dfs_forest(graph, start):
    q = deque()
    q.append(start)
    forest = [] # collection of paths
    main_visited = set()

    while q:
        curr = q.pop()
        if curr not in main_visited:
            main_visited.add(curr)
            q.extend(set(graph[curr]-main_visited))

            visited = set()
            path = []
            sub_q = deque()
            sub_q.append(curr)

            while sub_q:
                sub_curr = sub_q.popleft()
                path.append(sub_curr)
                
                for item in graph[sub_curr]:
                    if item not in visited:
                        path.append(item)
                        visited.add(item)
                        sub_q.append(item)
                    if path not in forest:
                        forest.append(path)
                path = [] # reset path
            visited = set() # reset visited
            
    return forest

print my_dfs_forest(graphB, 'A')
# from pythonds.graph import Graph, Vertex
# from pythonds import Queue
from collections import deque


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

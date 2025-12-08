import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

G.add_nodes_from(["Router","TV","Phone Kateryna","Tablet","Laptop","Work Laptop"])
G.add_edges_from([
    ("Router", "TV"),
    ("Router", "Phone Kateryna"),
    ("Router", "Tablet"),
    ("Router", "Laptop"),
    ("Router", "Work Laptop"),
    ("Phone Kateryna","Laptop"),
    ("Phone Kateryna","Tablet")
])

start_node = "Work Laptop"
end_node = "Tablet"


def bfs_find_path(graph,start,end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()  
        node = path[-1] 

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None            
    
def dfs_find_path(graph, start, end,path=None):
    if path is None:
        path = []
    path.append(start)
    if start == end:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            result = dfs_find_path(graph, neighbor, end, path)
            if result:
                return result
    path.pop()  
                
    return None 
    
path_bfs = bfs_find_path(G,start_node,end_node)


path_dfs = dfs_find_path(G,start_node,end_node)

print(f"Шлях BFS (ширина): {path_bfs}")
print(f"Шлях DFS (глибина): {path_dfs}")


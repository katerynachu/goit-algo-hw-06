import networkx as nx
import matplotlib.pyplot as plt

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

path_bfs = nx.shortest_path(G,start_node,end_node)

path_dfs = list(nx.all_simple_paths(G,start_node,end_node))[0]

print(f"Шлях BFS (ширина): {path_bfs}")
print(f"Шлях DFS (глибина): {path_dfs}")


import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Router","TV","Phone Kateryna","Tablet","Laptop","Work Laptop"])
G.add_weighted_edges_from([
    ("Router", "TV",1),
    ("Router", "Phone Kateryna",3),
    ("Router", "Tablet",3),
    ("Router", "Laptop",3),
    ("Router", "Work Laptop",3),
    ("Phone Kateryna","Laptop",5),
    ("Phone Kateryna","Tablet",5)
])

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph.nodes}
    predecessors = {node: None for node in graph.nodes}
    distances[start_node] = 0
    unvisited_nodes = list(graph.nodes)
    while unvisited_nodes:
        current_node = min(unvisited_nodes,key=lambda node :distances[node])
        if distances[current_node] == float('inf'):
            break

        for neighbor,weight_data in graph[current_node].items():
            weight = weight_data['weight']
            new_distance = distances[current_node] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
        unvisited_nodes.remove(current_node)      
    return distances, predecessors

all_shortest_distances = {}
for start_node in G.nodes:
    distances, _ = dijkstra(G, start_node) 
    all_shortest_distances[start_node] = distances

print(all_shortest_distances)
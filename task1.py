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

nx.draw(G,with_labels=True)
plt.show()

print(f"Кількість вершин (пристроїв): {G.number_of_nodes()}")
print(f"Кількість ребер (зв'язків): {G.number_of_edges()}")

degrees = G.degree() 
print("Ступінь кожної вершини (Degree):", degrees)


import networkx as nx

G = nx.DiGraph()
G.add_node("Alice")
G.add_node("Bella")
G.add_node("Carla")
G.add_node("Danni")
G.add_node("Esmer")
G.add_node("Freda")
G.add_node("Grace")

N = list(G.nodes())
print(N)

for i in range(len(N)):
    # print(i)
    # print(N[i])
    if i < (len(N)-1):
        G.add_edge(N[i], N[i+1])
    G.add_edge(N[-1], N[0])

E = list(G.edges())
print(E)

# nx.draw(G)
# nx.draw_circular(G)

import networkx as nx
import matplotlib.pyplot as plt
"""
f = open("res.txt", "r")

f2 = open("Code/bert-relation-extraction/res2.txt", "w")

with open("Code/bert-relation-extraction/res.txt", 'r') as infile:
    for line_idx, line in enumerate(infile):
        c = line[:-7] + "\n"
        f2.write(c)
"""

f2 = open("Code/bert-relation-extraction/res2.txt", "r")

G = nx.DiGraph()

edge_labels_C = {}

edge_labels_W = {}
count = 0
with open("Code/bert-relation-extraction/res.txt", 'r') as infile:
    for line_idx, line in enumerate(infile):
        c = line.split("@")
        if "<e1>" in c[0] or "<e2>" in c[0] or "<e1>" in c[1] or "<e2>" in c[1]:
            continue
        G.add_edge(c[0], c[1], name=c[2])
        cor = c[3][:-1]
        if c[2] == c[3][:-1]:
            edge_labels_C[(c[0], c[1])] = c[2]
        else:
            edge_labels_W[(c[0], c[1])] = c[2]
        count += 1
        if count > 20:
            break

pos = nx.spring_layout(G)
plt.figure()
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels_C,
    font_color='black'
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels_W,
    font_color='red'
)
plt.axis('off')
plt.show()

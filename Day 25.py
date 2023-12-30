import networkx as nx
import matplotlib.pyplot as plt
import re

text_sequence = open('day25-input.txt', 'r').read().split('\n')


# Create a graph
G = nx.Graph()
for line in text_sequence:
    # Split the string by space and colon using regular expression and filter non-empty values
    result = [substring for substring in re.split(r'\s|:', line) if substring]
    for i in range(len(result)-1):
        G.add_edges_from([(result[0],result[i+1])])

# Display the original graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.title("Original Graph")
plt.show()

# Identify and remove an edge to cut the graph
cut_edges = [('nhg', 'jjn'),('tmc','lms'),('xnn','txf')]
G.remove_edges_from(cut_edges)

# Display the modified graph after cutting the edge
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.title("Graph after Cutting Edge")
plt.show()

# Calculate connected components
components = list(nx.connected_components(G))

component_size = []
# Print the number of nodes in each connected component
for i, component in enumerate(components):
    print(f"Number of nodes in Component {i + 1}: {len(component)}")
    component_size.append(len(component))
print(component_size[0]*component_size[1])


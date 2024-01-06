import networkx as nx
import matplotlib.pyplot as plt

def construct_map_graph(map_data):
    G = nx.Graph()

    rows = len(map_data)
    cols = len(map_data[0])

    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] == '.' or map_data[i][j] == '#':
                node = (i, j)
                G.add_node(node, symbol=map_data[i][j])  # Add the symbol as a node attribute

                # Add neighbors (right, left, up, down)
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and (map_data[ni][nj] == '.' or map_data[ni][nj] == '#'):
                        neighbor = (ni, nj)
                        G.add_edge(node, neighbor)

    return G

# Specify the file path
file_path = "/Users/sabadaftari/AdventOfCode/day11-input.txt"

# Initialize an empty list to store modified rows
map_data = []

# Read the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        # Check if the line contains '#'
        if '#' not in line:
            # Copy the line into a new line above it
            map_data.append(line.rstrip('\n'))
        map_data.append(line.rstrip('\n'))

def find_column_without_hash(rows):
    num_columns = len(rows[0])  # Assuming all rows have the same number of columns
    index_list = []
    for column_index in range(num_columns):
        if all('#' not in row[column_index] for row in rows):
            index_list.append(column_index)

    return index_list

def copy_and_add_column(rows, source_column_index):
    new_rows = []

    for row in rows:
        # Copy the 35th column and add it to the right side
        new_row = row[:source_column_index+1] + "." + row[source_column_index+1:]
        new_rows.append(new_row)

    return new_rows

# map_data = [
#     "...............#..........................",
#     "...#...........................#...........",
#     "...........................................",
#     "...#......#................#................",
#     "............................................",
#     "...................#........................",
#     "............#................#............."
# ]
# Find the index of the column without '#'
index_of_column_without_hash = find_column_without_hash(map_data)

if index_of_column_without_hash is not None:
    print(f"Index of the column without '#': {index_of_column_without_hash}")
else:
    print("No such column without '#' found.")


for idx in sorted(index_of_column_without_hash, reverse=True):
    # Copy the 35th column and add it to a new column on the right
    map_data = copy_and_add_column(map_data, idx)



# Construct the NetworkX graph
map_graph = construct_map_graph(map_data)

# Get the nodes corresponding to '#' characters
hash_nodes = [node for node, attr in map_graph.nodes(data=True) if attr['symbol'] == '#']

# Initialize a list to store the lengths of shortest paths
path_lengths = []

# Find and save the lengths of shortest paths between each pair of '#' characters
for i in range(len(hash_nodes) - 1):
    for j in range(i + 1, len(hash_nodes)):
        start_node = hash_nodes[i]
        end_node = hash_nodes[j]
        shortest_path = nx.shortest_path_length(map_graph, source=start_node, target=end_node)
        path_lengths.append(shortest_path)

# Calculate the sum of the lengths
sum_of_lengths = sum(path_lengths)

print(f"Lengths of Shortest Paths: {path_lengths}")
print(f"Sum of Lengths: {sum_of_lengths}")

# Visualize the graph (optional)
pos = {node: (node[1], -node[0]) for node in map_graph.nodes()}
nx.draw(map_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=8, font_color='black', edge_color='gray')

# Show the plot
plt.show()

import re
import networkx as nx
import matplotlib.pyplot as plt

def convert_to_list(input_string):

    # Using re.split() to separate characters by space or equals sign
    result = re.split(r'[= ,()]', input_string)

    # Removing empty strings from the result
    result = [item for item in result if item]
    return result

def search(texts, target):
    for row in texts:
        if target == row[0]:
            return row[1], row[2]

if __name__ == "__main__":

    text_sequence = list(open('day8-input.txt', 'r').read().split('\n'))
    text_sequence1 = text_sequence[0]+text_sequence[0]+text_sequence[0]+text_sequence[0]
    text_sequence3 = text_sequence1+text_sequence1+text_sequence1+text_sequence1+text_sequence1
    text_sequence2 = text_sequence3+text_sequence3+text_sequence3+text_sequence3+text_sequence3

    converted_texts = [convert_to_list(text) for text in text_sequence[2:]]

    starting_point = 'AAA'
    count =0
    # count1 = 0
    while starting_point !='ZZZ':
        left, right = search(converted_texts, starting_point)
        print(starting_point,left,right)
        # try:
        print(text_sequence2[count])
        if text_sequence2[count]== "R":
            starting_point=right
        else:
            starting_point=left   
        # except IndexError:
        #     count=0
        count+=1

    print("number of steps: ",count)



    # Create a directed graph
    G = nx.DiGraph()

    for edge in converted_texts:
        G.add_edge(edge[0], edge[1])
        G.add_edge(edge[0], edge[2])

    # Visualize the graph (optional)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", arrowsize=10)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

    # Find the shortest path
    start_node = 'AAA'
    end_node = 'ZZZ'
    shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
    shortest_path_length = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')

    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
    print(f"Shortest path length: {shortest_path_length}")


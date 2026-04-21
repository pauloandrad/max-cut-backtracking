import sys

def populate_node_groups_recursive(nodes_list, nodes, col, max_col):
    if col == max_col:
        nodes_list.append(nodes.copy())
        return

    group = 0

    while group <= 1:
        nodes.append(group)
        populate_node_groups_recursive(nodes_list, nodes, col + 1, max_col)
        nodes.pop()
        group += 1

def initialize_node_groups(max_col):
    node_list = []
    nodes = []
    node_col = 0

    populate_node_groups_recursive(node_list, nodes, node_col, max_col)

    return node_list

def initialize_edges(edges):
    edge_list = []

    for edge in range(edges):
        if edge == edges - 1:
            edge_list.append((edge, 0))
            continue

        edge_list.append((edge, edge + 1))

    return edge_list

def calculate_scores(edges, node_list):
    all_score = []

    for i, nodes in enumerate(node_list):
        score = 0

        for edge in edges:
            if nodes[edge[0]] != nodes[edge[1]]:
                score = score + 1

        print(score)
        all_score.append(score)

    return all_score


if __name__ == '__main__':
    if len(sys.argv) > 1:
        max_graph = int(sys.argv[1])
    else:
        max_graph = 10

    groups_list = initialize_node_groups(max_graph)
    all_edges = initialize_edges(max_graph)
    all_scores = calculate_scores(all_edges, groups_list)

    max_points = [i for i, x in enumerate(all_scores) if x == max(all_scores)]

    print(all_edges)

    for max_point in max_points:
        print(groups_list[max_point])








def populate_node_groups_recursive(nodes_list, nodes, col):
    if col == 4:
        nodes_list.append(nodes.copy())
        return

    group = 0

    while group <= 1:
        nodes.append(group)
        populate_node_groups_recursive(nodes_list, nodes, col + 1)
        nodes.pop()
        group += 1

def initialize_node_groups():
    node_list = []
    nodes = []
    node_col = 0

    populate_node_groups_recursive(node_list, nodes, node_col)

    return node_list

def initialize_edges():
    return [(0,1), (1,2), (2,3), (3,0)]

def calculate_scores(edges, node_list):
    all_score = []

    for i, nodes in enumerate(node_list):
        score = 0

        for edge in edges:
            if nodes[edge[0]] != nodes[edge[1]]:
                score = score + 1

        all_score.append(score)

    return all_score


if __name__ == '__main__':
    groups_list = initialize_node_groups()
    all_edges = initialize_edges()
    all_scores = calculate_scores(all_edges, groups_list)

    max_points = [i for i, x in enumerate(all_scores) if x == max(all_scores)]

    print(all_edges)

    for max_point in max_points:
        print(groups_list[max_point])








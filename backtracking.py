import sys

def is_partial_solution(top_score, edges, nodes, col, max_col):
    score = calculate_scores(edges, nodes, col)
    possible_points = max_col - col

    if score + possible_points > top_score[0]:
        return True

    return False


def populate_node_groups_recursive(solution, top_score, nodes, col, max_col, edges):
    group = 0

    if col == max_col:
        score = calculate_scores(edges, nodes, col)

        if score > top_score[0]:
            top_score[0] = score
            solution[0] = nodes.copy()

        return

    while group <= 1:
        nodes.append(group)

        if is_partial_solution(top_score, edges, nodes, col, max_col):
            populate_node_groups_recursive(solution, top_score, nodes, col + 1, max_col, edges)

        nodes.pop()
        group += 1

def initialize_node_groups(max_col, edges):
    top_score = [0]
    solution = [[]]
    nodes = []
    node_col = 0

    populate_node_groups_recursive(solution, top_score, nodes, node_col, max_col, edges)

    print(top_score)

    return solution

def initialize_edges(edges):
    edge_list = []

    for edge in range(edges):
        if edge == edges - 1:
            edge_list.append((edge, 0))
            continue

        edge_list.append((edge, edge + 1))

    return edge_list

def calculate_scores(edges, nodes, col):
    score = 0

    for i, edge in enumerate(edges):
        if i >= col:
            return score

        if nodes[edge[0]] != nodes[edge[1]]:
            score = score + 1

    return score


if __name__ == '__main__':
    if len(sys.argv) > 1:
        max_graph = int(sys.argv[1])
    else:
        max_graph = 10

    all_edges = initialize_edges(max_graph)
    solution_nodes = initialize_node_groups(max_graph, all_edges)

    print(all_edges)
    print(solution_nodes)








import networkx as nx


def find_circular_dependencies(graph: nx.DiGraph):
    """
    Detect circular dependencies in the graph.
    """

    try:
        cycles = list(nx.simple_cycles(graph))
        return cycles
    except:
        return []


def find_dead_files(graph: nx.DiGraph):
    """
    Files with no dependencies and no dependents.
    """

    dead = []

    for node in graph.nodes():

        if graph.in_degree(node) == 0 and graph.out_degree(node) == 0:
            dead.append(node)

    return dead


def dependency_heatmap(graph: nx.DiGraph):
    """
    Rank files by dependency importance.
    Higher score = more connections.
    """

    heat = {}

    for node in graph.nodes():

        heat[node] = graph.degree(node)

    ranked = sorted(
        heat.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked


def dependency_depth(graph: nx.DiGraph):
    """
    Calculate dependency depth of each node.
    """

    depth_map = {}

    for node in graph.nodes():

        try:

            lengths = nx.single_source_shortest_path_length(graph, node)

            depth_map[node] = max(lengths.values()) if lengths else 0

        except:

            depth_map[node] = 0

    return depth_map


def analyze_graph(graph: nx.DiGraph):
    """
    Run full architecture analysis.
    """

    cycles = find_circular_dependencies(graph)
    dead = find_dead_files(graph)
    heat = dependency_heatmap(graph)
    depth = dependency_depth(graph)

    return {
        "cycles": cycles,
        "dead_files": dead,
        "heatmap": heat[:10],  # top 10 important modules
        "depth": depth
    }
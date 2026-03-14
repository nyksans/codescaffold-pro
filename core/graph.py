import networkx as nx


def build_dependency_graph(dependencies: dict):
    """
    Convert dependency dictionary into a directed graph.
    
    Edge direction:
    dependency -> file
    
    Example:
    parse.py imported by app.py
    
    parse.py → app.py
    """

    graph = nx.DiGraph()

    # create nodes
    for file in dependencies:
        graph.add_node(file)

    # create edges
    for file, imports in dependencies.items():

        for dep in imports:

            if dep == file:
                continue

            graph.add_edge(dep, file)

    return graph


def compute_depth_levels(graph: nx.DiGraph):
    """
    Compute architecture depth for each file.

    Higher depth = deeper dependency chain.
    """

    depth_map = {}

    for node in graph.nodes():

        try:
            paths = nx.single_source_shortest_path_length(graph, node)

            if paths:
                depth_map[node] = max(paths.values())
            else:
                depth_map[node] = 0

        except:
            depth_map[node] = 0

    return depth_map


def find_root_modules(graph: nx.DiGraph):
    """
    Files with no incoming dependencies.
    Usually entry points.
    """

    roots = []

    for node in graph.nodes():

        if graph.in_degree(node) == 0:
            roots.append(node)

    return roots


def find_leaf_modules(graph: nx.DiGraph):
    """
    Files that depend on nothing.
    """

    leaves = []

    for node in graph.nodes():

        if graph.out_degree(node) == 0:
            leaves.append(node)

    return leaves
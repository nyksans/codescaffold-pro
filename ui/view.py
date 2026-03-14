import json
import os
import streamlit.components.v1 as components


def render_graph(graph, structure, layers, entry_points):

    nodes = []
    edges = []

    layer_colors = {
        "frontend": "#60a5fa",
        "logic": "#a78bfa",
        "algorithms": "#fbbf24",
        "backend": "#34d399",
        "assets": "#94a3b8",
        "other": "#64748b"
    }

    layer_lookup = {}

    for layer, files in layers.items():
        for f in files:
            layer_lookup[f] = layer

    for node in graph.nodes():

        layer = layer_lookup.get(node, "other")
        color = layer_colors.get(layer, "#64748b")

        if node in entry_points:
            color = "#fb7185"

        nodes.append({
            "id": node,
            "label": node,
            "shape": "box",
            "borderWidth": 2,
            "color": {
                "background": "#0f172a",
                "border": color
            },
            "font": {
                "color": "#e5e7eb",
                "face": "monospace",
                "size": 13
            }
        })

    for s, t in graph.edges():

        edges.append({
            "from": s,
            "to": t,
            "arrows": "to",
            "smooth": {"type": "dynamic"},
            "color": "#475569"
        })

    graph_data = json.dumps({
        "nodes": nodes,
        "edges": edges,
        "structure": structure
    })

    html_path = os.path.join(
        os.path.dirname(__file__),
        "frontend",
        "index.html"
    )

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("__GRAPH_DATA__", graph_data)

    components.html(html, height=1000, scrolling=False)
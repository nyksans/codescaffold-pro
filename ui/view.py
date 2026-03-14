import json
import os
import ast
import streamlit.components.v1 as components

def get_uml_structure(file_path):
    structure = {"classes": []}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                # Extracting attributes (variables assigned within the class body)
                attributes = []
                for n in node.body:
                    if isinstance(n, ast.Assign):
                        for target in n.targets:
                            if isinstance(target, ast.Name):
                                attributes.append(target.id)
                
                structure["classes"].append({
                    "name": node.name,
                    "methods": methods,
                    "attributes": attributes
                })
    except Exception:
        pass
    return structure

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

    layer_lookup = {f: layer for layer, files in layers.items() for f in files}

    for node in graph.nodes():
        layer = layer_lookup.get(node, "other")
        color = layer_colors.get(layer, "#64748b")
        if node in entry_points:
            color = "#fb7185"

        # Analyze the file content for UML data
        uml_data = get_uml_structure(node)

        nodes.append({
            "id": node,
            "label": node,
            "shape": "box",
            "borderWidth": 2,
            "color": {"background": "#0f172a", "border": color},
            "font": {"color": "#e5e7eb", "face": "monospace", "size": 13},
            "umlDetails": uml_data
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

    html_path = os.path.join(os.path.dirname(__file__), "frontend", "index.html")

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read().replace("__GRAPH_DATA__", graph_data)

    components.html(html, height=620, scrolling=False)
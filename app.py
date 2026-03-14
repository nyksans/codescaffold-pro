import streamlit as st

from core.repo import clone_repository
from core.parse import parse_repository
from core.graph import build_dependency_graph
from core.dependency_intelligence import analyze_graph
from core.entry_detector import detect_entry_points
from core.architecture import detect_architecture

from ui.theme import apply_theme
from ui.layout import header, theme_toggle
from ui.view import render_graph


st.set_page_config(
    page_title="CodeScaffold",
    layout="wide"
)

# Theme toggle
theme_mode = theme_toggle()
apply_theme(theme_mode)

# Header
header()

st.markdown("<br>", unsafe_allow_html=True)

# Repo input
repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/user/repository"
)

analyze = st.button("Analyze Repository")


if analyze:

    if not repo_url:
        st.error("Please enter a repository URL")
        st.stop()

    # Clone repository
    with st.spinner("Cloning repository..."):

        try:
            repo_path = clone_repository(repo_url)

        except Exception as e:

            st.error(f"Clone failed: {e}")
            st.stop()

    # Parse repository
    with st.spinner("Parsing repository..."):

        try:
            deps, structure, files = parse_repository(repo_path)

        except Exception as e:

            st.error(f"Parser error: {e}")
            st.stop()

    # Build graph
    with st.spinner("Building dependency graph..."):

        graph = build_dependency_graph(deps)

    # Architecture analysis
    analysis = analyze_graph(graph)

    # Entry detection
    entry_points = detect_entry_points(files)

    # Layer detection
    layers = detect_architecture(files)

    st.success("Analysis complete")

    st.markdown("---")

    # Metrics section
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Files", len(files))
    col2.metric("Dependencies", graph.number_of_edges())
    col3.metric("Circular Dependencies", len(analysis["cycles"]))
    col4.metric("Dead Files", len(analysis["dead_files"]))

    st.markdown("---")

    # Render graph
    render_graph(
        graph,
        structure,
        layers,
        entry_points
    )
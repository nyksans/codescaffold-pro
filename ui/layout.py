import streamlit as st


def header():
    """
    Render main application header.
    """

    st.markdown(
        '<div class="main-title">CodeScaffold</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">Developer Architecture Explorer</div>',
        unsafe_allow_html=True
    )


def theme_toggle():
    """
    Theme switcher.
    """

    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "dark"

    col1, col2 = st.columns([6,1])

    with col2:

        if st.button("Toggle Theme"):

            if st.session_state.theme_mode == "dark":
                st.session_state.theme_mode = "light"
            else:
                st.session_state.theme_mode = "dark"

    return st.session_state.theme_mode


def layout_columns():
    """
    Create main UI layout columns.
    """

    left, center, right = st.columns([2,6,2])

    return left, center, right
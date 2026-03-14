import streamlit as st


def apply_theme(theme_mode="dark"):
    """
    Apply UI theme styling.
    Supports dark and light modes.
    """

    if theme_mode == "light":

        st.markdown(
            """
            <style>

            .stApp {
                background: #fafafa;
                color: #1f2933;
            }

            .main-title {
                font-size: 40px;
                font-weight: 700;
                color: #d63384;
                margin-bottom: 5px;
            }

            .sub-title {
                opacity: 0.7;
                margin-bottom: 25px;
            }

            .glass-card {
                background: white;
                border-radius: 12px;
                padding: 18px;
                border: 1px solid #f1f1f1;
                box-shadow: 0 2px 6px rgba(0,0,0,0.04);
            }

            .sidebar-card {
                background: #ffffff;
                border-radius: 10px;
                padding: 15px;
                border: 1px solid #eee;
                margin-bottom: 12px;
            }

            </style>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <style>

            .stApp {
                background: linear-gradient(135deg,#020617,#020617);
                color: #e5e7eb;
            }

            .main-title {
                font-size: 40px;
                font-weight: 700;
                letter-spacing: 1px;
            }

            .sub-title {
                opacity: 0.6;
                margin-bottom: 25px;
            }

            .glass-card {
                background: rgba(255,255,255,0.05);
                border-radius: 14px;
                padding: 20px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.08);
            }

            .sidebar-card {
                background: rgba(255,255,255,0.03);
                border-radius: 10px;
                padding: 15px;
                border: 1px solid rgba(255,255,255,0.05);
                margin-bottom: 12px;
            }

            </style>
            """,
            unsafe_allow_html=True
        )
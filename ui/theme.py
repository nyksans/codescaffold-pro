import streamlit as st


def apply_theme(theme_mode="dark"):
    """
    Apply a space-themed UI.
    Uses a darker variant for dark mode
    and a softer space-light variant for light mode.
    """

    if theme_mode == "light":
        css = """
        <style>
        .stApp {
            background:
              radial-gradient(circle at 10% 20%, rgba(56,189,248,0.16), transparent 55%),
              radial-gradient(circle at 80% 10%, rgba(129,140,248,0.18), transparent 55%),
              radial-gradient(circle at 50% 80%, rgba(52,211,153,0.12), transparent 55%),
              #e5e7eb;
            color: #0f172a;
        }

        .main-title {
            font-size: 40px;
            font-weight: 700;
            letter-spacing: 1px;
        }

        .sub-title {
            opacity: 0.7;
            margin-bottom: 25px;
        }

        .glass-card {
            background: rgba(255,255,255,0.9);
            border-radius: 14px;
            padding: 20px;
            backdrop-filter: blur(14px);
            border: 1px solid rgba(148,163,184,0.45);
            box-shadow: 0 20px 45px rgba(15,23,42,0.08);
        }

        .sidebar-card {
            background: rgba(255,255,255,0.95);
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(148,163,184,0.35);
            margin-bottom: 12px;
        }

        /* form controls in light mode */
        .stTextInput > label {
            font-weight: 500;
            color: #111827;
        }

        .stTextInput input {
            background: rgba(15,23,42,0.04) !important;
            border-radius: 999px !important;
            border: 1px solid rgba(148,163,184,0.7) !important;
            color: #020617 !important;
            box-shadow: 0 8px 20px rgba(15,23,42,0.15) !important;
        }

        .stTextInput input::placeholder {
            color: rgba(15,23,42,0.5) !important;
        }

        .stButton > button {
            border-radius: 999px;
            border: 1px solid rgba(15,23,42,0.8);
            background: linear-gradient(135deg,#0f172a,#1f2937);
            color: #f9fafb;
            font-weight: 500;
            box-shadow: 0 10px 30px rgba(15,23,42,0.45);
        }

        .stButton > button:hover {
            border-color: #0ea5e9;
            background: linear-gradient(135deg,#0ea5e9,#1d4ed8);
        }
        </style>
        """
    else:
        css = """
        <style>
        .stApp {
            background:
              radial-gradient(circle at 10% 20%, rgba(56,189,248,0.12), transparent 55%),
              radial-gradient(circle at 80% 10%, rgba(129,140,248,0.18), transparent 55%),
              radial-gradient(circle at 50% 80%, rgba(52,211,153,0.12), transparent 55%),
              #020617;
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
            background: rgba(15,23,42,0.9);
            border-radius: 14px;
            padding: 20px;
            backdrop-filter: blur(12px);
            border: 1px solid rgba(148,163,184,0.35);
            box-shadow: 0 20px 60px rgba(15,23,42,0.95);
        }

        .sidebar-card {
            background: rgba(15,23,42,0.92);
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(148,163,184,0.3);
            margin-bottom: 12px;
        }
        </style>
        """

    st.markdown(css, unsafe_allow_html=True)
"""
SgHealth-Optimize  |  Main Streamlit App
Interactive Analytics: Singapore Eldercare Demand & Accessibility Gaps
"""
import streamlit as st

st.set_page_config(
    page_title="SgHealth-Optimize",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Hide Streamlit's auto-generated multipage navigation links */
    section[data-testid="stSidebarNav"] {
        display: none;
    }
    /* Sidebar — match main page theme */
    section[data-testid="stSidebar"] {
        background-color: #F7F8FA;
        border-right: 1px solid #E5E7EB;
    }
    section[data-testid="stSidebar"] * {
        color: #1A1A2E !important;
    }
    section[data-testid="stSidebar"] .stRadio label {
        font-size: 0.95rem;
        padding: 6px 10px;
        border-radius: 6px;
        transition: background 0.15s;
    }
    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(0,0,0,0.05);
    }
    section[data-testid="stSidebar"] .stCaption,
    section[data-testid="stSidebar"] small {
        color: #6B7280 !important;
    }
    /* Main typography */
    .main-title { font-size: 2rem; font-weight: 700; color: #1A1A2E; letter-spacing: -0.5px; }
    .sub-title  { font-size: 1rem; color: #6B7280; margin-bottom: 1.5rem; }
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #1E3A5F 0%, #2D5986 100%);
        border-radius: 10px; padding: 18px 22px; color: white;
        margin-bottom: 10px;
    }
    .metric-card h3 { margin: 0; font-size: 2rem; font-weight: 700; }
    .metric-card p  { margin: 4px 0 0; font-size: 0.85rem; opacity: 0.8; }
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 12px; }
    .stTabs [data-baseweb="tab"] {
        font-size: 0.95rem; font-weight: 600; padding: 8px 18px;
        border-radius: 8px 8px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Preload all pipeline data once (cached) — page switches are instant ────────
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils.shared_data import get_pipeline_data

get_pipeline_data()  # warms st.cache_data; all pages reuse this result

# ── Navigation ─────────────────────────────────────────────────────────────────
# NOTE: page modules live in views/ (NOT pages/) — a folder literally named
# "pages" triggers Streamlit's automatic multipage navigation, which produced
# the broken duplicate sidebar links seen above the divider.
PAGES = {
    "Overview":          "views/overview",
    "Risk Map":          "views/risk_map",
    "Trends":            "views/trends",
    "Cluster Analysis":  "views/cluster_analysis",
}

with st.sidebar:
    st.markdown("### SgHealth-Optimize")
    st.markdown("<span style='font-size:0.82rem;color:#6B7280;'>Eldercare Demand & Accessibility Gaps</span>", unsafe_allow_html=True)
    st.divider()
    page = st.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
    st.divider()
    st.caption("Data: SingStat 2011–2025 | MOH | Data.gov.sg")

# ── Dynamic page routing ───────────────────────────────────────────────────────
if page == "Overview":
    import views.overview as p
elif page == "Risk Map":
    import views.risk_map as p
elif page == "Trends":
    import views.trends as p
else:
    import views.cluster_analysis as p

p.render()

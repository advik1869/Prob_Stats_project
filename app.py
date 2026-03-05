import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Global Health Data Analyzer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a Premium Look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #1e3a8a; /* Deep blue header */
        font-family: 'Inter', sans-serif;
    }
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 4px solid #3b82f6;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
st.title("🌍 Global Health Statistics Analyzer")
st.markdown("""
Welcome to the interactive Probability and Statistics project focusing on Global Health Metrics (WHO Life Expectancy Data).
This dashboard covers major statistical concepts including **Exploratory Data Analysis**, **Correlation**, **Multiple Regression**, and **ANOVA**.
""")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Cleaned_Life_Expectancy.csv")
        return df
    except FileNotFoundError:
        st.error("Error: Could not find Cleaned_Life_Expectancy.csv. Please ensure it is generated.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.markdown("### Dataset Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="metric-card"><h2>{df["country"].nunique()}</h2><p>Countries</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h2>{df["year"].min()} - {df["year"].max()}</h2><p>Time Span</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h2>{round(df["life_expectancy"].mean(), 1)}</h2><p>Global Avg Life Expectancy</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><h2>{df.shape[1]}</h2><p>Variables Analyzed</p></div>', unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### Raw Data Preview")
    st.dataframe(df, use_container_width=True)
    
    st.info("👈 Use the sidebar to navigate to specific statistical analyses (EDA, Correlation, Hypothesis Testing).")

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA", page_icon="📊", layout="wide")

st.title("📊 Exploratory Data Analysis (EDA)")

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Life_Expectancy.csv")

df = load_data()

st.markdown("""
### Data Visualization
Explore the distributions and relationships between different health and economic factors.
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### Variable Distribution")
    dist_var = st.selectbox("Select Variable to visualize distribution:", df.select_dtypes(include=['float64', 'int64']).columns)
    
    fig_hist = px.histogram(df, x=dist_var, marginal="box", 
                             title=f"Distribution of {dist_var.replace('_', ' ').title()}",
                             color_discrete_sequence=['#3b82f6'])
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.markdown("#### Bivariate Relationship (Scatter Plot)")
    scat_x = st.selectbox("Select X-axis:", df.select_dtypes(include=['float64', 'int64']).columns, index=df.columns.get_loc("gdp") if "gdp" in df.columns else 0)
    scat_y = st.selectbox("Select Y-axis:", df.select_dtypes(include=['float64', 'int64']).columns, index=df.columns.get_loc("life_expectancy") if "life_expectancy" in df.columns else 1)
    
    color_by = st.selectbox("Color By (Optional):", ["None"] + list(df.select_dtypes(include=['object']).columns))
    
    if color_by == "None":
        fig_scatter = px.scatter(df, x=scat_x, y=scat_y, opacity=0.6, 
                                 title=f"{scat_y.replace('_', ' ').title()} vs {scat_x.replace('_', ' ').title()}",
                                 color_discrete_sequence=['#ef4444'])
    else:
        fig_scatter = px.scatter(df, x=scat_x, y=scat_y, opacity=0.6, color=color_by,
                                 title=f"{scat_y.replace('_', ' ').title()} vs {scat_x.replace('_', ' ').title()} by {color_by.title()}")
        
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.markdown("#### Global Map Visualization")
if "country" in df.columns and "life_expectancy" in df.columns:
    # Get latest year data
    latest_year = df['year'].max()
    df_latest = df[df['year'] == latest_year]
    
    fig_map = px.choropleth(df_latest, locations="country", locationmode='country names',
                            color="life_expectancy", hover_name="country",
                            color_continuous_scale=px.colors.sequential.Viridis,
                            title=f"Global Life Expectancy ({latest_year})")
    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.info("Map visualization requires 'country' and 'life_expectancy' columns.")

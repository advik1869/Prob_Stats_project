import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import plotly.express as px

st.set_page_config(page_title="ANOVA & Hypothesis Testing", page_icon="🧪", layout="wide")

st.title("🧪 ANOVA & Hypothesis Testing")
st.markdown("""
This module covers **Module 6: Hypothesis Testing - II**.
We will use Analysis of Variance (ANOVA) to test if there are statistically significant differences between the means of three or more independent groups.
""")

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Life_Expectancy.csv")

df = load_data()

# We need categorical variables for ANOVA.
# Let's create an artificial 'Income Level' based on GDP quantiles since 'Status' is the only true categorical one in this dataset.
if 'gdp' in df.columns:
    df['income_level'] = pd.qcut(df['gdp'], q=3, labels=['Low', 'Medium', 'High'])

categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

if 'year' in numeric_cols: numeric_cols.remove('year')

tab1, tab2 = st.tabs(["1. One-Way ANOVA", "2. Two-Way ANOVA"])

with tab1:
    st.header("One-Way ANOVA")
    st.markdown("""
    Test if the mean of a dependent variable is the same across different categories of ONE independent variable.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
       cat_var = st.selectbox("Select Categorical Factor (Independent Variable):", categorical_cols, index=0)
    with col2:
       num_var = st.selectbox("Select Continuous Metric (Dependent Variable):", numeric_cols, index=numeric_cols.index('life_expectancy') if 'life_expectancy' in numeric_cols else 0)
    
    if cat_var and num_var:
        # Visualize the distribution
        fig_box = px.box(df, x=cat_var, y=num_var, color=cat_var, 
                         title=f"Distribution of {num_var.replace('_', ' ').title()} by {cat_var.replace('_', ' ').title()}")
        st.plotly_chart(fig_box, use_container_width=True)
        
        if st.button("Run One-Way ANOVA"):
            # Group data
            groups = df.groupby(cat_var)[num_var].apply(list)
            
            # Perform ANOVA
            f_stat, p_val = stats.f_oneway(*groups)
            
            st.subheader("Results")
            res_col1, res_col2 = st.columns(2)
            res_col1.metric("F-Statistic", f"{f_stat:.4f}")
            res_col2.metric("P-Value", f"{p_val:.4e}")
            
            if p_val < 0.05:
                st.success(f"**Conclusion:** The P-Value is less than 0.05. We reject the null hypothesis. There is a statistically significant difference in {num_var.replace('_', ' ').title()} across different {cat_var.replace('_', ' ').title()} groups.")
            else:
                st.warning(f"**Conclusion:** The P-Value is greater than 0.05. We fail to reject the null hypothesis. There is no statistically significant difference.")

with tab2:
    st.header("Two-Way ANOVA")
    st.markdown("""
    Test the main and interaction effects of TWO categorical independent variables on a continuous dependent variable.
    """)
    
    if len(categorical_cols) >= 2:
        col1, col2, col3 = st.columns(3)
        with col1:
             factor1 = st.selectbox("Select Factor 1:", categorical_cols, index=0, key='f1')
        with col2:
             factor2 = st.selectbox("Select Factor 2:", categorical_cols, index=1 if len(categorical_cols)>1 else 0, key='f2')
        with col3:
             dep_var = st.selectbox("Select Dependent Variable:", numeric_cols, index=numeric_cols.index('life_expectancy') if 'life_expectancy' in numeric_cols else 0, key='dv')
             
        if factor1 == factor2:
            st.error("Please select two different categorical factors.")
        else:
            if st.button("Run Two-Way ANOVA"):
                # Clean column names for statsmodels formula
                df_clean = df.copy()
                f1_safe = factor1.replace(" ", "_").replace("-", "_")
                f2_safe = factor2.replace(" ", "_").replace("-", "_")
                dv_safe = dep_var.replace(" ", "_").replace("-", "_")
                
                df_clean.rename(columns={factor1: f1_safe, factor2: f2_safe, dep_var: dv_safe}, inplace=True)
                
                formula = f"{dv_safe} ~ C({f1_safe}) + C({f2_safe}) + C({f1_safe}):C({f2_safe})"
                model = ols(formula, data=df_clean).fit()
                anova_table = sm.stats.anova_lm(model, typ=2)
                
                st.subheader("ANOVA Table")
                
                # Format the table for display
                def highlight_pval(val):
                    if isinstance(val, (int, float)) and val < 0.05:
                        return 'background-color: #4ade80'
                    return ''
                    
                st.dataframe(anova_table.style.applymap(highlight_pval, subset=['PR(>F)']), use_container_width=True)
                st.caption("Green highlights denote statistical significance (p < 0.05).")
    else:
         st.warning("Not enough categorical variables found for Two-Way ANOVA. The dataset needs at least two categorical features.")

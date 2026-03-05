import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
from scipy import stats

st.set_page_config(page_title="Correlation & Regression", page_icon="📈", layout="wide")

st.title("📈 Correlation & Regression Analysis")
st.markdown("""
This module covers **Module 3: Correlation and Regression**.
Investigate how different variables interact with each other and build predictive models.
""")

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Life_Expectancy.csv")

df = load_data()
numeric_df = df.select_dtypes(include=[np.number])

tab1, tab2 = st.tabs(["1. Correlation Matrix", "2. Multiple Linear Regression"])

with tab1:
    st.header("Correlation Analysis")
    st.markdown("Analyze the linear relationship between continuous variables.")
    
    corr_method = st.radio("Correlation Method:", ["Pearson", "Spearman (Rank)"], horizontal=True)
    method = 'pearson' if corr_method == "Pearson" else 'spearman'
    
    vars_to_corr = st.multiselect("Select variables to correlate:", numeric_df.columns, 
                                  default=["life_expectancy", "adult_mortality", "infant_deaths", "alcohol", "gdp", "bmi", "schooling"])
    
    if len(vars_to_corr) > 1:
        corr_matrix = numeric_df[vars_to_corr].corr(method=method)
        
        fig_corr = px.imshow(corr_matrix, text_auto=".2f", aspect="auto",
                             color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
                             title=f"{corr_method} Correlation Matrix")
        st.plotly_chart(fig_corr, use_container_width=True)
        
        st.info("""
        **Interpretation:** 
        * Values close to 1 indicate a strong positive correlation.
        * Values close to -1 indicate a strong negative correlation.
        * Values close to 0 indicate little or no linear correlation.
        """)
    else:
        st.warning("Please select at least two variables.")

with tab2:
    st.header("Multiple Linear Regression")
    st.markdown("""
    Predict a target variable based on multiple predictor variables.
    
    > **⚠️ Note:** The Target Variable (Y) represents the dependent variable you are trying to predict. The Predictor Variables (X) represent the independent variables. 
    > **You cannot choose the same variable for both X and Y.** If your chosen Target Variable happens to be in the default Predictor list below, please remove it from the Predictor list first to avoid calculating a regression against itself!
    """)
    
    target_var = st.selectbox("Select Target Variable (Y):", numeric_df.columns, index=numeric_df.columns.get_loc("life_expectancy") if "life_expectancy" in numeric_df.columns else 0)
    
    predictor_vars = st.multiselect(
        "Select Predictor Variables (X):", 
        numeric_df.columns, 
        default=["adult_mortality", "gdp", "bmi", "schooling"] if all(x in numeric_df.columns for x in ["adult_mortality", "gdp", "bmi", "schooling"]) else []
    )
    
    if target_var in predictor_vars:
        st.warning(f"⚠️ **{target_var}** is the independent (Target) variable. It cannot simultaneously be chosen as a predictor (X). Please remove it from the Predictors list to run the model.")
        
    if st.button("Run Regression Model"):
        if target_var in predictor_vars:
            st.error(f"Cannot run model. Please remove '{target_var}' from the Predictor Variables (X).")
        elif len(predictor_vars) > 0:
            X = numeric_df[predictor_vars]
            y = numeric_df[target_var]
            
            # Add constant for intercept
            X = sm.add_constant(X)
            
            # Fit OLS model
            model = sm.OLS(y, X).fit()
            
            st.subheader("Regression Results Summary")
            
            # Display key metrics in cards
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("R-squared", f"{model.rsquared:.4f}")
            col2.metric("Adj. R-squared", f"{model.rsquared_adj:.4f}")
            col3.metric("F-statistic", f"{model.fvalue:.2f}")
            col4.metric("Prob (F-statistic)", f"{model.f_pvalue:.4e}")
            
            st.markdown("#### Coefficients")
            # Extract coefficients and p-values into a dataframe for display
            results_df = pd.DataFrame({
                "Coefficient": model.params,
                "Std Error": model.bse,
                "t-value": model.tvalues,
                "P>|t|": model.pvalues
            })
            
            # Highlight significant p-values
            def highlight_sig(val):
                color = '#4ade80' if val < 0.05 else ''
                return f'background-color: {color}'
            
            st.dataframe(results_df.style.applymap(highlight_sig, subset=['P>|t|']), use_container_width=True)
            st.caption("Green highlights denote statistically significant predictors (p < 0.05).")
            
            st.markdown("#### Regression Equation")
            eq = f"{target_var} = {model.params['const']:.2f} "
            for var in predictor_vars:
                coef = model.params[var]
                sign = "+" if coef >= 0 else "-"
                eq += f"{sign} {abs(coef):.4f} * {var} "
            st.latex(eq.replace("_", "\\_"))
            
        else:
            st.error("Please select at least one predictor variable.")

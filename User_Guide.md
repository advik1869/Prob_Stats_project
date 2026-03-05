# Global Health Data Analyzer: User Guide and Project Documentation

## Introduction
The **Global Health Data Analyzer** is an interactive web-based dashboard built using Python and Streamlit. It leverages the standard World Health Organization (WHO) Life Expectancy dataset to demonstrate and apply core statistical concepts: Exploratory Data Analysis (EDA), Correlation, Linear Regression, and Analysis of Variance (ANOVA).

This guide will walk you through each page of the application, explain the statistical reasoning behind the visualizations, and instruct you on how to use the interactive tools.

---

## Page 1: Landing Page & Dataset Overview (`app.py`)

### What This Page Does
The landing page serves as the entry point to the application. It provides an immediate, high-level understanding of the dataset's scope and contents before diving into complex mathematical relationships. 

### How to Use It
1. **Review High-Level Metrics:** At the top of the page, four key metric cards summarize the dataset:
   - **Countries:** 193 total countries are analyzed.
   - **Time Span:** Data spans from the year 2000 to 2015.
   - **Global Avg Life Expectancy:** The overall baseline life expectancy is calculated (69.2 years).
   - **Variables Analyzed:** There are 22 different health, economic, and social variables available for testing.
2. **Inspect the Raw Data Preview:** Scroll through the interactive table to view the raw numbers. This allows you to understand the data types (e.g., continuous variables like `infant_deaths` vs categorical variables like `status`).
3. **Navigate:** Use the sidebar on the left side of the screen to select the specific statistical module you wish to explore.

---

## Page 2: Exploratory Data Analysis (EDA)

### What This Page Does
In statistics and machine learning, EDA is the critical first step. It is used to visually understand the shape of the data, spot outliers, and verify if variables are normally distributed.

### How to Use It
1. **Variable Distribution (Left Panel):** 
   - **Action:** Select any continuous variable (e.g., `life_expectancy` or `gdp`) from the dropdown.
   - **Interpretation:** The dashboard generates a combined Histogram and Box Plot. The blue bars show the frequency of the data, helping you identify if the data follows a normal (bell-curve) distribution or if it is skewed. The box plot above it displays the statistical quartiles (median, 25th, and 75th percentiles) and visually flags outliers.
2. **Bivariate Relationship (Right Panel):**
   - **Action:** Select an X-axis variable and a Y-axis variable to compare two metrics simultaneously. You can also optionally color the data points by a category (like `Status`).
   - **Interpretation:** This generates a Scatter Plot. Every dot represents a country in a given year. If the dots form a clear upwards or downwards sloping line, it visually indicates that the two variables are correlated. A scattered, random cloud indicates no correlation. Coloring the dots allows you to see if these trends differ between Developed and Developing nations.

---

## Page 3: Correlation & Regression Analysis

### What This Page Does
This page covers **Module 3** of the syllabus. It mathematically quantifies the relationships you visualized on the EDA page and builds predictive algorithms.

### How to Use It
1. **Tab 1: Correlation Matrix:**
   - **Action:** Select two or more variables from the multiselect box. Choose either the **Pearson** (for linear relationships) or **Spearman Rank** (for non-linear monotonic relationships) correlation method.
   - **Interpretation:** The system generates a heatmap. Values closer to `1` (dark blue) indicate a strong positive correlation (as one variable goes up, the other goes up). Values closer to `-1` (dark red) indicate a strong negative correlation. Values near `0` indicate no linear relationship.
2. **Tab 2: Multiple Linear Regression:**
   - **Action:** Select a single "Target Variable (Y)" (e.g., `life_expectancy`) that you want to predict. Then, select multiple "Predictor Variables (X)" (e.g., `gdp`, `alcohol`, `schooling`). Click "Run Regression Model".
   - **Interpretation:** The dashboard uses Ordinary Least Squares (OLS) to fit a model and outputs:
     - **R-squared:** The percentage of variance in your target variable explained by your predictors (closer to 1.0 is better).
     - **P-Values:** The table highlights statistically significant predictors in green (P-value < 0.05). If a variable is not green, it does not meaningfully help predict the target.
     - **Regression Equation:** A fully generated mathematical equation you can use to calculate the target variable by hand.

---

## Page 4: ANOVA & Hypothesis Testing

### What This Page Does
This page covers **Module 6** of the syllabus. Analysis of Variance (ANOVA) is used to test if there are statistically significant differences between the means of three or more independent categorical groups.

### How to Use It
1. **Tab 1: One-Way ANOVA:**
   - **Action:** Select a Categorical Factor (e.g., `status` or the automatically generated `income_level`) and a Continuous Metric (e.g., `life_expectancy`). Click "Run One-Way ANOVA".
   - **Interpretation:** The dashboard first visualizes the groups side-by-side using a Box Plot. It then calculates the F-Statistic and the P-Value. If the P-Value is less than 0.05, the dashboard outputs a success message indicating you can reject the Null Hypothesis (i.e., there *is* a statistically significant difference between the groups).
2. **Tab 2: Two-Way ANOVA:**
   - **Action:** Select two *different* Categorical Factors and one Dependent Variable. Click "Run Two-Way ANOVA".
   - **Interpretation:** This tests the interaction effects (e.g., Does the effect of Income Level on Life Expectancy change depending on the Status of the country?). It outputs an ANOVA table and highlights any statistically significant interactions in green.

---
*Created for the Probability and Statistics Final Project.*

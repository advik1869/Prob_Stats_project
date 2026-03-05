# 🌍 Global Health Data Analyzer

An interactive web dashboard built with **Python** and **Streamlit** that analyzes the WHO Life Expectancy dataset using core statistical techniques from a Probability & Statistics course.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Features

| Page | Statistical Concepts Covered |
|------|------------------------------|
| **Exploratory Data Analysis** | Histograms, Box Plots, Scatter Plots, Choropleth Maps |
| **Correlation & Regression** | Pearson & Spearman Correlation Matrix, Multiple Linear Regression (OLS) |
| **ANOVA & Hypothesis Testing** | One-Way ANOVA, Two-Way ANOVA, F-Test, P-Value Interpretation |

## 📊 Dataset

This project uses the **WHO Life Expectancy** dataset containing health, economic, and social indicators for **193 countries** spanning **2000–2015** (22 variables, 2938 records).

The dataset is automatically downloaded and cleaned when you first run the app.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/health-data-analyzer.git
cd health-data-analyzer

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Download & Clean the Data

```bash
python3 download_data.py
python3 data_loader.py
```

### Run the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## 📂 Project Structure

```
health_data_analyzer/
├── app.py                          # Main landing page
├── pages/
│   ├── 1_Exploratory_Data_Analysis.py
│   ├── 2_Correlation_&_Regression.py
│   └── 3_ANOVA_&_Hypothesis_Testing.py
├── data_loader.py                  # Dataset cleaning & preprocessing
├── download_data.py                # Dataset download script
├── make_pdf.py                     # PDF documentation generator
├── User_Guide.md                   # Detailed user guide
├── WHO_Life_Expectancy.csv         # Raw dataset (auto-downloaded)
├── requirements.txt
├── .gitignore
└── README.md
```

## 📖 User Guide

A detailed PDF guide explaining each page and how to interpret the statistical outputs is included. To generate it:

```bash
python3 make_pdf.py
```

This creates `Global_Health_Data_Analyzer_Guide.pdf` in the project root.

## 🧪 Statistical Methods Used

- **Measures of Central Tendency & Dispersion** — via EDA histograms and box plots
- **Pearson & Spearman Rank Correlation** — interactive heatmap
- **Multiple Linear Regression (OLS)** — with R², Adjusted R², F-statistic, P-values, and the full regression equation
- **One-Way ANOVA** — testing significance across categorical groups
- **Two-Way ANOVA** — testing interaction effects between two categorical factors

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- **World Health Organization (WHO)** — for the Life Expectancy dataset
- **Streamlit** — for the interactive web framework
- **Statsmodels & SciPy** — for the statistical computation engines

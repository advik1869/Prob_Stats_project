import pandas as pd
import numpy as np

def load_and_clean_data(filepath="WHO_Life_Expectancy.csv"):
    """Loads and preprocesses the WHO Life Expectancy dataset."""
    df = pd.read_csv(filepath)
    
    # 1. Clean Column Names (strip whitespace, make lowercase, replace spaces with underscores)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')
    
    # Clean specific tricky columns if they exist
    df = df.rename(columns={
        'life_expectancy': 'life_expectancy',
        'thinness__1_19_years': 'thinness_1_19_years',
        'thinness_5_9_years': 'thinness_5_9_years'
    })

    # 2. Handle Missing Values
    # For a project of this scope, we can fill numeric NAs with the column mean
    # grouped by the Country (or global mean if country mean is also NA)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        if col != 'year': # Don't fill year
            # Fill with country mean first
            df[col] = df.groupby('country')[col].transform(lambda x: x.fillna(x.mean()))
            # If still NA (e.g. whole country is missing that metric), fill with global mean
            df[col] = df[col].fillna(df[col].mean())
            
    return df

if __name__ == "__main__":
    df = load_and_clean_data()
    print("Cleaned Data Shape:", df.shape)
    print("\nMissing values after cleaning:")
    print(df.isnull().sum()[df.isnull().sum() > 0])
    print("\nColumns:", df.columns.tolist())
    df.to_csv("Cleaned_Life_Expectancy.csv", index=False)
    print("\nSaved to Cleaned_Life_Expectancy.csv")

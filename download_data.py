import pandas as pd
import urllib.request
from io import BytesIO
from zipfile import ZipFile

url = "https://github.com/magoZion/ds-machine-learning/raw/main/Life%20Expectancy%20Data.zip"
print("Downloading from:", url)

try:
    with urllib.request.urlopen(url) as response:
        with ZipFile(BytesIO(response.read())) as z:
            # Assuming there's only one CSV in the zip
            csv_filename = [f for f in z.namelist() if f.endswith('.csv')][0]
            with z.open(csv_filename) as f:
                df = pd.read_csv(f)
                df.to_csv("Life_Expectancy_Data.csv", index=False)
                print("Successfully downloaded and saved Life_Expectancy_Data.csv")
                print(df.head())
except Exception as e:
    print("Error:", e)

# Fallback direct download if zip fails:
fallback_url = "https://raw.githubusercontent.com/Kumar-laxmi/Statistical_Methods_for_Decision_Making/main/Life%20Expectancy%20Data.csv"
try:
    df_fallback = pd.read_csv(fallback_url)
    df_fallback.to_csv("Life_Expectancy_Data.csv", index=False)
    print("Successfully downloaded fallback datset.")
    print(df_fallback.head())
except Exception as e:
    print("Fallback failed:", e)

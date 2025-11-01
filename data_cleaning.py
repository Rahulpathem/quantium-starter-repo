# data_cleaning.py
import pandas as pd
import glob
import os

# 1) Find all CSVs in data/
csv_paths = glob.glob(os.path.join("data", "daily_sales_data_*.csv"))
if not csv_paths:
    raise FileNotFoundError("No CSV files found at data/daily_sales_data_*.csv")

# 2) Read + combine
dfs = [pd.read_csv(p) for p in csv_paths]
df = pd.concat(dfs, ignore_index=True)

# 3) Keep only Pink Morsel (case-insensitive to be safe)
df = df[df["product"].str.lower() == "pink morsel"]

# 4) Clean price and compute sales
# price is like "$4.99" → strip $ and convert to float
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
df["sales"] = df["price"] * df["quantity"]

# 5) Keep only the requested columns with exact names
out = df.rename(columns={"date": "Date", "region": "Region", "sales": "Sales"})[["Sales", "Date", "Region"]]

# 6) Save
out_path = os.path.join("data", "processed_sales_data.csv")
out.to_csv(out_path, index=False)

# Optional quick sanity print
print("Rows:", len(out))
print(out.head(5).to_string(index=False))
print(f"\nSaved -> {out_path}")

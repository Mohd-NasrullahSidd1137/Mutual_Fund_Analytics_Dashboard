import pandas as pd

# Load Fund Master
df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*70)
print("Fund Master Analysis")
print("="*70)

print("\nDataset Shape")
print(df.shape)

print("\nUnique Fund Houses")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses")
print(df["fund_house"].nunique())

print("\nCategories")
print(df["category"].unique())

print("\nSub Categories")
print(df["sub_category"].unique())

print("\nRisk Categories")
print(df["risk_category"].unique())

print("\nPlans")
print(df["plan"].unique())
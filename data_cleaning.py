import os
import pandas as pd

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

# -----------------------------
# 1. NAV HISTORY
# -----------------------------
print("Cleaning: 02_nav_history.csv")

nav = pd.read_csv(f"{RAW_PATH}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav = nav.drop_duplicates()

nav.to_csv(f"{PROCESSED_PATH}/02_nav_history.csv", index=False)

print("✅ NAV History Cleaned")

# -----------------------------
# 2. INVESTOR TRANSACTIONS
# -----------------------------
print("Cleaning: 08_investor_transactions.csv")

txn = pd.read_csv(f"{RAW_PATH}/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

txn["transaction_type"] = txn["transaction_type"].str.title()

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending", "Rejected"]

txn = txn[txn["kyc_status"].isin(valid_kyc)]

txn = txn.drop_duplicates()

txn.to_csv(f"{PROCESSED_PATH}/08_investor_transactions.csv", index=False)

print("✅ Investor Transactions Cleaned")

# -----------------------------
# 3. SCHEME PERFORMANCE
# -----------------------------
print("Cleaning: 07_scheme_performance.csv")

perf = pd.read_csv(f"{RAW_PATH}/07_scheme_performance.csv")

perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

perf = perf.drop_duplicates()

perf.to_csv(f"{PROCESSED_PATH}/07_scheme_performance.csv", index=False)

print("✅ Scheme Performance Cleaned")

print("\n🎉 Day 2 Data Cleaning Completed Successfully!")
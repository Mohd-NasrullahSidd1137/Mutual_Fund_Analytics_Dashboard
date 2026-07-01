import os
import pandas as pd

print("=" * 70)
print("Bluestock Mutual Fund Analytics Platform")
print("Day 1 - Data Ingestion")
print("=" * 70)

# Dataset folder
DATA_PATH = "data/raw"

# Read all csv files
csv_files = sorted(
    [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]
)

print(f"\nTotal CSV Files Found : {len(csv_files)}")

for file in csv_files:

    file_path = os.path.join(DATA_PATH, file)

    print("\n" + "=" * 70)
    print(f"Dataset : {file}")
    print("=" * 70)

    df = pd.read_csv(file_path)

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

print("\n" + "=" * 70)
print("All datasets loaded successfully.")
print("=" * 70)
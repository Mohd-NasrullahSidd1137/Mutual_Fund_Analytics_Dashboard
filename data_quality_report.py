import os
import pandas as pd

folder = "data/raw"

print("="*70)
print("Data Quality Summary")
print("="*70)

for file in sorted(os.listdir(folder)):

    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(folder,file))

        print(f"\n{file}")

        print(f"Rows : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")
        print(f"Missing : {df.isnull().sum().sum()}")
        print(f"Duplicates : {df.duplicated().sum()}")
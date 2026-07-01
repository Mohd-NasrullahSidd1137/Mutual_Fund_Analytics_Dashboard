import os
import requests
import pandas as pd

# Folder jahan CSV save hongi
OUTPUT_FOLDER = "data/raw"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# AMFI Scheme Codes
funds = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 70)
print("Fetching Live NAV Data")
print("=" * 70)

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"{fund_name}.csv"

        nav_df.to_csv(
            os.path.join(OUTPUT_FOLDER, file_name),
            index=False
        )

        print(f"✅ {fund_name} downloaded successfully")

    except Exception as e:
        print(f"❌ Error downloading {fund_name}")
        print(e)

print("\nAll NAV files downloaded successfully.")
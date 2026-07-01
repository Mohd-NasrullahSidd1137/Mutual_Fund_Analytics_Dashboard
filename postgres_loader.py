import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

USERNAME = "postgres"
PASSWORD = quote_plus("Shanu@1137")   # <-- Apna password
HOST = "localhost"
PORT = "5433"
DATABASE = "bluestock_mf"

engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

DATA_PATH = "data/processed"

csv_files = sorted(
    [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]
)

print("=" * 70)
print("Loading CSV Files into PostgreSQL")
print("=" * 70)

for file in csv_files:

    table_name = file.replace(".csv", "")

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ {table_name} loaded successfully")

print("\n🎉 All tables loaded into PostgreSQL!")
from urllib.parse import quote_plus
from sqlalchemy import create_engine

USERNAME = "postgres"
PASSWORD = quote_plus("Shanu@1137")

HOST = "localhost"
PORT = "5433"
DATABASE = "bluestock_mf"

engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

try:
    connection = engine.connect()
    print("✅ PostgreSQL Connected Successfully!")
    connection.close()

except Exception as e:
    print(e)
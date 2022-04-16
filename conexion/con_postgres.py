import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

postgres = psycopg2.connect(
    host=os.environ.get("HOST_POSTGRESQL"),
    database=os.environ.get("DATABASE_POSTGRESQL"),
    user=os.environ.get("USER_POSTGRESQL"),
    port=os.environ.get("PORT_POSTGRESQL"),
    password=os.environ.get("PASSWORD_POSTGRESQL")
)


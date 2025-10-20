import os

import psycopg2
from psycopg2.extras import RealDictCursor

host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("USER")
password = os.getenv("PASSWORD")


try:
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        cursor_factory=RealDictCursor,
    )
    cursor = conn.cursor()
    print("Database Connection was successful")
except:
    return {"message": "db connection failed"}

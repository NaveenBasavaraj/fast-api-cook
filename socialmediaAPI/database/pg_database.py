import os

import psycopg2
from psycopg2.extras import RealDictCursor

host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

attempts = 1
while attempts <= 2:
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
        break
    except Exception as e:
        attempts += 1
        print(f"error connecting to db {e}")

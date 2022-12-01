from psycopg2 import connect
from psycopg2._psycopg import connection, cursor

dsn = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "port": "5432",
    "host": "localhost",
}

try:
    with connect(**dsn) as conn:
        conn: connection

        with conn.cursor() as cur:
            cur: cursor

            cur.execute("create database test;")
        conn.commit()
    print("finish")
finally:
    conn.close()

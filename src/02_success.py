from typing import Optional

from psycopg2 import connect
from psycopg2._psycopg import connection, cursor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

dsn = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "port": "5432",
    "host": "localhost",
}


conn: Optional[connection] = None
try:
    conn = connect(**dsn)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    with conn.cursor() as cur:
        cur: cursor

        cur.execute("create database test;")
finally:
    if conn:
        conn.close()

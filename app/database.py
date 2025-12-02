from mysql.connector import pooling
from contextlib import contextmanager

db_pool = pooling.MySQLConnectionPool(
    pool_size=5,
    pool_name="mypool",
    host="localhost",
    user="root",
    password="root1234",
    database="app"
)

@contextmanager
def get_db():
    conn = db_pool.get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        yield conn, cur
    finally:
        cur.close()
        conn.close()

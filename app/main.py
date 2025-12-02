from fastapi import FastAPI
from .database import get_db
from .auth import router as auth_router
from .users import router as items_router

app = FastAPI()

def init_db():
    with get_db() as (conn, cur):
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) UNIQUE,
                password TEXT
            ) ENGINE=InnoDB;
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                user_id INT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            ) ENGINE=InnoDB;
        """)

        conn.commit()

# Initialize database
init_db()

# Include routers
app.include_router(auth_router)
app.include_router(items_router)

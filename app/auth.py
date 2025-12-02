from fastapi import APIRouter, HTTPException
from .database import get_db
from .schemas import Register, Login, UserOut
from .security import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=UserOut)
def register(data: Register):
    # use 'with' for context manager
    with get_db() as (conn, cur):
        # check if email exists
        cur.execute("SELECT * FROM users WHERE email=%s", (data.email,))
        if cur.fetchone():
            raise HTTPException(400, "Email already registered")

        # hash password
        hashed = hash_password(data.password)

        # insert new user
        cur.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (data.email, hashed)
        )
        conn.commit()

        return {"id": cur.lastrowid, "email": data.email}

@router.post("/login")


@router.post("/login")
def login(data: Login):
    with get_db() as (conn, cur):
        cur.execute("SELECT * FROM users WHERE email=%s", (data.email,))
        user = cur.fetchone()
        if not user:
            raise HTTPException(400, "Invalid email or password")

        if not verify_password(data.password, user["password"]):
            raise HTTPException(400, "Invalid email or password")

        token = create_token({"user_id": user["id"]})
        return {"access_token": token, "token_type": "bearer"}

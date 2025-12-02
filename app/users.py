from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from .database import get_db
from .security import decode_token
from .schemas import ItemCreate, ItemOut

router = APIRouter(prefix="/items")
auth = HTTPBearer()

def get_current_user(token=Depends(auth)):
    try:
        return decode_token(token.credentials)
    except:
        raise HTTPException(401, "Invalid or expired token")


@router.post("/", response_model=ItemOut)
def create_item(data: ItemCreate, user=Depends(get_current_user)):
    conn, cur = get_db()

    cur.execute(
        "INSERT INTO items (title, user_id) VALUES (%s, %s)",
        (data.title, user["id"])
    )
    conn.commit()

    return {"id": cur.lastrowid, "title": data.title, "user_id": user["id"]}


@router.get("/", response_model=list[ItemOut])
def get_items(user=Depends(get_current_user)):
    conn, cur = get_db()

    cur.execute("SELECT * FROM items WHERE user_id=%s", (user["id"],))
    rows = cur.fetchall()

    return rows

from typing import Optional
from fastapi import Depends, FastAPI, Header
from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None, token: str = Depends(oauth2_scheme)):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, token: str = Depends(oauth2_scheme)):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
from __future__ import annotations

from app.db.crud.shortlink import (
    create_shortlink,
    get_original_url_and_meta_data,
)
from app.db.schemas.shortlink import (
    ShortlinkCreate,
    ShortlinkInverse,
    ShortlinkOut,
)
from app.db.session import get_db
from fastapi import APIRouter, Depends

shortlink_router = r = APIRouter()


@r.post("/shortlink", response_model=ShortlinkOut)
async def generate_shortlink(shortlink: ShortlinkCreate, db=Depends(get_db)):
    """
    Return shortened URL pointing to Long-Form URL.
    """
    return create_shortlink(db, shortlink)


@r.get(
    "/shortlink/{key_str}",
    response_model=ShortlinkInverse,
)
async def original_url_and_meta_data(key_str: str, db=Depends(get_db)):
    """
    Return original URL aliased by shortened URL.
    """
    return get_original_url_and_meta_data(db, key_str)

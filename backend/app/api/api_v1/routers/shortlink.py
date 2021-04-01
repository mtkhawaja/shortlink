from __future__ import annotations


import app.db.crud.shortlink as sl_crud
import app.db.schemas.shortlink as sl_schema
from app.db.session import get_db
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND


shortlink_router = r = APIRouter()


@r.post("/shortlink", response_model=sl_schema.ShortlinkKey)
async def create_shortlink(
    shortlink: sl_schema.ShortlinkCreate, db=Depends(get_db)
):
    """
    Return shortened URL key string pointing to Long-Form URL
    along with an expiry timestamp.
    """
    return sl_crud.create_shortlink(db, shortlink)


@r.get(
    "/shortlink/{key_str}/meta/",
    response_model=sl_schema.ShortlinkMeta,
)
async def get_original_url_and_meta_data(key_str: str, db=Depends(get_db)):
    """
    Return original url aliased by shortened URL
    along with related metadata.
    """
    return sl_crud.get_original_url_and_meta_data(db, key_str)


@r.get(
    "/shortlink/{key_str}",
    response_model=sl_schema.ShortlinkOriginal,
)
async def get_original_url_and_expiry(key_str: str, db=Depends(get_db)):
    """
    Return original URL aliased by shortened URL key string.
    """
    return sl_crud.get_original_url_and_expiry(db, key_str)


@r.get("/shortlink/redirect/{key_str}")
async def original_url_redirect(key_str: str, db=Depends(get_db)):
    """
    Redirect to original url aliased by shortlink key string if
    it exists. If a URL doesn't exist, redirect configured default
    url.
    """
    response_url = sl_crud.get_original_url(db, key_str)
    return RedirectResponse(url=response_url, status_code=HTTP_302_FOUND)

import logging
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from src.db.schemas.general import Message
from src.db.schemas.short_link_schemas import ShortLinkCreate, ShortLinkResponse
from src.services.short_link_service import ShortLinkService
from src.settings.caching import ShortLinkCache
from src.settings.dependencies import get_db, get_settings, get_conversion_service, get_short_link_cache

short_link_router = APIRouter(prefix="/v1")
logger = logging.getLogger(__name__)
conversion_service = get_conversion_service(get_settings().conversion_base)


@short_link_router.post("/create/", response_model=ShortLinkResponse)
def create_short_link(short_link_create: ShortLinkCreate,
                      db: Session = Depends(get_db),
                      cache: ShortLinkCache = Depends(get_short_link_cache)):
    logger.debug(f"Received request to shorten url: '{short_link_create.original_url}'")
    response: Optional[ShortLinkResponse] = cache.retrieve_write(short_link_create.original_url)
    if not response:
        response = ShortLinkService.create_short_link(db, short_link_create.original_url, conversion_service)
        logger.info(f"Created short link code: '{response.key_string}' for url '{response.original_url}'")
        cache.cache_write(response)
    return response


@short_link_router.get("/resolve/{key_string}", response_model=ShortLinkResponse, responses={404: {"model": Message}})
def get_original_link(key_string: str,
                      db: Session = Depends(get_db),
                      cache: ShortLinkCache = Depends(get_short_link_cache)):
    logger.debug(f"Received request to resolve url for short link key string: '{key_string}'")
    response: Optional[ShortLinkResponse] = cache.retrieve_read(key_string)
    if not response:
        response = ShortLinkService.get_short_link(db, key_string, conversion_service)
        if response:
            logger.info(f"Resolved short link code: '{key_string}' to url '{response.original_url}'")
            cache.cache_read(response)
        else:
            return JSONResponse(status_code=404,
                                content={"message": f"Original url for '{key_string}' does not exist"})
    return response

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.db.schemas import short_link_schemas
from src.db.schemas.short_link_schemas import ShortLinkCreate
from src.services.short_link_service import ShortLinkService
from src.settings.database import Base, engine
from src.settings.dependencies import get_db, get_settings, get_conversion_service

short_link_router = APIRouter(prefix="/v1")

settings = get_settings()
conversion_service = get_conversion_service(settings.conversion_base)
Base.metadata.create_all(bind=engine)


@short_link_router.post("/create/", response_model=short_link_schemas.ShortLinkResponse)
def create_short_link(short_link_create: ShortLinkCreate, db: Session = Depends(get_db)):
    response = ShortLinkService.create_short_link(db, short_link_create.original_url, conversion_service)
    return JSONResponse(content=response.dict())


@short_link_router.get("/resolve/{key_string}", response_model=short_link_schemas.ShortLinkResponse)
def get_original_link(key_string: str, db: Session = Depends(get_db)):
    response = ShortLinkService.get_short_link(db, key_string, conversion_service)
    return JSONResponse(content=response.dict())

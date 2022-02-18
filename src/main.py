import logging

from fastapi import FastAPI
from sqlalchemy.engine import Engine

from src.routers import short_link_router
from src.settings.database import Base
from src.settings.dependencies import get_settings, get_engine

logger = logging.getLogger(__name__)
app = FastAPI(title="Short Link")


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


app.include_router(short_link_router)


@app.on_event('startup')
def startup_event():
    settings = get_settings()
    settings.log_configuration(logger)
    engine: Engine = get_engine()
    Base.metadata.create_all(bind=engine)


import logging

from fastapi import FastAPI

from src.routers import short_link_router
from src.settings.dependencies import get_settings

logger = logging.getLogger(__name__)
app = FastAPI(title="Short Link")


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


app.include_router(short_link_router)

settings = get_settings()
settings.log_configuration(logger)

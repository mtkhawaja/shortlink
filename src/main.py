from fastapi import FastAPI

from src.routers import short_link_router

app = FastAPI(title="Short Link")


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


app.include_router(short_link_router)

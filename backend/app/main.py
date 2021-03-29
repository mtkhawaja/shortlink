from app.core.config import PROJECT_NAME, HOST_PORT, HOST_NAME, DEBUG
from app.api.api_v1.routers.shortlink import shortlink_router
from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.auth import auth_router
from app.core.auth import get_current_active_user
from app.db.session import SessionLocal
from starlette.requests import Request
from fastapi import FastAPI, Depends
from uvicorn import run

app = FastAPI(title=PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    """
    Welcome message for root route.
    """
    return {"message": f"Welcome to {PROJECT_NAME} !"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(shortlink_router, prefix="/api/v1", tags=["shortlink"])

if __name__ == "__main__":
    run("main:app", host=HOST_NAME, reload=DEBUG, port=HOST_PORT)

from datetime import datetime, timedelta
from pydantic import BaseModel


class ShortlinkBase(BaseModel):
    id: int
    original_url: str
    time_to_live: timedelta = timedelta(days=1)
    created_at: datetime = None
    expires_at: datetime = None


class ShortlinkOut(BaseModel):
    key_str: str
    expires_at: datetime

    class Config:
        orm_mode = True


class ShortlinkCreate(BaseModel):
    original_url: str
    time_to_live: timedelta = timedelta(days=1)

    class Config:
        orm_mode = True


class ShortlinkInverse(BaseModel):
    original_url: str
    time_to_live: timedelta
    created_at: datetime
    expires_at: datetime

    class Config:
        orm_mode = True

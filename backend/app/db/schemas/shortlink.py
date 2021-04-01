from datetime import datetime, timedelta
from pydantic import BaseModel


class ShortlinkCreate(BaseModel):
    original_url: str
    time_to_live: timedelta = timedelta(days=1)


class ShortlinkKey(BaseModel):
    key_str: str
    expires_at: datetime

    class Config:
        orm_mode = True


class ShortlinkMeta(BaseModel):
    original_url: str
    time_to_live: timedelta
    created_at: datetime
    expires_at: datetime

    class Config:
        orm_mode = True


class ShortlinkOriginal(BaseModel):
    original_url: str
    expires_at: datetime

    class Config:
        orm_mode = True

from pydantic import BaseModel


class ShortLinkCreate(BaseModel):
    original_url: str


class ShortLinkResponse(BaseModel):
    original_url: str
    key_string: str

    class Config:
        orm_mode = True


class ShortLink(BaseModel):
    id: int
    original_url: str
    key_string: str

    class Config:
        orm_mode = True

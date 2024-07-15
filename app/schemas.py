from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool
    clicks: int
    short_url: str

    class Config:
        orm_mode = True
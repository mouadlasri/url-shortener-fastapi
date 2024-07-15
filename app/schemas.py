from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class URLBase(BaseModel):
    target_url: str
    expires_at: Optional[datetime] = None

class URL(URLBase):
    is_active: bool
    clicks: int
    short_url: str
    created_at: datetime

    class Config:
        orm_mode = True
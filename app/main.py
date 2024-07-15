from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas, utils
from .database import get_db
from datetime import datetime

app = FastAPI()

@app.post("/shorten", response_model=schemas.URL)
async def create_url(url: schemas.URLBase, db: AsyncSession = Depends(get_db)):
    short_key = utils.create_random_key()
    
    db_url = models.URL(
        original_url=url.target_url,
        short_key=short_key,
        expires_at=url.expires_at
    )

    db.add(db_url)
    await db.commit()
    await db.refresh(db_url)

    return schemas.URL(
        target_url=db_url.original_url,
        is_active=True,
        clicks=db_url.clicks,
        short_url=f"{short_key}",
        created_at=db_url.created_at,
        expires_at=db_url.expires_at
    )

@app.get("/{short_key}")
async def forward_to_target_url(short_key: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.URL).where(models.URL.short_key == short_key))

    db_url = result.scalar_one_or_none()

    if db_url and db_url.is_active:
        if db_url.expires_at and db_url.expires_at < datetime.utcnow():
            db_url.is_active = False
            await db.commit()
            raise HTTPException(status_code=404, detail="URL has expired")
        db_url.clicks += 1
        await db.commit()
        return {"url": db_url.original_url}
    else:
        raise HTTPException(status_code=404, detail="URL not found")
    
@app.get("/stats/{short_key}", response_model=schemas.URL)
async def get_url_stats(short_key: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.URL).where(models.URL.short_key == short_key))

    db_url = result.scalar_one_or_none()
    if db_url:
        return db_url
    
    raise HTTPException(status_code=404, detail="URL not found")
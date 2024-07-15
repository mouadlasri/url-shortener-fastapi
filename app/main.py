from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas, utils
from .database import get_db

app = FastAPI()

@app.post("/shorten", response_model=schemas.URL)
async def create_url(url: schemas.URLBase, db: AsyncSession = Depends(get_db)):
    short_key = utils.create_random_key()
    db_url = models.URL(
        original_url=url.target_url,
        short_key=short_key,
    )
    db.add(db_url)
    await db.commit()
    await db.refresh(db_url)
    return schemas.URL(
        target_url=db_url.original_url,
        is_active=True,
        clicks=db_url.clicks,
        short_url=f"{short_key}"
    )

@app.get("/{short_key}")
async def forward_to_target_url(short_key: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.URL).where(models.URL.short_key == short_key))
    db_url = result.scalar_one_or_none()
    if db_url:
        db_url.clicks += 1
        await db.commit()
        return {"url": db_url.original_url}
    else:
        raise HTTPException(status_code=404, detail="URL not found")
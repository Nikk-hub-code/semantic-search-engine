from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.schemas.search import (
    SearchRequest
)

from app.services.search_service import (
    SearchService
)

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.post("/search")
def semantic_search(
    request: SearchRequest,
    db: Session = Depends(get_db)
):
    search_service = SearchService(db)

    results = search_service.semantic_search(
        query=request.query,
        limit=request.limit
    )

    return {
        "query": request.query,
        "results": results
    }
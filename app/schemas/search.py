from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    limit: int = 5


class SearchResult(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    content: str
    similarity: float
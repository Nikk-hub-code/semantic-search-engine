from sqlalchemy import text
from sqlalchemy.orm import Session

from app.services.embedding_service import (
    EmbeddingService
)


class SearchService:
    def __init__(self, db: Session):
        self.db = db

        self.embedding_service = (
            EmbeddingService()
        )

    def semantic_search(
        self,
        query: str,
        limit: int = 5
    ):
        """
        Perform semantic similarity search
        using pgvector cosine distance.
        """

        # Generate embedding for query
        query_embedding = (
            self.embedding_service
            .generate_embedding(query)
        )

        sql = text("""
            SELECT
                id,
                document_id,
                chunk_index,
                content,
                embedding <=> CAST(:embedding AS vector)
                    AS distance
            FROM chunks
            ORDER BY embedding <=> CAST(:embedding AS vector)
            LIMIT :limit
        """)

        result = self.db.execute(
            sql,
            {
                "embedding": str(query_embedding),
                "limit": limit
            }
        )

        rows = result.fetchall()

        results = []

        for row in rows:
            results.append(
                {
                    "id": row.id,
                    "document_id": row.document_id,
                    "chunk_index": row.chunk_index,
                    "content": row.content,
                    "similarity": 1 - row.distance
                }
            )

        return results
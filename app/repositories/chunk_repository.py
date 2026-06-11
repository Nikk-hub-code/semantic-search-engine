from sqlalchemy.orm import Session

from app.models.chunk import Chunk


class ChunkRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_chunk(
        self,
        document_id: int,
        chunk_index: int,
        content: str
    ) -> Chunk:
        chunk = Chunk(
            document_id=document_id,
            chunk_index=chunk_index,
            content=content
        )

        self.db.add(chunk)
        self.db.commit()
        self.db.refresh(chunk)

        return chunk

    def bulk_create_chunks(
        self,
        chunks_data: list[dict]
    ):
        chunks = [
            Chunk(**chunk_data)
            for chunk_data in chunks_data
        ]

        self.db.add_all(chunks)
        self.db.commit()

        return chunks

    def get_chunks_by_document(
        self,
        document_id: int
    ):
        return (
            self.db.query(Chunk)
            .filter(Chunk.document_id == document_id)
            .order_by(Chunk.chunk_index)
            .all()
        )

    def delete_chunks_by_document(
        self,
        document_id: int
    ) -> int:
        deleted_count = (
            self.db.query(Chunk)
            .filter(Chunk.document_id == document_id)
            .delete()
        )

        self.db.commit()

        return deleted_count
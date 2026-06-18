from pathlib import Path

from sqlalchemy.orm import Session

from app.repositories.source_repository import SourceRepository
from app.repositories.document_repository import DocumentRepository
from app.repositories.chunk_repository import ChunkRepository

from app.services.embedding_service import (
    EmbeddingService
)

from app.utils.text_splitter import split_text


class IngestionService:
    def __init__(self, db: Session):
        self.db = db

        self.source_repo = SourceRepository(db)
        self.document_repo = DocumentRepository(db)
        self.chunk_repo = ChunkRepository(db)

        self.embedding_service = (
            EmbeddingService()
        )

    def ingest_text_file(
        self,
        file_path: str,
        source_name: str | None = None,
        chunk_size: int = 500,
        chunk_overlap: int = 50
    ):
        """
        Ingest a text file into the database.

        Workflow:
        File
          ↓
        Read Text
          ↓
        Split Text
          ↓
        Generate Embeddings
          ↓
        Create Source
          ↓
        Create Document
          ↓
        Store Chunks + Embeddings
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        # Read file
        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:
            text = file.read()

        # Split text into chunks
        chunks = split_text(
            text=text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        # Create source
        source = self.source_repo.create_source(
            name=source_name or path.stem,
            source_type="txt",
            source_url=None
        )

        # Create document
        document = (
            self.document_repo.create_document(
                source_id=source.id,
                title=path.name,
                metadata_json={
                    "file_name": path.name,
                    "chunk_count": len(chunks)
                }
            )
        )

        # Generate embeddings + store chunks
        chunks_data = []

        for index, chunk_text in enumerate(chunks):

            embedding = (
                self.embedding_service
                .generate_embedding(chunk_text)
            )

            chunks_data.append(
                {
                    "document_id": document.id,
                    "chunk_index": index,
                    "content": chunk_text,
                    "embedding": embedding
                }
            )

        self.chunk_repo.bulk_create_chunks(
            chunks_data
        )

        return {
            "source_id": source.id,
            "document_id": document.id,
            "chunks_created": len(chunks)
        }
from app.core.database import SessionLocal

from app.repositories.document_repository import DocumentRepository
from app.repositories.chunk_repository import ChunkRepository


def main():
    db = SessionLocal()

    try:
        document_repo = DocumentRepository(db)
        chunk_repo = ChunkRepository(db)

        document = document_repo.get_document_by_id(3)

        if document is None:
            print("Document not found")
            return

        chunks = chunk_repo.get_chunks_by_document(
            document.id
        )

        print(f"Title: {document.title}")
        print(f"Total Chunks: {len(chunks)}")

        print("\nFirst 3 Chunks:\n")

        for chunk in chunks[:3]:
            print(
                f"Chunk {chunk.chunk_index}: "
                f"{chunk.content[:100]}..."
            )

    finally:
        db.close()


if __name__ == "__main__":
    main()
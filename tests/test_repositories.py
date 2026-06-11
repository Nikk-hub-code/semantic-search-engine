from app.core.database import SessionLocal

from app.repositories.source_repository import SourceRepository
from app.repositories.document_repository import DocumentRepository
from app.repositories.chunk_repository import ChunkRepository


def main():
    db = SessionLocal()

    try:
        source_repo = SourceRepository(db)
        document_repo = DocumentRepository(db)
        chunk_repo = ChunkRepository(db)

        # Create Source
        source = source_repo.create_source(
            name="Test Source",
            source_type="txt",
            source_url="https://example.com"
        )

        print(f"Source Created: {source.id}")

        # Create Document
        document = document_repo.create_document(
            source_id=source.id,
            title="Test Document",
            metadata_json={
                "author": "Kaushal",
                "category": "testing"
            }
        )

        print(f"Document Created: {document.id}")

        # Create Chunks
        chunk_1 = chunk_repo.create_chunk(
            document_id=document.id,
            chunk_index=0,
            content="This is the first chunk."
        )

        chunk_2 = chunk_repo.create_chunk(
            document_id=document.id,
            chunk_index=1,
            content="This is the second chunk."
        )

        print(f"Chunk Created: {chunk_1.id}")
        print(f"Chunk Created: {chunk_2.id}")

        # Fetch Chunks
        chunks = chunk_repo.get_chunks_by_document(
            document.id
        )

        print("\nRetrieved Chunks:")
        for chunk in chunks:
            print(
                f"Chunk {chunk.chunk_index}: "
                f"{chunk.content}"
            )

        print("\nRepository test completed successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
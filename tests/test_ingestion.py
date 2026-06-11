from app.core.database import SessionLocal
from app.services.ingestion_service import IngestionService


def main():
    db = SessionLocal()

    try:
        ingestion_service = IngestionService(db)

        result = ingestion_service.ingest_text_file(
            file_path="data/sample1.txt"
        )

        print(result)

    finally:
        db.close()


if __name__ == "__main__":
    main()
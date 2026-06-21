from app.core.database import SessionLocal

from app.services.search_service import (
    SearchService
)


def main():
    db = SessionLocal()

    try:
        search_service = SearchService(db)

        results = (
            search_service.semantic_search(
                query="What are embeddings?",
                limit=3
            )
        )

        print("\nSearch Results:\n")

        for result in results:
            print(
                f"Chunk Index: "
                f"{result['chunk_index']}"
            )

            print(
                f"Distance: "
                f"{result['distance']}"
            )

            print(
                f"Content: "
                f"{result['content'][:200]}"
            )

            print("-" * 50)

    finally:
        db.close()


if __name__ == "__main__":
    main()
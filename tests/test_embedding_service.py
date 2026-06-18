from app.services.embedding_service import (
    EmbeddingService
)


def main():
    embedding_service = EmbeddingService()

    text = (
        "Semantic search understands meaning."
    )

    embedding = (
        embedding_service.generate_embedding(
            text
        )
    )

    print(
        f"Embedding Dimensions: "
        f"{len(embedding)}"
    )

    print("\nFirst 10 Values:")
    print(embedding[:10])


if __name__ == "__main__":
    main()
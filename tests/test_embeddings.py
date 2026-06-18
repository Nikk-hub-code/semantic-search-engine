from sentence_transformers import SentenceTransformer


def main():
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    embedding = model.encode(
        "Hello world"
    )

    print(f"Embedding Dimensions: {len(embedding)}")

    print("\nFirst 10 Values:")
    print(embedding[:10])


if __name__ == "__main__":
    main()
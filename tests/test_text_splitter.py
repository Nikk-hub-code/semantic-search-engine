from app.utils.text_splitter import split_text

text = """
ABCDEFGHIJKLMNOPQRSTUVWXYZ
""" 

chunks = split_text(
    text=text,
    chunk_size=10,
    chunk_overlap=2
)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i}")
    print(chunk)
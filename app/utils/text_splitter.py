from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitterService:
    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_text(self, text: str):
        raw_chunks = self.splitter.split_text(text)

        chunks = []

        current_position = 0

        for index, chunk in enumerate(raw_chunks):
            start = text.find(chunk, current_position)
            end = start + len(chunk)

            chunks.append({
                "chunk_index": index,
                "content": chunk,
                "start_char": start,
                "end_char": end
            })

            current_position = end

        return chunks
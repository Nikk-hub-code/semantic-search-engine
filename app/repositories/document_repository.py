from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_document(
        self,
        source_id: int,
        title: str,
        metadata_json: dict | None = None
    ) -> Document:
        document = Document(
            source_id=source_id,
            title=title,
            metadata_json=metadata_json
        )

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def get_document_by_id(
        self,
        document_id: int
    ) -> Document | None:
        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def get_documents_by_source(
        self,
        source_id: int
    ):
        return (
            self.db.query(Document)
            .filter(Document.source_id == source_id)
            .all()
        )

    def delete_document(
        self,
        document_id: int
    ) -> bool:
        document = self.get_document_by_id(document_id)

        if not document:
            return False

        self.db.delete(document)
        self.db.commit()

        return True
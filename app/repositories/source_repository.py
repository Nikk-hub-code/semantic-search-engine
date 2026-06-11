from sqlalchemy.orm import Session

from app.models.source import Source


class SourceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_source(
        self,
        name: str,
        source_type: str,
        source_url: str | None = None
    ) -> Source:
        source = Source(
            name=name,
            source_type=source_type,
            source_url=source_url
        )

        self.db.add(source)
        self.db.commit()
        self.db.refresh(source)

        return source

    def get_source_by_id(
        self,
        source_id: int
    ) -> Source | None:
        return (
            self.db.query(Source)
            .filter(Source.id == source_id)
            .first()
        )

    def get_all_sources(self):
        return self.db.query(Source).all()

    def delete_source(
        self,
        source_id: int
    ) -> bool:
        source = self.get_source_by_id(source_id)

        if not source:
            return False

        self.db.delete(source)
        self.db.commit()

        return True
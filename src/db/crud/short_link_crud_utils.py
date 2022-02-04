from typing import Optional

from sqlalchemy.orm import Session

from src.db.models import ShortLinkModel


class ShortLinkCrudUtils:
    @staticmethod
    def get_short_link_by_id(db: Session, short_link_primary_key: int) -> Optional[ShortLinkModel]:
        return db.query(ShortLinkModel) \
            .filter(ShortLinkModel.id == short_link_primary_key) \
            .first()

    @staticmethod
    def create_short_link(db: Session, original_url: str) -> ShortLinkModel:
        db_short_link = ShortLinkModel(original_url=original_url)
        db.add(db_short_link)
        db.commit()
        db.refresh(db_short_link)
        return db_short_link

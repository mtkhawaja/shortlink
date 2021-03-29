from app.db.models.Shortlink import Shortlink
from app.db.schemas.shortlink import (
    ShortlinkCreate,
    ShortlinkOut,
    ShortlinkInverse,
)
from sqlalchemy.orm import Session


def get_original_url_and_meta_data(
    db: Session, key_str: str
) -> ShortlinkInverse:
    pk = Shortlink.decode(key_str)
    return db.query(Shortlink).filter(Shortlink.id == pk).first()


def create_shortlink(db: Session, shortlink: ShortlinkCreate) -> ShortlinkOut:
    db_shortlink = Shortlink(
        original_url=shortlink.original_url,
        time_to_live=shortlink.time_to_live,
    )
    db.add(db_shortlink)
    db.commit()
    db.refresh(db_shortlink)
    return db_shortlink

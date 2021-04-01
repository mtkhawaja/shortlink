from app.db.models.Shortlink import Shortlink
import app.db.schemas.shortlink as sl_schema
from sqlalchemy.orm import Session
from app.core.config import NOT_FOUND_REDIRECT


def get_original_url(db: Session, key_str: str) -> str:
    pk = Shortlink.decode(key_str)
    sl = db.query(Shortlink.original_url).filter(Shortlink.id == pk).first()
    return sl.original_url if sl else NOT_FOUND_REDIRECT


def get_original_url_and_expiry(
    db: Session, key_str: str
) -> sl_schema.ShortlinkOriginal:
    pk = Shortlink.decode(key_str)
    return db.query(Shortlink).filter(Shortlink.id == pk).first()


def get_original_url_and_meta_data(
    db: Session, key_str: str
) -> sl_schema.ShortlinkMeta:
    pk = Shortlink.decode(key_str)
    return db.query(Shortlink).filter(Shortlink.id == pk).first()


def create_shortlink(
    db: Session, shortlink: sl_schema.ShortlinkCreate
) -> sl_schema.ShortlinkKey:
    db_shortlink = Shortlink(
        original_url=shortlink.original_url,
        time_to_live=shortlink.time_to_live,
    )
    db.add(db_shortlink)
    db.commit()
    db.refresh(db_shortlink)
    return db_shortlink

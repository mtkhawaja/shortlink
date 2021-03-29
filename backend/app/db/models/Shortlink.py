from __future__ import annotations

from datetime import datetime, timedelta

from app.db.models.util.Decoder import Decoder
from app.db.models.util.Encoder import Encoder
from app.db.session import Base
from sqlalchemy import Column, DateTime, Integer, Interval, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func


class Shortlink(Base):
    __tablename__ = "shortlink"
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    time_to_live = Column(Interval, default=timedelta(days=1), nullable=False)

    @hybrid_property
    def expires_at(cls: Shortlink) -> datetime:
        return cls.created_at + cls.time_to_live

    @hybrid_property
    def key_str(cls: Shortlink) -> str:
        return Encoder.encode(cls.id)

    @staticmethod
    def decode(key_str: str) -> int:
        return Decoder.decode(key_str)

from sqlalchemy import Column, Integer, String

from src.settings.database import Base


class ShortLinkModel(Base):
    __tablename__ = "short_link"
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)

from typing import Optional

from sqlalchemy.orm import Session

from src.db.crud.short_link_crud_utils import ShortLinkCrudUtils
from src.db.models import ShortLinkModel
from src.db.schemas import short_link_schemas
from src.services.conversion_service import BaseConversionService


class ShortLinkService:

    @staticmethod
    def get_short_link(db: Session,
                       key_string: str,
                       conversion_service: BaseConversionService) -> Optional[short_link_schemas.ShortLinkResponse]:
        primary_key: int = conversion_service.decode(key_string)
        db_response: ShortLinkModel = ShortLinkCrudUtils.get_short_link_by_id(db, primary_key)
        if not db_response:
            return None
        return short_link_schemas.ShortLinkResponse(original_url=db_response.original_url, key_string=key_string)

    @staticmethod
    def create_short_link(db: Session,
                          base_link: str,
                          conversion_service: BaseConversionService) -> short_link_schemas.ShortLinkResponse:
        db_response: ShortLinkModel = ShortLinkCrudUtils.create_short_link(db, base_link)
        original_url: str = db_response.original_url
        key_string: str = conversion_service.encode(db_response.id)
        return short_link_schemas.ShortLinkResponse(original_url=original_url, key_string=key_string)

import logging
from datetime import datetime
from pyswagger.primitives import Datetime
from typing import Optional, Union, Dict, Any

from waitlist.utility.swagger.eve import ESIResponse

logger = logging.getLogger(__name__)


class CorporationInfo(ESIResponse):
    def __init__(self, expires: datetime, status_code: int, error: Optional[str],
                 data: Optional[Dict[str, Union[str, int, float, Datetime]]]) -> None:
        super().__init__(expires, status_code, error)
        self.data: Optional[Dict[str, Union[str, int, float, Datetime]]] = data

    def get_alliance_id(self) -> Optional[int]:
        return self.__get_data('alliance_id', None)

    def get_ceo_id(self) -> int:
        return self.data['ceo_id']

    def get_corporation_description(self) -> str:
        return self.__get_data('description', '')

    def get_corporation_name(self) -> str:
        return self.data['name']

    def get_creator_id(self) -> int:
        return self.data['creator_id']

    def get_member_count(self) -> int:
        return self.data['member_count']

    def get_tax_rate(self) -> float:
        return self.data['tax_rate']

    def get_ticker(self) -> str:
        return self.data['ticker']

    def get_url(self) -> str:
        return self.__get_data('url', '')

    def get_creation_date(self) -> Optional[datetime]:
        return self.data['date_founded'].v if 'date_founded' in self.data else None

    def __get_data(self, key: str, default: Any = None) -> Any:
        return self.data[key] if key in self.data else default

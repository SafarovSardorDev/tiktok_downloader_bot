from dataclasses import dataclass
from typing import List
from aiogram.types import LabeledPrice
from data import config


@dataclass
class Preproduct:
    """
    https://core.telegram.org/bots/api
    """
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
    provider_data: dict = None
    # photo_url: str = None
    # photo_size: str = None	
    # photo_width: str = None
    # photo_height: str = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False
    provider_token: str = config.PROVIDER_TOKEN

    def generate_invoice(self):
        return self.__dict__
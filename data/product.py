from aiogram import types
from aiogram.types import LabeledPrice
from utils.misc.pretarif import Preproduct


python_premium = Preproduct(
    title="Premium ta'rif",
    description="Premium ta'rifga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Premium ta'rif",
            amount=3638367
        )
    ],
    start_parameter="create_invoice_ds_praktikum",
    # photo_url=
    # photo_width=
    # photo_height=
    # photo_size=
    need_email=True,
    need_name=True,
    need_phone_number=True
)
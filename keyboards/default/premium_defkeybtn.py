from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

premium_tarif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Premium ta\'rif haqida')
        ]
    ],
    resize_keyboard=True
)
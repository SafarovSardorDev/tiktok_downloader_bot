from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from handlers.users import start

keybuttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='En'),
            KeyboardButton(text='Ru'),
            KeyboardButton(text='Uz')
        ]
    ],
    resize_keyboard=True
)

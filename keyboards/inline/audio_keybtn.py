from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

videos_audio = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🎵 Videoning musiqasi', callback_data='music')
        ]
    ]
)

premium_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔥 Premium', callback_data='premium')
        ]
    ]
)
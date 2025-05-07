from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer('Bu bot TikTokdagi videolarni watermarksiz yuklab beradi. Botga TikTok video linkini tashlang!!!')
    # await message.answer(message.text)
    # time_emoji = message.text
    # await message.answer(time_emoji)
    # print(message)

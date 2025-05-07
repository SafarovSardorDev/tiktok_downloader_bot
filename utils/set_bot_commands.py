from aiogram import types



async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("premium", "Premium ta'rifga o'tish"),
            types.BotCommand("all_users", "Hamma foydalanuvchilar ro'yxati admin uchun" ),
            types.BotCommand("count", "Foydalanuvchilar soni"),
        ]
    )

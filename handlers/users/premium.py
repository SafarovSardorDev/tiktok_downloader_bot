from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp,bot
from keyboards.default.premium_defkeybtn import premium_tarif
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.audio_keybtn import premium_inline
from data.product import python_premium
from data.config import ADMINS


@dp.message_handler(commands='premium')
async def bot_premium_btn(message: types.Message):
    await message.answer('Buttonni bosing', reply_markup=premium_tarif)


@dp.message_handler(text='Premium ta\'rif haqida')
async def bot_premium(message: types.Message):
    await message.answer("""
Oyiga atigi $2.99 evaziga Premium hisobini oling.

Premium hisob xususiyatlari:

🌅 Hikoyalar yuklab olish
🌠 Diqqatga sazovor joylarni yuklab oling
🚫 Reklama yo‘q
🚀 Tezroq yuklab olish
⚙️ Ustuvor qo‘llab-quvvatlash""", reply_markup=premium_inline)
    
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)



@dp.callback_query_handler(text="premium")
async def pre_invoice(call: types.CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_premium.generate_invoice(),
                           payload="premium")
    await call.answer()

@dp.pre_checkout_query_handler()
async def process_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    
    if pre_checkout_query.invoice_payload:
        await bot.send_message(chat_id=pre_checkout_query.from_user.id, text="Tabriklaymiz siz premium ta'rifga obuna bo'ldingiz!" )
    else:
        await bot.send_message(chat_id=pre_checkout_query.from_user.id, text="Uzr. Xatolik bo'ldi. Qaytadan urinib ko'ring")
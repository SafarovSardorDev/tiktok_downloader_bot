from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from tiktok import tiktok_video
from keyboards.inline.audio_keybtn import videos_audio, premium_inline
from aiogram.dispatcher import FSMContext

@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def send_video(message:types.Message, state: FSMContext):
    link = message.text
    data_video = tiktok_video(link=link)
    await state.update_data(
        {'link' : link}
    )
    await message.answer('⏳')
    try:
        await message.answer_video(data_video[0], caption='@testusersardor123bot - TikTokdagi barcha videolarni watermarksiz yuklab oling!', reply_markup=videos_audio)
    except Exception as e:
        await message.answer('Bu URL manzil orqali hech narsa topilmadi!😔')
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id+1)
    

@dp.callback_query_handler(text = 'music')
async def send_audio(call: types.CallbackQuery, state: FSMContext):
    data =await state.get_data()
    data_audio = tiktok_video(link=data.get('link'))[1]
    await call.message.answer_audio(data_audio)










from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.builtin import CommandStart
import wikipedia
import logging
from loader import dp, db, bot
from aiogram.types import ReplyKeyboardRemove
from data.config import ADMINS



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}! \nBu bot orqali TikTokdagi videolarni watermarksiz yuklab olishingiz mumkin. ⚡️")
    if await db.check_new_user(message.from_user.id):
        await message.answer("Siz botda ro'yxatdan o'tgansiz!")
    else:
        await db.add_user(message.from_user.id, message.from_user.username)
    

@dp.message_handler(commands='all_users', user_id=ADMINS)
async def bot_all_users(message: types.Message):
    try:
        excel_all_users= await db.all_users()
        # print(excel_all_users)
        for i in excel_all_users:
            # print(i)
        ##########for da aylantirib listdan qirqib olamiz
            text = f"""
            {i[0]} telegram id = {i[1]} username = {i[2]}
            """
            await message.answer(text)
    except Exception as e:
        await message.answer('Error')


@dp.message_handler(commands="count", user_id=ADMINS)
async def bot_add_user(message: types.Message):
    count_users= await db.count_users()
    await message.answer(count_users)

# import pandas as pd

# df = pd.read_excel('./excell_data/infos.xlsx')
# print(df)

# df = pd.read_excel('C:U/sers/Shaxzod/Desktop/py_darslik/BOTS/first_exercise/handlers/users/excell_data/infos.xlsx')
# print(df)


# # importing openpyxl module
# import openpyxl
 
# # Give the location of the file
# path = "C:\\Users\\Shaxzod\\Desktop\\first_exercise\\handlers\\users\\excell_data\\users_infos.xlsx"
# # C:\\Users\\Shaxzod\\Desktop\\py_darslik\\BOTS\\first_exercise\\handlers\\users\\excell_data\\users_infos.xlsx
 
# # workbook object is created
# wb_obj = openpyxl.load_workbook(path)
 
# sheet_obj = wb_obj.active
# print(sheet_obj["A1"].value)


# from openpyxl import load_workbook
# path = 'data.xlsx'
# wb = load_workbook(path)
# sheet = wb.active
# print(sheet["A1"])

# @dp.message_handler(commands='all_users', user_id=ADMINS)
# async def bot_all_users(message: types.Message):
#     sheet["C1"] = "safarov sardor"
#     wb.save(path)
#     with open(path, "r") as file:
#         await bot.send_document(chat_id=ADMINS, document=file)
    
        


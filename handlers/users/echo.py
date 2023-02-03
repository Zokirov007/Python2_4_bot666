from aiogram import types

from loader import dp
from filters.shaxsiy_uchun import shaxsiy

# Echo bot
@dp.message_handler(shaxsiy(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(text=f'{message.text}')

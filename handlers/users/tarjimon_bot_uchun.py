from aiogram import types
from googletrans import Translator
from loader import dp

yordamchi = Translator()

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    til = yordamchi.detect(text=message.text).lang
    if til =='uz':
        tarjima_qilish = yordamchi.translate(text=message.text,dest='en',src='uz').text
        await message.answer(text=tarjima_qilish)
    else:
        tarjima_qilish = yordamchi.translate(text=message.text, dest='uz', src='en').text
        await message.answer(text=tarjima_qilish)
    if til=='ru':
        tarjima_qilish = yordamchi.translate(text=message.text, dest='uz', src='ru').text
        await message.answer(text=tarjima_qilish)
    else:
        tarjima_qilish = yordamchi.translate(text=message.text, dest='ru', src='uz').text
        await message.answer(text=tarjima_qilish)
    if til=='en':
        tarjima_qilish = yordamchi.translate(text=message.text,dest='uz',src='en').text
        await message.answer(text=tarjima_qilish)
    else:
        tarjima_qilish = yordamchi.translate(text=message.text,dest='en',src='uz').text
        await message.answer(text=tarjima_qilish)
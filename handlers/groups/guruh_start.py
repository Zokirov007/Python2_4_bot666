from aiogram import types
from aiogram.types import ContentTypes

from loader import dp,bot
from filters.guruh_uchun import guruh

# Echo bot
@dp.message_handler(guruh(),commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text='Guruhga xush kelibsiz')

@dp.message_handler(guruh(),text='Salom')
async def bot_echo(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id,text=f'Assalomu alaykum guruhga xush kelibsiz')

@dp.message_handler(guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].full_name
    await message.reply(text=f'Guruhga xush kelibsiz {ism}')

@dp.message_handler(guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.full_name
    await message.reply(text=f'Guruhni tark etdi {ism}')

@dp.message_handler(guruh(),text='jinni')
async def bot_echo(message: types.Message):
    ism = message.from_user.full_name
    user_id = message.from_user.id
    guruh_id = message.chat.id
    message_id = message.message_id
    await bot.ban_chat_member(chat_id=guruh_id,message_id=message_id)
from aiogram import types
from aiogram.types import ContentTypes
from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text=f"{message}")

@dp.message_handler(text="Ichimliklar --- 🍻")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasm_uchun_ii/3'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Pepsi")

@dp.message_handler(text="Non maxsulotlari --- 🍞")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/2'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Patir nonlar")

@dp.message_handler(text="Shirinliklar --- 🥮")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/3'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Shirinliklar")

@dp.message_handler(text="Sut maxsulotlari --- 🥛")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/4'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Sut maxsulotlari")

@dp.message_handler(text="Gosht maxsulotlari --- 🍖")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/5'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Gosht maxsulotlari")

@dp.message_handler(text="Kostyumlar --- 👔")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/6'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Kostyumlar")

@dp.message_handler(text="Ko'ylaklar --- 👗")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/7'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Ko'ylaklar")

@dp.message_handler(text="Shimlar --- 👖")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/8'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Shimlar")

@dp.message_handler(text="Oyoq kiyimlar --- 👠")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/9'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Oyoq kiyimlar")

@dp.message_handler(text="Paypoqlar --- 🧦")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/10'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Paypoqlar")

@dp.message_handler(text="Soatlar --- ⌚")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/11'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Soatlar")

@dp.message_handler(text="Telefonlar --- 📱")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/12'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Telefonlar")

@dp.message_handler(text="Quloqchinlar --- 🎧")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/14'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Quloqchinlar")

@dp.message_handler(text="Skutirlar --- 🏍")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/13'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Skutirlar")

@dp.message_handler(text="Batareyalar --- 🚦")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/15'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Batareyalar")

@dp.message_handler(text="To'plar --- ⚽")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/16'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="To'plar")

@dp.message_handler(text="Fudbo'lkalar --- 👕")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/17'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Fudbo'lkalar")

@dp.message_handler(text="Kraso'fkalar --- 👟")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/18'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Kraso'fkalar")

@dp.message_handler(text="Gantellar --- 🏋️")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/19'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Gantellar")

# @dp.message_handler(text="Musho'klar")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm_manzili = ''
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Musho'klar")

@dp.message_handler(text="Bread products --- 🍞")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/20'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bread products")

@dp.message_handler(text="Drinks --- 🍻")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/21'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Drinks")

@dp.message_handler(text="Sweets --- 🥮")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/22'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Sweets")

@dp.message_handler(text="Dairy products --- 🥛")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/23'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Dairy products")

@dp.message_handler(text="Meat products --- 🍖")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/24'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Meat products")

@dp.message_handler(text="Costumes --- 👔")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/25'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Costumes")

@dp.message_handler(text="Dresses --- 👗")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/26'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Dresses")

@dp.message_handler(text="Pants --- 👖")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/27'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Pants")

@dp.message_handler(text="Shoes --- 👠")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/28'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Shoes")

@dp.message_handler(text="Socks --- 🧦")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/29'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Socks")

@dp.message_handler(text="Wristwatch --- ⌚")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/30'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Wristwatch")

@dp.message_handler(text="Phones --- 📱")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/31'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Phones")

@dp.message_handler(text="Tesla --- 🏍")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/32'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Tesla")

@dp.message_handler(text="Headphones --- 🎧")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/33'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Headphones")

@dp.message_handler(text="Batteries --- 🚦")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/15'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Batteries")

@dp.message_handler(text="Balls --- ⚽")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/34'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Balls")

@dp.message_handler(text="T-shirts --- 👕")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/35'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="T-shirts")

@dp.message_handler(text="Boots --- 👟")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/36'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Boots")

@dp.message_handler(text="Dumbbells --- 🏋️")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/37'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Dumbbells")

@dp.message_handler(text="Helmets --- 🚴")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/38'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Helmets --- 🚴")


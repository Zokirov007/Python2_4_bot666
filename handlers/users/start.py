from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from filters.shaxsiy_uchun import shaxsiy
from loader import dp, obyekt, bot
from keyboards.default.menu_uchun import menu_buttons,menu_buttons2
from keyboards.default.oziq_ovqat_uchun import oziq_ovqat_buttons,oziq_ovqat_buttons2
from keyboards.default.kiyimlar_uchun import kiyim_kechak_buttons,kiyim_kechak_buttons2
from keyboards.default.elektironika_uchun import elektironika_buttons,elektironika_buttons2
from keyboards.default.sport_uchun import sport_buttons,sport_buttons2
from keyboards.inline.tillar_uchun import tillar_buttons
@dp.message_handler(shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    try:
        obyekt.user_qoshish(ism,user_id,username,familya)
    except Exception:
        pass

    await message.answer(f"Salom, {message.from_user.full_name} !"
                         f"Tillardan birini tanlang !"
                         f"Choose one of the languages !",reply_markup=tillar_buttons)

@dp.message_handler(commands="reklama")
async def bot_start(message: types.Message):
    userlar = obyekt.select_barcha_foydalanuvchilar()
    print(userlar)

    for user in userlar:
        await bot.send_message(chat_id=user[4],text="Bu reklama !!!")
    await message.answer(f"Bo'limlardan birini tanlang",reply_markup=oziq_ovqat_buttons)

@dp.message_handler(text="Oziq ovqat --- 🍜")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang",reply_markup=oziq_ovqat_buttons)

@dp.message_handler(text="Ortga --- 📪")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang",reply_markup=menu_buttons)

@dp.message_handler(text="Kiyim kechaklar --- 👕")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang",reply_markup=kiyim_kechak_buttons)

@dp.message_handler(text="Elektironika --- 📡")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang", reply_markup=elektironika_buttons)

@dp.message_handler(text='Sports --- 🚴')
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang", reply_markup=sport_buttons)

@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Maxsulotni tanlang", reply_markup=menu_buttons)

menular = obyekt.selecet_XAMMA_menular()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    maxsulotlar = obyekt.select_maxsulotlar(tur=text)
    j = 0
    index = 0
    keys = []
    for menu in maxsulotlar:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f'{menu[1]}', )])
        else:
            keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
        j += 1
    keys.append([KeyboardButton(text='Ortga')])
    maxsulot_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Maxsulotni tanlang",reply_markup=maxsulot_buttons)


menular = obyekt.selecet_XAMMA_maxsulotlar()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    text = message.text
    print(text)
    maxsulot = obyekt.select_maxsulot(nomi=text)
    max_nomi = maxsulot[1]
    max_narxi = maxsulot[3]
    max_rasmi = maxsulot[2]
    max_text = maxsulot[4]
    user_id = message.from_user.id
    malumot = f"Nomi : {max_nomi}\n" \
              f"Narxi : {max_narxi}\n" \
              f"Malumot : {max_text}"

    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=malumot)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum {xabar.from_user.full_name} botga xush kelibsiz !",reply_markup=menu_buttons)

@dp.callback_query_handler(text="til2")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum {xabar.from_user.full_name} botga xush kelibsiz !",reply_markup=menu_buttons2)


@dp.message_handler(text="Elektironics --- 📡")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang", reply_markup=elektironika_buttons2)

@dp.message_handler(text="Exit --- 📪")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang", reply_markup=menu_buttons2)

@dp.message_handler(text="Foods --- 🍜")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang", reply_markup=oziq_ovqat_buttons2)

@dp.message_handler(text="Clothes --- 👕")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang", reply_markup=kiyim_kechak_buttons2)

@dp.message_handler(text="Sports --- 🚴")
async def bot_start(message: types.Message):
    await message.answer(f"Bo'limlardan birini tanlang", reply_markup=sport_buttons2)


@dp.message_handler(text="Sport --- 🚴‍")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/rasmlar_alfsi/4'
    await message.answer(text=message.text,reply_markup=sport_buttons)


@dp.callback_query_handler(text="www")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum {xabar.from_user.full_name} botga xush kelibsiz !",reply_markup=tillar_buttons)
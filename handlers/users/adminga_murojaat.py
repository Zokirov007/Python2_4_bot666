from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_uchun import tasdiqlash_buttons, menu_buttons, tasdiqlash_buttons2, menu_buttons2
from loader import dp,bot
from states.murojaat_uchun import Forma, Forma1


# Echo bot
@dp.message_handler(text="Adminga murojaat --- 💻")
async def bot_echo(message: types.Message):
    await message.answer(text="✍️Ismni kiriting...")
    await Forma.ism_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.ism_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"name":ism})
    await message.answer(f"✍️Familiyani kiriting...")
    await Forma.fam_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.fam_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    familya = message.text
    await state.update_data({"fam":familya})
    await message.answer(f"✍ Yoshni kiriting...")
    await Forma.yosh_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.yosh_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    yoshi = message.text
    await state.update_data({"yosh":yoshi})
    await message.answer(f"📞 Telefon no'meringizni kiriting kiriting...")
    await Forma.tel_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.tel_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    nomer = message.text
    await state.update_data({"tel":nomer})
    await message.answer(f"✍️Murojaatingizni kiriting...")
    await Forma.msg_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.msg_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    xabar = message.text
    await state.update_data({"text":xabar})
    user_id = message.from_user.id
    malumot = await state.get_data()
    ismi = malumot.get('name')
    familyasi = malumot.get('fam')
    yoshi = malumot.get('yosh')
    teli = malumot.get('tel')
    murojaati = malumot.get('text')

    text = f"Ism : {ismi}\n" \
           f"Fam : {familyasi}\n" \
           f"Yosh : {yoshi}\n" \
           f"Tel : {teli}\n" \
           f"Murojaat : {murojaati}"

    await bot.send_message(chat_id=user_id,text=text,reply_markup=tasdiqlash_buttons)
    await Forma.tasdiqlash_holati.set()

@dp.message_handler(state=Forma.tasdiqlash_holati,text="❌ Bekor qilish")
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer(f"Bekor qilish",reply_markup=menu_buttons)
    await state.finish()

@dp.message_handler(state=Forma.tasdiqlash_holati,text="✅ Tasdiqlash")
async def bot_start(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    user_id = message.from_user.id
    ismi = malumot.get('name')
    familyasi = malumot.get('fam')
    yoshi = malumot.get('yosh')
    teli = malumot.get('tel')
    murojaati = malumot.get('text')

    text = f"Ism : {ismi}\n" \
           f"Fam : {familyasi}\n" \
           f"Yosh : {yoshi}\n" \
           f"Tel : {teli}\n" \
           f"Murojaat : {murojaati}"
    await bot.send_message(chat_id='1301396842',text=text)
    await bot.send_message(chat_id=user_id,text="Adminga yuborildi",reply_markup=menu_buttons)
    await state.finish()

# --------------------------------------------------------------------------------------------------------

@dp.message_handler(text="Contact admin --- 💻")
async def bot_echo(message: types.Message):
    await message.answer(text="Enter name...")
    await Forma1.ism1_qabul_qilish_holati.set()

@dp.message_handler(state=Forma1.ism1_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"name1":ism})
    await message.answer(f"Enter last name...")
    await Forma1.fam1_qabul_qilish_holati.set()

@dp.message_handler(state=Forma1.fam1_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    familya = message.text
    await state.update_data({"fam1":familya})
    await message.answer(f"Enter age...")
    await Forma1.yosh1_qabul_qilish_holati.set()

@dp.message_handler(state=Forma1.yosh1_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    yoshi = message.text
    await state.update_data({"yosh1":yoshi})
    await message.answer(f"Enter your phone number...")
    await Forma1.tel1_qabul_qilish_holati.set()

@dp.message_handler(state=Forma1.tel1_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    nomer = message.text
    await state.update_data({"tel1":nomer})
    await message.answer(f"Enter your application...")
    await Forma1.msg1_qabul_qilish_holati.set()

@dp.message_handler(state=Forma1.msg1_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    xabar = message.text
    await state.update_data({"text1":xabar})
    user_id = message.from_user.id
    malumot = await state.get_data()
    ismi = malumot.get('name1')
    familyasi = malumot.get('fam1')
    yoshi = malumot.get('yosh1')
    teli = malumot.get('tel1')
    murojaati = malumot.get('text1')

    text = f"Name : {ismi}\n" \
           f"Family : {familyasi}\n" \
           f"Young : {yoshi}\n" \
           f"Telephone : {teli}\n" \
           f"Appeal : {murojaati}"

    await bot.send_message(chat_id=user_id,text=text,reply_markup=tasdiqlash_buttons2)
    await Forma1.tasdiqlash1_holati.set()

@dp.message_handler(state=Forma1.tasdiqlash1_holati,text="❌ Cancellation")
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer(f"Cancellation",reply_markup=menu_buttons2)
    await state.finish()

@dp.message_handler(state=Forma1.tasdiqlash1_holati,text="✅ Confirmation")
async def bot_start(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    user_id = message.from_user.id
    ismi = malumot.get('name1')
    familyasi = malumot.get('fam1')
    yoshi = malumot.get('yosh1')
    teli = malumot.get('tel1')
    murojaati = malumot.get('text1')

    text = f"Name : {ismi}\n" \
           f"Family : {familyasi}\n" \
           f"Young : {yoshi}\n" \
           f"Telephone : {teli}\n" \
           f"Appeal : {murojaati}"
    await bot.send_message(chat_id='1301396842',text=text)
    await bot.send_message(chat_id=user_id,text="Sent to admin",reply_markup=menu_buttons2)
    await state.finish()
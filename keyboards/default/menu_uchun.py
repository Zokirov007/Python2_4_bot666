

from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
from loader import obyekt

menular = obyekt.selecet_XAMMA_menular()
j = 0
index= 0
keys = []
for menu in menular:
    if j % 2 == 0 and j != 0:
        index += 1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f'{menu[1]}', )])
    else:
        keys[index].append(KeyboardButton(text=f'{menu[1]}', ))
    j +=1
keys.append([KeyboardButton(text='ADMINGA MUROJAATπ€')])
menu_buttons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)



tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="β Tasdiqlash"),
            KeyboardButton(text="β Bekor qilish")
        ]
    ],
    resize_keyboard=True
)



menu_buttons2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foods --- π"),
            KeyboardButton(text="Clothes --- π")
        ],
        [
            KeyboardButton(text="Elektironics --- π‘"),
            KeyboardButton(text="Sports --- π΄")
        ],
        [
            KeyboardButton(text="Contact admin --- π»")
        ],
        [
            KeyboardButton(text="Lokatsiya",request_location=True),
            KeyboardButton(text="Kontakt",request_contact=True)
        ]
    ],
    resize_keyboard=True
)

tasdiqlash_buttons2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="β Confirmation"),
            KeyboardButton(text="β Cancellation")
        ]
    ],
    resize_keyboard=True
)
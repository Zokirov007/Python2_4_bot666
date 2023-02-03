from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

kiyim_kechak_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kostyumlar --- 👔"),
            KeyboardButton(text="Ko'ylaklar --- 👗"),
            KeyboardButton(text="Shimlar --- 👖")
        ],
        [
            KeyboardButton(text="Oyoq kiyimlar --- 👠"),
            KeyboardButton(text="Paypoqlar --- 🧦")
        ],
        [
            KeyboardButton(text="Ortga --- 📪")
        ]
    ],
    resize_keyboard=True
)


kiyim_kechak_buttons2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Costumes --- 👔"),
            KeyboardButton(text="Dresses --- 👗"),
            KeyboardButton(text="Pants --- 👖")
        ],
        [
            KeyboardButton(text="Shoes --- 👠"),
            KeyboardButton(text="Socks --- 🧦")
        ],
        [
            KeyboardButton(text="Exit --- 📪")
        ]
    ],
    resize_keyboard=True
)
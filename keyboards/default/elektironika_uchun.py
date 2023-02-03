from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

elektironika_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Soatlar --- ⌚"),
            KeyboardButton(text="Telefonlar --- 📱"),
            KeyboardButton(text="Skutirlar --- 🏍")
        ],
        [
            KeyboardButton(text="Quloqchinlar --- 🎧"),
            KeyboardButton(text="Batareyalar --- 🚦")
        ],
        [
            KeyboardButton(text="Ortga --- 📪")
        ]
    ],
    resize_keyboard=True
)

elektironika_buttons2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Wristwatch --- ⌚"),
            KeyboardButton(text="Phones --- 📱"),
            KeyboardButton(text="Tesla --- 🏍")
        ],
        [
            KeyboardButton(text="Headphones --- 🎧"),
            KeyboardButton(text="Batteries --- 🚦")
        ],
        [
            KeyboardButton(text="Exit --- 📪")
        ]
    ],
    resize_keyboard=True
)
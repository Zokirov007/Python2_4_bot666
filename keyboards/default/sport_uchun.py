from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

sport_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="To'plar --- ⚽"),
            KeyboardButton(text="Fudbo'lkalar --- 👕"),
            KeyboardButton(text="Kraso'fkalar --- 👟")
        ],
        [
            KeyboardButton(text="Gantellar --- 🏋️‍"),
            KeyboardButton(text="Kaskalar 🚴‍")
        ],
        [
            KeyboardButton(text="Ortga --- 📪")
        ]
    ],
    resize_keyboard=True
)

sport_buttons2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Balls --- ⚽"),
            KeyboardButton(text="T-shirts --- 👕"),
            KeyboardButton(text="Boots --- 👟")
        ],
        [
            KeyboardButton(text="Dumbbells --- 🏋️"),
            KeyboardButton(text="Helmets --- 🚴")
        ],
        [
            KeyboardButton(text="Exit --- 📪")
        ]
    ],
    resize_keyboard=True
)
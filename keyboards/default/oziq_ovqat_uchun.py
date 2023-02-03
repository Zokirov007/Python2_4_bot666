from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

oziq_ovqat_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Non maxsulotlari --- 🍞"),
            KeyboardButton(text="Ichimliklar --- 🍻"),
            KeyboardButton(text="Shirinliklar --- 🥮")
        ],
        [
            KeyboardButton(text="Sut maxsulotlari --- 🥛"),
            KeyboardButton(text="Gosht maxsulotlari --- 🍖")
        ],
        [
            KeyboardButton(text="Ortga --- 📪")
        ]
    ],
    resize_keyboard=True
)

oziq_ovqat_buttons2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bread products --- 🍞"),
            KeyboardButton(text="Drinks --- 🍻"),
            KeyboardButton(text="Sweets --- 🥮")
        ],
        [
            KeyboardButton(text="Dairy products --- 🥛"),
            KeyboardButton(text="Meat products --- 🍖")
        ],
        [
            KeyboardButton(text="Exit --- 📪")
        ]
    ],
    resize_keyboard=True
)
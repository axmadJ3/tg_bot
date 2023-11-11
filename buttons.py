from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Uzbek Kitoblar'),
            KeyboardButton('Rus Kitoblar')
        ]
    ],
    resize_keyboard=True
)

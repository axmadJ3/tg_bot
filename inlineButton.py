from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Abdulla Qodriy', callback_data='1u'),
            InlineKeyboardButton(text='Oybek', callback_data='2u'),
            InlineKeyboardButton(text='Otkir Hoshimov', callback_data='3u')
        ]
    ]
)


inline_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пушкин', callback_data='1r'),
            InlineKeyboardButton(text='Толстой', callback_data='2r'),
            InlineKeyboardButton(text='Достоевский', callback_data='3r')
        ]
    ]
)


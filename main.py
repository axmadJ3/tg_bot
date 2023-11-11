from aiogram import executor
from aiogram.types import Message
from config import dp
from aiogram.types import CallbackQuery
from buttons import start_button
import inlineButton


@dp.message_handler(commands=['start'])
async def start_func(mes: Message):
    text = 'Botga xush kelibsiz'
    img = open('image/photo_2023-11-09_18-26-36.jpg', 'rb')
    await mes.answer_photo(img, caption=text, reply_markup=start_button)


@dp.message_handler(commands=['help'])
async def cmd_help(mes: Message):
    await mes.reply(f'Nma yordam kerak {mes.from_user.full_name}')


# uzbek kitoblar
@dp.message_handler(text='Uzbek Kitoblar')
async def inline_func(mes: Message):
    img = open('image/photo_2023-11-09_18-26-35.jpg', 'rb')
    await mes.answer_photo(img, caption='Yozuvchini tanlang', reply_markup=inlineButton.inline_uzb)


@dp.callback_query_handler(text='1u')
async def inline_text_1(call: CallbackQuery):
    kitoblar = open("kitob/O'tkan Kunlar (Abdulla Qodiriy).pdf", 'rb')
    await call.message.answer_document(kitoblar, reply_markup=start_button)


@dp.callback_query_handler(text='2u')
async def inline_text_2(call: CallbackQuery):
    kitoblar = open("kitob/Oybek. Bolalik (xotira-qissa).pdf", 'rb')
    await call.message.answer_document(kitoblar, reply_markup=start_button)


@dp.callback_query_handler(text='3u')
async def inline_text_3(call: CallbackQuery):
    kitoblar = open("kitob/O'tkir Hoshimov. Sevgi qissalari.pdf", 'rb')
    await call.message.answer_document(kitoblar, reply_markup=start_button)


# rus kitoblar
@dp.message_handler(text='Rus Kitoblar')
async def inline_func(mes: Message):
    img = open('image/img.png', 'rb')
    await mes.answer_photo(img, caption='Выберите писателя', reply_markup=inlineButton.inline_rus)


@dp.callback_query_handler(text='1r')
async def inline_text_1rus(call: CallbackQuery):
    kitoblar = open("kitob/avidreaders.ru__kapitanskaya-dochka.pdf", 'rb')
    await call.message.answer_document(kitoblar, reply_markup=start_button)


@dp.callback_query_handler(text='2r')
async def inline_text_2rus(call: CallbackQuery):
    kitoblar = open("kitob/avidreaders.ru__kavkazskiy-plennik3.pdf", 'rb')
    await call.message.answer_document(kitoblar, reply_markup=start_button)


@dp.callback_query_handler(text='3r')
async def inline_text_3rus(call: CallbackQuery):
    kitoblar = open("kitob/avidreaders.ru__prestuplenie-i-nakazanie-dr-izd.pdf", 'rb')
    await call.message.answer_document(kitoblar, reply_markup=start_button)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

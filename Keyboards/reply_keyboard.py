from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kbd = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог товаров')],
    [KeyboardButton(text='Варианты оплаты')],
    [KeyboardButton(text='О магазине')],
    [KeyboardButton(text='Помощь')]

])

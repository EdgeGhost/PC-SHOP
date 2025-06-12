from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kbd = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог товаров'),KeyboardButton(text='О магазине')],
    [KeyboardButton(text='История запросов'),KeyboardButton(text='Помощь')]
],resize_keyboard=True)


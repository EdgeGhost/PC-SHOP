from aiogram.utils.keyboard import InlineKeyboardBuilder

builder_ctg = InlineKeyboardBuilder()
builder_ctg.button(text='Процессоры', callback_data='CPU')
builder_ctg.button(text='Видеокарты', callback_data='GPU')
builder_ctg.button(text='Оперативная память', callback_data='RAM')
builder_ctg.button(text='Накопитель (HDD/SSD)', callback_data='ROM')
builder_ctg.button(text='Материнская плата', callback_data='Motherboard')
builder_ctg.button(text='Блок питание', callback_data='PSU')
builder_ctg.button(text='Система охлаждение', callback_data='FUN')
builder_ctg.button(text='Корпус', callback_data='Case')
builder_ctg.adjust(2)
inline_ctg = builder_ctg.as_markup()
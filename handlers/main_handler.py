from aiogram import Router, types,F
from aiogram.filters import CommandStart

from Keyboards.reply_keyboard import reply_kbd
from Keyboards.catalog_btns import inline_ctg

user_router = Router()

@user_router.message(CommandStart())
async def start(mess: types.Message):
    await mess.answer(text='Добро пожаловать в магазин электроники SynthwavePC🖥\n'
                           'Вы находитесь на главном меню🏠',reply_markup=reply_kbd, parse_mode='HTML')

@user_router.message(F.text == 'Каталог товаров')
async def catalog(mess: types.Message):
    await mess.answer(text='Выберите каталог', reply_markup=inline_ctg)

@user_router.message(F.text == 'О магазине')
async def about(mess: types.Message):
    await mess.answer(text='Магазин электроники SynthwavePC🖥 мы продаем качественные и оригинальные товары,быстрая и безопасная доставка')

@user_router.message(F.text == 'История запросов')
async def history(mess: types.Message):
    await mess.answer('В разработке')

@user_router.message(F.text == 'Помощь')
async def history(mess: types.Message):
    await mess.answer('В разработке')
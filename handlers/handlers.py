from aiogram import F,Router,types
from aiogram.filters import CommandStart

from Second_Bot.Keyboards.reply_keyboard import reply_kbd

user_router = Router()

@user_router.message(CommandStart())
async def start(mess: types.Message):
    await mess.answer(text='Добро пожаловать в магазин электроники SynthwavePC🖥\n'
                           'Вы находитесь на главном меню🏠',reply_markup=reply_kbd, parse_mode='HTML')

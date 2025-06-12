import os
import asyncio

from aiogram import Bot,Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers.main_handler import user_router

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
dp.include_router(user_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())

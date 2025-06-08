from aiogram.types import BotCommand

cmd_list = [
    BotCommand(command='main', description='Главное меню'),
    BotCommand(command='history', description='История запросов'),
    BotCommand(command='about', description='О разработчике'),
    BotCommand(command='help', description='Помощь')
]
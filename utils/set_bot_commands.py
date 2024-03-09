from aiogram import types, Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command='start', description='Запустить бота'),
        BotCommand(command='help', description='Нужна помощь?')

    ], BotCommandScopeDefault())
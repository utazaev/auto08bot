import logging
from aiogram import Bot

from data.config import admins


async def on_startup_notify(bot: Bot):
    for admin in admins:
        try:
            text = 'Бот запущен и готов к работе'
            await bot.send_message(chat_id=admin, text=text)

        except Exception as err:
            logging.exception(err)

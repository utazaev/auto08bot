import asyncio
from aiogram import F
from file_read.reader import sort_automag, sort_autoopen, sort_autoelectric
from loader import bot, dp
from utils import notify_admins, set_bot_commands
from handlers.users.start import get_start
from aiogram.filters import Command


dp.startup.register(notify_admins.on_startup_notify)
dp.message.register(get_start, Command(commands="start"))
dp.message.register(sort_automag, F.text == ('Автомагазины'))
#dp.message.register(show_inline_menu, F.text == ('Автомагазины'))
dp.message.register(sort_autoopen, F.text == ('Аварийное вскрытие'))
dp.message.register(sort_autoelectric, F.text == ('Автоэлектрики'))

async def main():
    await set_bot_commands.set_default_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())

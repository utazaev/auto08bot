from aiogram import types, Dispatcher, Bot
from aiogram.enums import ParseMode
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()



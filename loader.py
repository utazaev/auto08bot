from aiogram import types, Dispatcher, Bot
from aiogram.enums import ParseMode
from data import config
import time

time.sleep(5)
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()



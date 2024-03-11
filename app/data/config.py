import os  # библиотека функций для работы с операционной системой

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

admins = [225576382]

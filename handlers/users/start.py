from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Здравствуйте {message.from_user.full_name}! \n'
                         f'Это справочник телефонов организаций г. Элиста', reply_markup=register_keyboard)

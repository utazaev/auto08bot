from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Автомагазины'
        ),
        KeyboardButton(
            text='Автоэлектрики'
        ),
        KeyboardButton(
            text='Аварийное вскрытие'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Для продолжения нажмите кнопку ниже')
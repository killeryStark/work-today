from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

smart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🟢Да"),
            KeyboardButton(text="🔴Нет")
        ]
    ],
    resize_keyboard=True
)

eisenhower_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🟢Да"),
            KeyboardButton(text="🔴Нет")
        ]
    ],
    resize_keyboard=True
)
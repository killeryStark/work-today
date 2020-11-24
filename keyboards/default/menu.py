from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕Добавить задачу"),
            KeyboardButton(text="🧾Добавить расходы")
        ],
        [
            KeyboardButton(text="📬Входящие"),
            KeyboardButton(text="☀️Сегодня")
        ],
        [
            KeyboardButton(text="📈Статистика"),
            KeyboardButton(text="⚙️Настройки")
        ]
    ],
    resize_keyboard=True
)
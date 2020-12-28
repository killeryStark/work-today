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
            KeyboardButton(text="📕Журнал"),
            KeyboardButton(text="💾Сохраненое")
        ],
        [
            KeyboardButton(text="➕Добавить категорию")
        ],
        [
            KeyboardButton(text="🗂Категории")
        ],
        [
            KeyboardButton(text="📈Статистика"),
            KeyboardButton(text="⚙️Настройки")
        ],
        [
            KeyboardButton(text="🈸Переводчик")
        ],
        [
            KeyboardButton(text="📜Информация"),
            KeyboardButton(text="💎Донейт")
        ]
    ],
    resize_keyboard=True
)
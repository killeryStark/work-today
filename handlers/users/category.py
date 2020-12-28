from aiogram import types

from keyboards.inline import task_button
from loader import dp, db, tasks


@dp.message_handler(text="🗂Категории")
async def add_task(message: types.Message):
    await message.answer("<b>Выберите категорию</b>\n"
                         "______________", reply_markup="")

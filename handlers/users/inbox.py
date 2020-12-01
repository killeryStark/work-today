from aiogram import types

from keyboards.inline import task_button
from loader import dp, db, tasks


@dp.message_handler(text="📬Входящие")
async def add_task(message: types.Message):
    id = message.from_user.id
    post = db.check_task_inbox(int(id))
    await message.answer("______________\n"
                         "<b>ВХОДЯЩИЕ</b>\n"
                         "______________")
    for msg in post:
        if msg["today"] == 0:
            msg = tasks.format_task(msg)
            await message.answer(msg, reply_markup=task_button)
        else: pass
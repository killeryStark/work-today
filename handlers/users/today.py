from aiogram import types

from keyboards.inline import task_button
from keyboards.inline.inline_task_button import today_button
from loader import dp, db, tasks


@dp.message_handler(text="☀️Сегодня")
async def add_task(message: types.Message):
    id = message.from_user.id
    post = db.check_task_today(int(id))
    await message.answer("<b>СЕГОДНЯ</b>\n"
                         "______________")
    for msg in post:
        if msg["today"] == 1:
            msg = tasks.format_task(msg)
            await message.answer(msg, reply_markup=today_button)
        else: pass
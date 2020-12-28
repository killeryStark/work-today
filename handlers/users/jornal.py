from aiogram import types

from keyboards.inline import task_button
from loader import dp, db, tasks


@dp.message_handler(text="📕Журнал")
async def jornal(message: types.Message):
    id = message.from_user.id
    post = db.check_jornal(int(id))
    await message.answer("<b>Журнал</b>\n"
                         "______________")
    for msg in post:
        msg = tasks.format_task(msg)
        await message.answer(msg)

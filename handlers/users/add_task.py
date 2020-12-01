from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import task_button
from loader import dp, db, tasks
from states import AddTaskStates


@dp.message_handler(text="➕Добавить задачу")
async def add_task(message: types.Message):
    await message.answer("Напишите задачу")
    await AddTaskStates.add.set()


@dp.message_handler(state=AddTaskStates.add)
async def task_answer(message: types.Message, state: FSMContext):
    post = {
        "user_id": message.from_user.id,
        "task": message.text,
        "notes": "",
        "tags": "",
        "date_create": tasks.get_now_formatted(),
        "remind": "",
        "category": "Входящие",
        "today": 0,
        "done": 0,
        "done_time": ""
    }
    db.add_task(post)
    msg = tasks.format_task(post)
    await state.finish()
    await message.answer(msg, reply_markup=task_button)



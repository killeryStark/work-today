from datetime import datetime

import pymongo
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, tasks
from states import AddTaskStates
from utils.task import Tasks


@dp.message_handler(text = "➕Добавить задачу")
async def add_task(message: types.Message):
    await message.answer("Напишите задачу")
    await AddTaskStates.add.set()

@dp.message_handler(state=AddTaskStates.add)
async def task_answer(message: types.Message):
    post={
        "user_id": message.from_user.id,
        "task": message.text,
        "tags": "",
        "date_create": datetime.utcnow(),
        "remind": "",
        "category": "Входящие",
        "tooday": 0
    }
    db.add_task(post)
    msg = tasks.format_task(post)
    await message.answer(msg)
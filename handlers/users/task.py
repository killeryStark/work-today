from time import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import today_button, eisenhower_button, task_button
from loader import dp, tasks, db, bot
from states import NotesStates, RemindStates


@dp.callback_query_handler(text="today")
async def add_tooday(call: CallbackQuery):
    await call.answer(cache_time=5)
    text = call.message.text
    id = tasks.find_task(text)
    param = 1
    db.edit_today(id, param)
    post = db.find_task(id)
    msg = tasks.format_task(post)
    await call.message.edit_text(msg, reply_markup=today_button)


@dp.callback_query_handler(text="not_today")
async def add_tooday(call: CallbackQuery):
    await call.answer(cache_time=5)
    text = call.message.text
    id = tasks.find_task(text)
    param = 0
    db.edit_today(id, param)
    post = db.find_task(id)
    msg = tasks.format_task(post)
    await call.message.edit_text(msg, reply_markup=task_button)


@dp.callback_query_handler(text="eisenhower")
async def eisenhower_keyboard(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_reply_markup(reply_markup=eisenhower_button)


@dp.callback_query_handler(text="eisenhower1")
async def eisenhower_keyboard(call: CallbackQuery):
    await call.answer(cache_time=5)
    text = call.message.text
    id = tasks.find_task(text)
    tags = "Важное Срочное"
    db.edit_tags(id, tags)
    post = db.find_task(id)
    if post['today'] == 1:
        keyboard = today_button
    else:
        keyboard = task_button
    msg = tasks.format_task(post)
    await call.message.edit_text(msg, reply_markup=keyboard)


@dp.callback_query_handler(text="eisenhower2")
async def eisenhower_keyboard(call: CallbackQuery):
    await call.answer(cache_time=5)
    text = call.message.text
    id = tasks.find_task(text)
    tags = "Важное Несрочное"
    db.edit_tags(id, tags)
    post = db.find_task(id)
    if post['today'] == 1:
        keyboard = today_button
    else:
        keyboard = task_button
    msg = tasks.format_task(post)
    await call.message.edit_text(msg, reply_markup=keyboard)


@dp.callback_query_handler(text="eisenhower3")
async def eisenhower_keyboard(call: CallbackQuery):
    await call.answer(cache_time=5)
    text = call.message.text
    id = tasks.find_task(text)
    tags = "Неважное Срочное"
    db.edit_tags(id, tags)
    post = db.find_task(id)
    if post['today'] == 1:
        keyboard = today_button
    else:
        keyboard = task_button
    msg = tasks.format_task(post)
    await call.message.edit_text(msg, reply_markup=keyboard)


@dp.callback_query_handler(text="eisenhower4")
async def eisenhower_keyboard(call: CallbackQuery):
    await call.answer(cache_time=5)
    text = call.message.text
    id = tasks.find_task(text)
    tags = "Неважное Несрочное"
    db.edit_tags(id, tags)
    post = db.find_task(id)
    if post['today'] == 1:
        keyboard = today_button
    else:
        keyboard = task_button
    msg = tasks.format_task(post)
    await call.message.edit_text(msg, reply_markup=keyboard)


@dp.callback_query_handler(text="done")
async def eisenhower_keyboard(call: CallbackQuery):
    await call.answer(cache_time=5)
    text = call.message.text
    id = tasks.find_task(text)
    time = tasks.get_now_formatted()
    db.edit_done(id, time)
    post = db.find_task(id)

    await call.message.delete()


@dp.callback_query_handler(text="notes")
async def notes(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer("Напишите заметку:")
    text = call.message.text
    id = tasks.find_task(text)
    await state.update_data(id=id)
    await NotesStates.add.set()


@dp.message_handler(state=NotesStates.add)
async def ad_notes(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get("id")
    notes = message.text
    db.add_notes(id, notes)
    task = db.find_task(id)
    msg = tasks.format_task(task)
    if task['today'] == 1:
        keyboard = today_button
    else:
        keyboard = task_button
    await message.answer(msg, reply_markup=keyboard)
    await state.finish()


@dp.callback_query_handler(text="remind")
async def remind(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer("Добавить напоминание"
                              "Введите в формате: 2020-11-28 03:01")
    text = call.message.text
    id = tasks.find_task(text)
    await state.update_data(id=id)
    await RemindStates.add.set()


@dp.message_handler(state=RemindStates.add)
async def add_remind(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get("id")
    remind = message.text + ":00"
    db.add_remind(id, remind)
    task = db.find_task(id)
    msg = tasks.format_task(task)
    if task['today'] == 1:
        keyboard = today_button
    else:
        keyboard = task_button
    await message.answer(msg, reply_markup=keyboard)
    await state.finish()


def check_remind():
    while True:
        users = db.load_users()
        for u in users:
            id = users["_id"]
            tasks = db.find_task(id)
            for t in tasks:
                time_task = tasks.get_now_formatted()
                if t["remind"] >= time_task:
                    task = tasks.format_task(t)
                    if task['today'] == 1:
                        keyboard = today_button
                    else:
                        keyboard = task_button
                    bot.send_message(id, tasks, reply_markup=keyboard)
                    time.sleep(30)

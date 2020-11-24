import pymongo
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu, smart, eisenhower_keyboard
from loader import dp, db
from states import StartSettings


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"🖖Привет, {message.from_user.full_name}!\n"
                         f"👨‍💻Я твой виртуальный ассистент в телеграме!\n"
                         "В мои задачи входит:\n"
                         "  1. Учет твоих финансов💸\n"
                         "  2. Ведение твоих задач✅\n"
                         "  3. Сохранение материалов💾\n")
    await message.answer("Давай меня настроим⚙")
    await message.answer("Использовать подсказки SMART?\n"
                         "Подробнее: https://ru.wikipedia.org/wiki/SMART", reply_markup=smart)
    await StartSettings.q1.set()

@dp.message_handler(state=StartSettings.q1)
async def eisenhower(message: types.Message, state=FSMContext):
    smart_answer = message.text
    status = True
    while status:
        if smart_answer == "🟢Да":
            smart_answer=1
            status = False
        elif smart_answer == "🔴Нет":
            smart_answer=0
            status = False
        else:
            await message.answer("Нажмите на одну из кнопок выбора")
            return

    await state.update_data(answer1=smart_answer)
    await message.answer("Включить теги матрицы Эйзенхауэра?", reply_markup=eisenhower_keyboard)
    await StartSettings.q2.set()

@dp.message_handler(state=StartSettings.q2)
async def eisenhower_answer(message: types.Message, state=FSMContext):
    data =await state.get_data()
    smart = data.get("answer1")
    eisenhower = message.text
    status = True
    while status:
        if eisenhower == "🟢Да":
            eisenhower=1
            status = False
        elif eisenhower == "🔴Нет":
            eisenhower = 0
            status = False
        else:
            await message.answer("Нажмите на одну из кнопок выбора")
            return

    post = {
        "_id": message.from_user.id,
        "name": message.from_user.full_name,
        "smart": smart,
        "eisenhower": eisenhower
    }

    try:
        db.add_user(post)
        await message.answer("Регистрация Успешна", reply_markup=menu)
    except pymongo.errors.DuplicateKeyError:
        await message.answer("Вы уже зарегистрированны", reply_markup=menu)
    await state.finish()


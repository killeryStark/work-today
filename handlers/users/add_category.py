from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import task_button
from loader import dp, db, tasks
from states import AddCategoryStates


@dp.message_handler(text="➕Добавить категорию")
async def add_category(message: types.Message):
    await message.answer("Напишите Название категории")
    await AddCategoryStates.add.set()

@dp.message_handler(state=AddCategoryStates.add)
async def task_answer(message: types.Message, state: FSMContext):
    id = message.from_user.id
    category = message.text
    db.add_category(int(id), category)
    await message.answer(f'Добавлена категория "{category}"')
    await state.finish()
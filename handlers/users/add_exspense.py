from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.errors import exceptions
from loader import dp, tasks, db
from states import AddExpenseStates


@dp.message_handler(text="🧾Добавить расходы")
async def add_task(message: types.Message):
    await message.answer("Добавить расход: \n Напимер: 1250 такси")
    await AddExpenseStates.add.set()


@dp.message_handler(state=AddExpenseStates)
async def add_expense(message: types.Message, state: FSMContext):
    """Добавляет новый расход"""
    try:
        id = message.from_user.id
        parsed_message = tasks._parse_message(message.text)
        categories = db.load_categories()
        categories_result = tasks.fill_aliases(categories)
        category = tasks.get_category(
            parsed_message.category_text, categories_result)
        created = tasks.get_now_formatted()
        db.add_expenses(id, parsed_message.amount, created, category.codename, category.is_base_expense)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    date = created[:-8]
    expenses = db.check_expenses(id)
    sum = 0
    expense_base = 0
    for expense in expenses:
        if date in expense["created"]:
            sum += int(expense["amount"])
        if expense["base"]:
            expense_base += int(expense["amount"])
        else:
            pass
    limit = db.find_user(id)
    await message.answer(f"Добавлены траты {parsed_message.amount} руб на {category.name}.\n\n"
                         f"Расходы сегодня:\n"
                         f"всего — {sum} руб.\n"
                         f"базовые — {expense_base} руб. из {limit['limit']} руб.\n\n")
    await state.finish()

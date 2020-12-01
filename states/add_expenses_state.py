from aiogram.dispatcher.filters.state import StatesGroup, State


class AddExpenseStates(StatesGroup):
    add = State()
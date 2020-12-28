from aiogram.dispatcher.filters.state import StatesGroup, State


class AddCategoryStates(StatesGroup):
    add = State()
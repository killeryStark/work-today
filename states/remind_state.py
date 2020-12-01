from aiogram.dispatcher.filters.state import StatesGroup, State


class RemindStates(StatesGroup):
    add = State()
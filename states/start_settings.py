from aiogram.dispatcher.filters.state import StatesGroup, State


class StartSettings(StatesGroup):
    q1 = State()
    q2 = State()
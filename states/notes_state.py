from aiogram.dispatcher.filters.state import StatesGroup, State


class NotesStates(StatesGroup):
    add = State()
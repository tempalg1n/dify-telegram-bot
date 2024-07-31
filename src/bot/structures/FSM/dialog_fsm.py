from aiogram.fsm.state import StatesGroup, State


class StartSG(StatesGroup):
    greeting = State()

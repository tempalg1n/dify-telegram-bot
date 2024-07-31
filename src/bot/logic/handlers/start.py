"""This file represents a start logic."""


from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode

from src.bot.structures.FSM.dialog_fsm import DialogSG

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: types.Message, dialog_manager: DialogManager):
    """Start command handler."""
    await dialog_manager.start(DialogSG.greeting, mode=StartMode.RESET_STACK)

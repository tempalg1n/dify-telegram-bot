"""This file represents a start logic."""


from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove
from aiogram_dialog import DialogManager, StartMode

from src.bot.structures.FSM.dialog_fsm import StartSG, AssistantSG

commands_handler_router = Router(name='start')


@commands_handler_router.message(CommandStart())
async def start_handler(message: types.Message, dialog_manager: DialogManager):
    """Start command handler."""
    await message.answer('💡', reply_markup=ReplyKeyboardRemove())
    await dialog_manager.start(StartSG.greeting, mode=StartMode.NORMAL)


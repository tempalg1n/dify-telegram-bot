"""This file represents a start logic."""

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from fluentogram import TranslatorRunner

from src.bot.structures.FSM.base_fsm import Conversation

commands_handler_router = Router(name='commands')


@commands_handler_router.message(CommandStart())
async def start_handler(message: types.Message, i18n: TranslatorRunner):
    """Start command handler."""
    await message.answer(
        i18n.greeting(
            username=message.from_user.full_name
        ),
        reply_markup=ReplyKeyboardRemove()
    )


@commands_handler_router.message(Command('new_chat'))
async def new_chat_handler(message: types.Message, i18n: TranslatorRunner, state: FSMContext):
    """New chat command handler."""
    await message.answer(i18n.new.chat(), reply_markup=ReplyKeyboardRemove())
    await state.clear()
    await state.set_state(Conversation.pending)

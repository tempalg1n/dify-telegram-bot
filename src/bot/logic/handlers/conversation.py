"""This file represents a start logic."""
import asyncio

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from fluentogram import TranslatorRunner

from src.bot.logic.tasks.dify import get_answer
from src.bot.structures.FSM.base_fsm import Conversation

conversation_handler_router = Router(name='conversation')


@conversation_handler_router.message(Conversation.pending)
async def user_input_handler(message: types.Message, i18n: TranslatorRunner, state: FSMContext):
    """User input handler."""
    waiting_message: types.Message = await message.answer(
        i18n.waiting(),
        reply_markup=ReplyKeyboardRemove()
    )
    state_data: dict = await state.get_data()
    conversation_id: str = state_data.get('conversation_id')
    asyncio.create_task(get_answer(
        user_input=message.text,
        user_id=message.from_user.id,
        conversation_id=conversation_id,
        wait_message_id=waiting_message.message_id,
        state=state
    ))


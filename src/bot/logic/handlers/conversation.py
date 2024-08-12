"""This file represents a start logic."""
import asyncio

from aiogram import Router, types, Bot
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from fluentogram import TranslatorRunner

from src.bot.logic.tasks.dify import get_answer
from src.bot.structures.FSM.base_fsm import Conversation

conversation_handler_router = Router(name='conversation')


@conversation_handler_router.message(Conversation.pending)
async def user_input_handler(
        message: types.Message,
        state: FSMContext,
        bot: Bot
):
    """User input handler."""
    state_data: dict = await state.get_data()
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    conversation_id: str = state_data.get('conversation_id')
    asyncio.create_task(get_answer(
        user_input=message.text,
        user_id=message.from_user.id,
        conversation_id=conversation_id,
        state=state
    ))


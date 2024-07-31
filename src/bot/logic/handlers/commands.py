"""This file represents a start logic."""

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove
from fluentogram import TranslatorRunner

commands_handler_router = Router(name='commands')


@commands_handler_router.message(CommandStart())
async def start_handler(message: types.Message, i18n: TranslatorRunner):  # TODO: add fluentogram to transfer data
    """Start command handler."""
    await message.answer(i18n.greeting(), reply_markup=ReplyKeyboardRemove())

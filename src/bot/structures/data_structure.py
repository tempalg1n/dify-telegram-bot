"""Data Structures.

This file contains TypedDict structure to store data which will
transfer throw Dispatcher->Middlewares->Handlers.
"""

from typing import TypedDict

from aiogram import Bot
from fluentogram import TranslatorRunner, TranslatorHub

from src.dify.client import Dify


class TransferData(TypedDict):
    """Common transfer data."""

    bot: Bot
    i18n: TranslatorRunner
    _translator_hub: TranslatorHub
    dify: Dify

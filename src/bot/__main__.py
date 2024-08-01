"""This file represent startup bot logic."""
import asyncio
import logging

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from sulguk import AiogramSulgukMiddleware

from src.bot.dispatcher import get_dispatcher
from src.bot.middlewares import middlewares
from src.bot.middlewares.i18n_md import I18nMiddleware, make_i18n_middleware
from src.bot.structures.data_structure import TransferData
from src.bot.utils.translation.fluentogram import create_translator_hub
from src.configuration import conf
from src.dify.client import Dify

COMMANDS = {
    'new_chat': 'Start new chat',
}


def register_middlewares(dp) -> None:
    i18n_middleware: I18nMiddleware = make_i18n_middleware()
    for observer in dp.observers.values():
        observer.outer_middleware(i18n_middleware)
        for middleware in middlewares:
            observer.outer_middleware(middleware)


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command,
    description in COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)


async def start_bot():
    """This function will start bot with polling mode."""
    bot = Bot(token=conf.bot.token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = get_dispatcher()
    translator_hub: TranslatorHub = create_translator_hub()
    await set_main_menu(bot)

    bot.session.middleware(AiogramSulgukMiddleware())
    setup_dialogs(dp)
    register_middlewares(dp)

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        **TransferData(
            _translator_hub=translator_hub,
            dify=Dify(conf.dify.api_key)
        ),
    )


if __name__ == '__main__':
    logging.basicConfig(level=conf.logging_level)
    asyncio.run(start_bot())

"""This file represent startup bot logic."""
import asyncio
import logging

from aiogram import Bot
from aiogram.types import BotCommand
from aiogram_dialog import setup_dialogs

from sulguk import AiogramSulgukMiddleware

from src.bot.dispatcher import get_dispatcher
from src.bot.middlewares import middlewares
from src.configuration import conf

COMMANDS = {
    'new_chat': 'Start new chat',
}


def register_middlewares(dp) -> None:
    for observer in dp.observers.values():
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
    bot = Bot(token=conf.bot.token)
    dp = get_dispatcher()
    await set_main_menu(bot)

    bot.session.middleware(AiogramSulgukMiddleware())
    setup_dialogs(dp)
    register_middlewares(dp)

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
    )


if __name__ == '__main__':
    logging.basicConfig(level=conf.logging_level)
    asyncio.run(start_bot())

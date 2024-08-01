"""This package is used for a bot logic implementation."""
from src.bot.logic.dialogs.start.dialog import start_dialog
from src.bot.logic.handlers.commands import commands_handler_router
from src.bot.logic.handlers.conversation import conversation_handler_router

routers = (
    commands_handler_router,
    conversation_handler_router,
    start_dialog,
)

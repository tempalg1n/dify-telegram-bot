from aiogram import Router
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button, Cancel

from src.bot.logic.dialogs.start.getter import get_data
from src.bot.structures.FSM.dialog_fsm import StartSG

from src.bot.utils.translation.i18n_format import I18NFormat

start_dialog = Dialog(
    Window(
        I18NFormat("Hello-user"),
        getter=get_data,
        state=StartSG.greeting,
    )
)

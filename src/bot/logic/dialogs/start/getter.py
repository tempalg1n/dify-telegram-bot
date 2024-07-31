from aiogram_dialog import DialogManager


async def get_data(dialog_manager: DialogManager, **kwargs):
    name = dialog_manager.event.from_user.full_name
    return {
        "username": name,
    }

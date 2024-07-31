from typing import Dict, List

from aiogram.types import InlineKeyboardButton
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import SwitchInlineQuery


class SwitchInlineQueryCurrentChat(SwitchInlineQuery):
    async def _render_keyboard(
        self,
        data: Dict,
        manager: DialogManager,
    ) -> List[List[InlineKeyboardButton]]:
        return [
            [
                InlineKeyboardButton(
                    text=await self.text.render_text(data, manager),
                    switch_inline_query_current_chat=await self.switch_inline.render_text(
                        data,
                        manager,
                    ),
                ),
            ],
        ]

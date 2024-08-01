from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from sulguk import SULGUK_PARSE_MODE, AiogramSulgukMiddleware

from src.configuration import conf
from src.dify.client import Dify


async def get_answer(
        user_input: str,
        user_id: int,
        wait_message_id: int,
        state: FSMContext,
        conversation_id: str = None,
):
    bot = Bot(conf.bot.token, default=DefaultBotProperties(parse_mode=SULGUK_PARSE_MODE))
    bot.session.middleware(AiogramSulgukMiddleware())
    dify: Dify = Dify(conf.dify.api_key)
    response = await dify.send_chat_message(user_input, user_id, conversation_id)
    if response[0] == 200:
        answer = response[1]['answer']
    else:
        answer = f'An error has occurred during conversation. Try again!'
    async with bot:
        await bot.delete_message(user_id, wait_message_id)
        await bot.send_message(user_id, answer)
        await state.set_data(
            {"conversation_id": conversation_id if conversation_id else response[1]['conversation_id']}
        )


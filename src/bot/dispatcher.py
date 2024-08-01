"""This file contains build dispatcher logic."""
import os

from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy

from .logic import routers


def get_dispatcher(
        storage: BaseStorage = MemoryStorage(),
        fsm_strategy: FSMStrategy | None = FSMStrategy.CHAT,
        event_isolation: BaseEventIsolation | None = None,
):
    """This function set up dispatcher with routers, filters and middlewares."""
    dp = Dispatcher(
        storage=storage,
        fsm_strategy=fsm_strategy,
        events_isolation=event_isolation,
    )
    for router in routers:
        dp.include_router(router)

    return dp

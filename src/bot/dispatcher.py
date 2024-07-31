"""This file contains build dispatcher logic."""
import os

from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.fsm.strategy import FSMStrategy
from fluent.runtime import FluentResourceLoader, FluentLocalization
from redis.asyncio.client import Redis

from src.configuration import conf

from .logic import routers
from .middlewares.i18n_md import I18nMiddleware

DEFAULT_LOCALE: str = conf.bot.DEFAULT_LOCALE
LOCALES: list[str] = conf.bot.LOCALES


def make_i18n_middleware():
    loader = FluentResourceLoader(os.path.join(
        os.path.dirname(__file__),
        "locales",
        "{locale}",
    ))
    l10ns = {
        locale: FluentLocalization(
            [locale, DEFAULT_LOCALE], ["lexicon.ftl"], loader,
        )
        for locale in LOCALES
    }
    return I18nMiddleware(l10ns, DEFAULT_LOCALE)


def get_redis_storage(
    redis: Redis, state_ttl=conf.redis.state_ttl, data_ttl=conf.redis.data_ttl
):
    """This function create redis storage or get it forcely from configuration.

    :param redis: Redis client instance
    :param state_ttl: FSM State Time-To-Delete timer in seconds (has effect only
    for Redis database)
    :param data_ttl: FSM Data Time-To-Delete timer in seconds (has effect only
    for Redis database)
    :return: Created Redis storage.
    """
    return RedisStorage(
        redis=redis,
        state_ttl=state_ttl,
        data_ttl=data_ttl,
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )


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

    # Register middlewares

    return dp

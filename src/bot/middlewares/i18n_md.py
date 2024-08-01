import os
from typing import Dict, Callable, Any, Awaitable, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from fluent.runtime import FluentLocalization, FluentResourceLoader
from fluentogram import TranslatorHub

from src.bot.utils.translation.fluentogram import create_translator_hub
from src.bot.utils.translation.i18n_format import I18N_FORMAT_KEY
from src.configuration import conf

DEFAULT_LOCALE: str = conf.bot.DEFAULT_LOCALE
LOCALES: list[str] = conf.bot.LOCALES


def make_i18n_middleware():
    loader = FluentResourceLoader(os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
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


class I18nMiddleware(BaseMiddleware):
    def __init__(
            self,
            l10ns: Dict[str, FluentLocalization],
            default_lang: str,
    ):
        super().__init__()
        self.l10ns = l10ns
        self.default_lang = default_lang

    async def __call__(
            self,
            handler: Callable[
                [Union[Message, CallbackQuery], Dict[str, Any]],
                Awaitable[Any],
            ],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any],
    ) -> Any:
        # some language/locale retrieving logic
        lang = self.default_lang

        l10n = self.l10ns[lang]
        # we use fluent.runtime here, but you can create custom functions
        data[I18N_FORMAT_KEY] = l10n.format_value
        hub: TranslatorHub = data.get('_translator_hub') or create_translator_hub()
        data['i18n'] = hub.get_translator_by_locale(locale=self.default_lang)

        return await handler(event, data)

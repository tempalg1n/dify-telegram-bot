import os

from fluent_compiler.bundle import FluentBundle

from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "locales",
        "{locale}",
        "lexicon.ftl"
    )
    translator_hub = TranslatorHub(
        {
            "ru": ("ru", "en"),
            "en": ("en", "ru")
        },
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=[path.format(locale='ru')])),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=[path.format(locale='en')]))
        ],
    )
    return translator_hub

"""This file represents configurations from files and environment."""
import os
from dataclasses import dataclass, field


@dataclass
class BotConfig:
    """Bot configuration."""

    token: str = os.getenv('BOT_TOKEN')
    LOCALES: list[str] = field(default_factory=lambda: [
        'en', 'ru'
    ])


@dataclass
class DifyConfig:
    api_key: str = os.getenv('DIFY_API_KEY')


@dataclass
class Configuration:
    """All in one configuration's class."""

    bot = BotConfig()
    dify = DifyConfig()


conf = Configuration()

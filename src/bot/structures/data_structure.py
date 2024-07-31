"""Data Structures.

This file contains TypedDict structure to store data which will
transfer throw Dispatcher->Middlewares->Handlers.
"""

from typing import TypedDict


class TransferData(TypedDict):
    """Common transfer data."""

    bot: Bot

"""
Shared Data Classes 

Note that this file is shared as is between pystuderxcom and pystudernext.
Do not place code that is specific to only one of these libraries in here!
"""

import logging

from dataclasses import dataclass
from typing import Iterable

from .types import StuderUserLevel


_LOGGER = logging.getLogger(__name__)


class StuderMessageUnknownException(Exception):
    pass

class StuderMessageSyntaxException(Exception):
    pass


@dataclass
class StuderMessageDef:
    level: StuderUserLevel
    number: int
    string: str


class StuderMessageSet:

    def __init__(self, messages: Iterable[StuderMessageDef]):
        self._messages = messages


    def get_by_nr(self, nr: int) -> StuderMessageDef:
        for msg in self._messages:
            if msg.number == nr:
                return msg

        raise StuderMessageUnknownException(nr)


    def str_by_nr(self, nr: int) -> str:
        msg = self.get_by_nr(nr)
        return msg.string

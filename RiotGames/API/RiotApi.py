#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

from RiotGames.API.Account import *
from RiotGames.Types.Server import Server


class RiotApi:
    def __init__(self, apikey: str):
        """
        :param apikey:
        """
        self._apiKey = apikey
        self.Account = Account(self)

    def _get_key(self) -> str:
        """
        :return:
        """
        return self._apiKey

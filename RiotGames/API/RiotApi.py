#  Copyright (c) 2020.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

class RiotApi:
    def __init__(self, apikey: str):
        """
        :param apikey:
        """
        self._apiKey = apikey

    def _get_key(self) -> str:
        """
        :return:
        """
        return self._apiKey

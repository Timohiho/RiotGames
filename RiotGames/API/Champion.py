#  Copyright (c) 2020.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source
import urllib.request

from RiotGames.API.RiotApi import RiotApi


class Champion(RiotApi):
    __champion_rotation_url = "https://{}.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={}"

    def __init__(self, apikey: str):
        """
        :param apikey: RiotGames API Key
        """
        super().__init__(apikey)
        self.__super = super()

    def champion_rotation(self, region: str) -> dict:
        """
        :param region: Server Region
        :return:
        """
        return eval(bytes(
            urllib.request.urlopen(self.__champion_rotation_url.format(region, super()._get_key())).read()).decode())

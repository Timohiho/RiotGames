#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

import urllib.request

from RiotGames.API.RiotApi import RiotApi
from RiotGames.Exceptions import *
from RiotGames.Types.Region import Region
from RiotGames.Types.Server import Server
from RiotGames.Account.Account import Account as AccountStruct


class Account(RiotApi):
    __account_by_puuid_url = "https://{}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{}?api_key={}"
    __account_by_riotid_url = "https://{}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{}/{}?api_key={}"

    def __init__(self, apikey: str, server: Server = Server.EUROPE):
        """
        :param apikey: RiotGames API Key
        """
        super().__init__(apikey)
        self.__super = super()
        self.__server = server

    def by_puuid(self, puuid: str):
        data: dict = eval(bytes(urllib.request.urlopen(
            self.__account_by_puuid_url.format(self.__server, puuid, super()._get_key())).read()).decode())
        if "puuid" in data.keys():
            return AccountStruct(data["puuid"], data["gameName"], data["tagLine"])
        else:
            if data["status"]["message"].startswith("Bad Request"):
                raise BadRequest
            else:
                raise Forbidden

    def by_riotid(self, region: Region, game_name: str):
        data: dict = eval(bytes(urllib.request.urlopen(
            self.__account_by_riotid_url.format(self.__server, game_name, region, super()._get_key())).read()).decode())
        if "puuid" in data.keys():
            return AccountStruct(data["puuid"], data["gameName"], data["tagLine"])
        else:
            if data["status"]["message"].startswith("Bad Request"):
                raise BadRequest
            else:
                raise Forbidden

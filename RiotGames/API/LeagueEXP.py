#  Copyright (c) 2020.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

import urllib.request

from RiotGames.Summoner.Ranked import Ranked

from RiotGames.API.RiotApi import RiotApi


class LeagueEXP(RiotApi):
    __queue_entries_url: str = "https://{}.api.riotgames.com/lol/league-exp/v4/entries/{}/{}?page={}&api_key={}"

    def __init__(self, apikey: str):
        """
        :param apikey:
        """
        super().__init__(apikey)
        self.__super = super()

    def queue_entries(self, region: str, queue: str, tier: str, division: str, page: int = 1) -> [Ranked]:
        """
        :param region:
        :param queue:
        :param tier:
        :param division:
        :param page:
        :return:
        """
        summoner_entries: [Ranked] = []

        data: dict = eval(bytes(urllib.request.urlopen(
            self.__queue_entries_url.format(region, queue, tier, division, page,
                                            super()._get_key())).read()).decode().replace("true", "True").replace(
            "false", "False"))
        for ranked_data in data:
            summoner_entries.append(Ranked(ranked_data["queueType"],
                                           ranked_data["summonerName"],
                                           ranked_data["hotStreak"],
                                           ranked_data["wins"],
                                           ranked_data["veteran"],
                                           ranked_data["losses"],
                                           ranked_data["freshBlood"],
                                           ranked_data["tier"],
                                           ranked_data["inactive"],
                                           ranked_data["rank"],
                                           ranked_data["summonerId"],
                                           ranked_data["leaguePoints"]))

        return summoner_entries

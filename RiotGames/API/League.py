#  Copyright (c) 2020.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

import urllib.request

from RiotGames.Summoner.Ranked import Ranked

from RiotGames.API.RiotApi import RiotApi


class League(RiotApi):
    __challenger_url: str = "https://{}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{}?api_key={}"
    __summoner_entries_url: str = "https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}"
    __queue_entries_url: str = "https://{}.api.riotgames.com/lol/league/v4/entries/{}/{}?page={}&api_key={}"
    __grandmaster_url: str = "https://{}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{}?api_key={}"
    __ranked_list_entries_url: str = "https://{}.api.riotgames.com/lol/league/v4/leagues/{}?api_key={}"
    __master_url: str = "https://{}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{}?api_key={}"

    def __init__(self, apikey: str):
        """
        :param apikey:
        """
        super().__init__(apikey)
        self.__super = super()

    def challenger(self, queue: str, region: str) -> [Ranked]:
        """
        :param queue:
        :param region:
        :return:
        """
        challenger_league: [Ranked] = []

        data: dict = eval(bytes(urllib.request.urlopen(
            self.__challenger_url.format(region, queue, super()._get_key())).read()).decode().replace("true",
                                                                                                      "True").replace(
            "false", "False"))
        for ranked_data in data["entries"]:
            challenger_league.append(Ranked(data["queue"],
                                            ranked_data["summonerName"],
                                            ranked_data["hotStreak"],
                                            ranked_data["wins"],
                                            ranked_data["veteran"],
                                            ranked_data["losses"],
                                            ranked_data["freshBlood"],
                                            data["tier"],
                                            ranked_data["inactive"],
                                            ranked_data["rank"],
                                            ranked_data["summonerId"],
                                            ranked_data["leaguePoints"]))

        return challenger_league

    def summoner_entries(self, summoner_id: str, region: str) -> [Ranked]:
        """
        :param summoner_id:
        :param region:
        :return:
        """
        summoner_entries: [Ranked] = []

        data: dict = eval(bytes(
            urllib.request.urlopen(
                self.__summoner_entries_url.format(region, summoner_id, super()._get_key())).read()).decode().replace(
            "true", "True").replace("false", "False"))
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

    def grandmaster(self, queue: str, region: str) -> [Ranked]:
        """
        :param queue:
        :param region:
        :return:
        """
        grandmaster_league: [Ranked] = []

        data: dict = eval(bytes(urllib.request.urlopen(
            self.__grandmaster_url.format(region, queue, super()._get_key())).read()).decode().replace("true",
                                                                                                       "True").replace(
            "false", "False"))
        for ranked_data in data["entries"]:
            grandmaster_league.append(Ranked(data["queue"],
                                             ranked_data["summonerName"],
                                             ranked_data["hotStreak"],
                                             ranked_data["wins"],
                                             ranked_data["veteran"],
                                             ranked_data["losses"],
                                             ranked_data["freshBlood"],
                                             data["tier"],
                                             ranked_data["inactive"],
                                             ranked_data["rank"],
                                             ranked_data["summonerId"],
                                             ranked_data["leaguePoints"]))

        return grandmaster_league

    def ranked_list_entries(self, league_id: str, region) -> [Ranked]:
        """
        :param league_id:
        :param region:
        :return:
        """
        ranked_entries: [Ranked] = []

        data: dict = eval(bytes(urllib.request.urlopen(
            self.__master_url.format(region, league_id, super()._get_key())).read()).decode().replace("true",
                                                                                                      "True").replace(
            "false", "False"))
        for ranked_data in data["entries"]:
            ranked_entries.append(Ranked(data["queue"],
                                         ranked_data["summonerName"],
                                         ranked_data["hotStreak"],
                                         ranked_data["wins"],
                                         ranked_data["veteran"],
                                         ranked_data["losses"],
                                         ranked_data["freshBlood"],
                                         data["tier"],
                                         ranked_data["inactive"],
                                         ranked_data["rank"],
                                         ranked_data["summonerId"],
                                         ranked_data["leaguePoints"]))

        return ranked_entries

    def master(self, queue: str, region: str) -> [Ranked]:
        """
        :param queue:
        :param region:
        :return:
        """
        master_league: [Ranked] = []

        data: dict = eval(bytes(urllib.request.urlopen(
            self.__master_url.format(region, queue, super()._get_key())).read()).decode().replace("true",
                                                                                                  "True").replace(
            "false", "False"))
        for ranked_data in data["entries"]:
            master_league.append(Ranked(data["queue"],
                                        ranked_data["summonerName"],
                                        ranked_data["hotStreak"],
                                        ranked_data["wins"],
                                        ranked_data["veteran"],
                                        ranked_data["losses"],
                                        ranked_data["freshBlood"],
                                        data["tier"],
                                        ranked_data["inactive"],
                                        ranked_data["rank"],
                                        ranked_data["summonerId"],
                                        ranked_data["leaguePoints"]))

        return master_league

#  Copyright (c) 2020.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

import urllib.request

from RiotGames.Summoner.Account import SummonerAccount

from RiotGames.API.RiotApi import RiotApi


class ChampionMasteries:
    def __init__(self, champion_level: int, chest_granted: bool, champion_points: int,
                 champion_points_since_last_level: int, champion_points_until_next_level: int, summoner_id: str,
                 tokens_earned: int, champion_id: int, last_play_time: int):
        """
        :param champion_level:
        :param chest_granted:
        :param champion_points:
        :param champion_points_since_last_level:
        :param champion_points_until_next_level:
        :param summoner_id:
        :param tokens_earned:
        :param champion_id:
        :param last_play_time:
        """
        self.championLevel: int = champion_level
        self.chestGranted: bool = chest_granted
        self.championPoints: int = champion_points
        self.championPointsSinceLastLevel: int = champion_points_since_last_level
        self.championPointsUntilNextLevel: int = champion_points_until_next_level
        self.summonerId: str = summoner_id
        self.tokensEarned: int = tokens_earned
        self.championId: int = champion_id
        self.lastPlayTime: int = last_play_time


class ChampionMastery(RiotApi):
    __summoner_masteries_url: str = \
        "https://{}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}"
    __champion_masteries_url: str = \
        "https://{}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}/{}?api_key={}"
    __score_url: str = "https://{}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{}?api_key={}"

    def __init__(self, apikey: str):
        """
        :param apikey:
        """
        super().__init__(apikey)
        self.__super = super()

    def summoner_masteries(self, summoner: SummonerAccount, region: str) -> [ChampionMasteries]:
        """
        :param summoner:
        :param region:
        :return:
        """
        summoner_masteries: [ChampionMasteries] = []

        data: dict = eval(bytes(urllib.request.urlopen(
            self.__summoner_masteries_url.format(region, summoner.summonerId,
                                                 super()._get_key())).read()).decode().replace("true", "True")
                          .replace("false", "False"))
        for champion_data in data:
            summoner_masteries.append(ChampionMasteries(champion_data["championLevel"],
                                                        champion_data["chestGranted"],
                                                        champion_data["championPoints"],
                                                        champion_data["championPointsSinceLastLevel"],
                                                        champion_data["championPointsUntilNextLevel"],
                                                        champion_data["summonerId"],
                                                        champion_data["tokensEarned"],
                                                        champion_data["championId"],
                                                        champion_data["lastPlayTime"]))
        return summoner_masteries

    def champion_masteries(self, summoner: SummonerAccount, champion_id: int, region: str) -> ChampionMasteries:
        """
        :param summoner:
        :param champion_id:
        :param region:
        :return:
        """
        data: dict = eval(bytes(urllib.request.urlopen(
            self.__summoner_masteries_url.format(region, summoner.summonerId, champion_id,
                                                 super()._get_key())).read()).decode().replace("true", "True")
                          .replace("false", "False"))
        return ChampionMasteries(data["championLevel"],
                                 data["chestGranted"],
                                 data["championPoints"],
                                 data["championPointsSinceLastLevel"],
                                 data["championPointsUntilNextLevel"],
                                 data["summonerId"],
                                 data["tokensEarned"],
                                 data["championId"],
                                 data["lastPlayTime"])

    def scores(self, summoner: SummonerAccount, region: str):
        """
        :param summoner:
        :param region:
        :return:
        """
        return eval(bytes(
            urllib.request.urlopen(
                self.__score_url.format(region, summoner.summonerId, super()._get_key())).read()).decode())

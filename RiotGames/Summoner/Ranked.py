#  Copyright (c) 2020.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source


class Ranked:
    def __init__(self, queue: str, summoner_name: str, hot_streak: bool, wins: int, veteran: bool, losses: int,
                 fresh_blood: bool, tier: str, inactive: bool, rank: str, summoner_id: str, league_points: int):
        """
        :param queue:
        :param summoner_name:
        :param hot_streak:
        :param wins:
        :param veteran:
        :param losses:
        :param fresh_blood:
        :param tier:
        :param inactive:
        :param rank:
        :param summoner_id:
        :param league_points:
        """
        self.queue: str = queue
        self.summonerName: str = summoner_name
        self.hotStreak: bool = hot_streak
        self.wins: int = wins
        self.veteran: bool = veteran
        self.losses: int = losses
        self.freshBlood: bool = fresh_blood
        self.tier: str = tier
        self.inactive: bool = inactive
        self.rank: str = rank
        self.summonerId: str = summoner_id
        self.leaguePoints: int = league_points

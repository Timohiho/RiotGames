#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

from RiotGames.League import Rank, Tier


class Entry:
    summoner_id: str
    summoner_name: str
    league_points: int
    tier: Tier
    rank: Rank
    wins: int
    losses: int
    veteran: bool
    inactive: bool
    fresh_blood: bool
    hot_streak: bool

    def __init__(self, summoner_id: str, summoner_name: str, league_points: int, rank: Rank, tier: Tier, wins: int,
                 losses: int, veteran: bool, inactive: bool, fresh_blood: bool, hot_streak: bool) -> None:
        self.summoner_id = summoner_id
        self.summoner_name = summoner_name
        self.league_points = league_points
        self.tier = tier
        self.rank = rank
        self.wins = wins
        self.losses = losses
        self.veteran = veteran
        self.inactive = inactive
        self.fresh_blood = fresh_blood
        self.hot_streak = hot_streak

#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

class ChampionMastery:
    champion_id: int
    champion_level: int
    champion_points: int
    last_play_time: int
    champion_points_since_last_level: int
    champion_points_until_next_level: int
    chest_granted: bool
    tokens_earned: int
    summoner_id: str

    def __init__(self, champion_id: int, champion_level: int, champion_points: int, last_play_time: int,
                 champion_points_since_last_level: int, champion_points_until_next_level: int, chest_granted: bool,
                 tokens_earned: int, summoner_id: str) -> None:
        self.champion_id = champion_id
        self.champion_level = champion_level
        self.champion_points = champion_points
        self.last_play_time = last_play_time
        self.champion_points_since_last_level = champion_points_since_last_level
        self.champion_points_until_next_level = champion_points_until_next_level
        self.chest_granted = chest_granted
        self.tokens_earned = tokens_earned
        self.summoner_id = summoner_id

#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

from typing import List

from RiotGames.Types.Region import Region


class ChampionRotation:
    region: Region
    free_champion_ids: List[int]
    free_champion_ids_for_new_players: List[int]
    max_new_player_level: int

    def __init__(self, region: Region, free_champion_ids: List[int], free_champion_ids_for_new_players: List[int],
                 max_new_player_level: int) -> None:
        self.region = region
        self.free_champion_ids = free_champion_ids
        self.free_champion_ids_for_new_players = free_champion_ids_for_new_players
        self.max_new_player_level = max_new_player_level

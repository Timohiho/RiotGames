#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source
from RiotGames.Types import Region


class Account:
    puuid: str
    game_name: str
    tag_line: Region

    def __init__(self, puuid: str, game_name: str, tag_line: Region) -> None:
        self.puuid = puuid
        self.game_name = game_name
        self.tag_line = tag_line

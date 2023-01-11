#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

from typing import List, Any

from RiotGames.Status import Game
from RiotGames.Types.Region import Region


class Status:
    region: Region
    game: Game
    id: str
    name: str
    locales: List[str]
    maintenances: List[Any]
    incidents: List[Any]

    def __init__(self, region: Region, game: Game, id: str, name: str, locales: List[str], maintenances: List[Any],
                 incidents: List[Any]) -> None:
        self.region = region
        self.game = game
        self.id = id
        self.name = name
        self.locales = locales
        self.maintenances = maintenances
        self.incidents = incidents

#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

from typing import List
from uuid import UUID

from RiotGames.League import Entry, Queue, Tier


class League:
    tier: Tier
    league_id: UUID
    queue: Queue
    name: str
    entries: List[Entry]

    def __init__(self, tier: str, league_id: UUID, queue: Queue, name: str, entries: List[Entry]) -> None:
        self.tier = tier
        self.league_id = league_id
        self.queue = queue
        self.name = name
        self.entries = entries

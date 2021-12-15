#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

class ActiveShard:
    puuid: str
    game: str
    active_shard: str

    def __init__(self, puuid: str, game: str, active_shard: str) -> None:
        self.puuid = puuid
        self.game = game
        self.active_shard = active_shard
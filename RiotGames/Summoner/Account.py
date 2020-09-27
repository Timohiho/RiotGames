#  Copyright (c) 2020.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

class SummonerAccount:
    def __init__(self, summoner_id: str, account_id: str, puuid: str, name: str, profile_icon_id: str,
                 revision_date: int, summoner_level: int):
        """
        :param summoner_id:
        :param account_id:
        :param puuid:
        :param name:
        :param profile_icon_id:
        :param revision_date:
        :param summoner_level:
        """
        self.summonerId: str = summoner_id
        self.accountId: str = account_id
        self.puuid: str = puuid
        self.name: str = name
        self.profileIconId: str = profile_icon_id
        self.revisionDate: int = revision_date
        self.summonerLevel: int = summoner_level

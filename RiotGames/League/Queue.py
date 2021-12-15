#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

from enum import Enum


class Queue(Enum):
    RANKED_SOLO_5x5 = "RANKED_SOLO_5x5"
    RANKED_FLEX_SR = "RANKED_FLEX_SR"
    RANKED_FLEX_TT = "RANKED_FLEX_TT"

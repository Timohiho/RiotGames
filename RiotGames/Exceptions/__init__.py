#  Copyright (c) 2021.
#  The copyright lies with Timo Hirsch-Hoffmann, the further use is only permitted with reference to source

class Error(Exception):
    """Base class for other exceptions"""
    pass

class BadRequest(Error):
    pass

class Forbidden(Error):
    pass
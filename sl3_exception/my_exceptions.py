
class Error(Exception):
    '''Base Exception costum class'''
    pass
class ValueTooSmallError(Error):
    '''Rase Value when it is too small'''
    pass
class ValueTooLarge(Error):
    '''Rase Value when it is too Large'''
    pass
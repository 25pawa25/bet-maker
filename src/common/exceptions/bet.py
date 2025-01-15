from common.exceptions import AppException
from common.exceptions.base import ObjectDoesNotExist


class BetError(AppException):
    """Base Bet Exception"""


class BetNotExists(ObjectDoesNotExist):
    """Bet not exists"""

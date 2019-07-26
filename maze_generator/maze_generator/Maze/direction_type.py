from enum import Enum
from random import Random


class DirectionType(Enum):

    # --------------------------------------------------------------------------
    # Cases
    # --------------------------------------------------------------------------

    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    # --------------------------------------------------------------------------
    # TODO POC
    # --------------------------------------------------------------------------

    def __str__(self):
        if self == DirectionType.NORTH:
            return "NORTH"
        elif self == DirectionType.SOUTH:
            return "SOUTH"
        elif self == DirectionType.WEST:
            return "WEST"
        elif self == DirectionType.EAST:
            return "EAST"
        raise ValueError("Unknown enum value")

    def opposite(self):
        if self == DirectionType.NORTH:
            return DirectionType.SOUTH
        elif self == DirectionType.SOUTH:
            return DirectionType.NORTH
        elif self == DirectionType.WEST:
            return DirectionType.EAST
        elif self == DirectionType.EAST:
            return DirectionType.WEST
        raise ValueError("Unknown enum value")

    @staticmethod
    def all():
        return [DirectionType.NORTH,
                DirectionType.SOUTH,
                DirectionType.EAST,
                DirectionType.WEST]

    @staticmethod
    def random():
        return Random().choice(DirectionType.all())

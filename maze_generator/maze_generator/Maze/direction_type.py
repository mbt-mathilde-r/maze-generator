from enum import Enum


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

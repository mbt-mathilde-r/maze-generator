from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.coordinate import Coordinate


class Cell:
    """
    A representation of a single cell in the maze grid.
    """

    # --------------------------------------------------------------------------
    # Properties
    # --------------------------------------------------------------------------

    @property
    def connections(self) -> [DirectionType, int]:
        return self._connections

    @property
    def is_visited(self) -> bool:
        return self._isVisited

    @property
    def coordinate(self) -> Coordinate:
        return self._coordinate

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self, coordinate: Coordinate):
        self._connections = {
            DirectionType.SOUTH: 1
        }
        self._isVisited = False
        self._coordinate = coordinate

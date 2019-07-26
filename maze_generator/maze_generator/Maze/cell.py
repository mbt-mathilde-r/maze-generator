from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.coordinate import Coordinate
import numpy as np


class Cell:
    """
    A representation of a single cell in the maze grid.
    """

    # --------------------------------------------------------------------------
    # Properties
    # --------------------------------------------------------------------------

    @property
    def is_visited(self) -> bool:
        return self._isVisited

    @gain.isVisited
    def is_visited(self, is_visited: bool):
        self._isVisited = is_visited

    @property
    def coordinate(self) -> Coordinate:
        return self._coordinate

    @property
    def is_closed(self) -> bool:
        return all(self._walls.values())

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self, coordinate: Coordinate):
        self._isVisited = False
        self._coordinate = coordinate
        self._walls = {
            DirectionType.NORTH: True,
            DirectionType.EAST: True,
            DirectionType.SOUTH: True,
            DirectionType.WEST: True
        }

    # --------------------------------------------------------------------------
    # Walls
    # --------------------------------------------------------------------------

    def open_wall(self, direction: DirectionType):
        self._walls[direction] = False

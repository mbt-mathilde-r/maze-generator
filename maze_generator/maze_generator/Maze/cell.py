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
    def coordinate(self) -> Coordinate:
        return self.__coordinate

    @property
    def is_closed(self) -> bool:
        return all(self.__walls.values())

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self, coordinate: Coordinate):
        self.isVisited = False
        self.__coordinate = coordinate
        self.__walls = {
            DirectionType.NORTH: True,
            DirectionType.EAST: True,
            DirectionType.SOUTH: True,
            DirectionType.WEST: True
        }

    # --------------------------------------------------------------------------
    # Walls
    # --------------------------------------------------------------------------

    def open_wall(self, direction: DirectionType):
        self.__walls[direction] = False

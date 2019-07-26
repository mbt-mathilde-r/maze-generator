from maze_generator.Maze.cell import Cell
from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.direction_type import DirectionType
from numpy import ndarray
from typing import Optional


# ------------------------------------------------------------------------------
# Representation of a maze grid with cells and walls
# ------------------------------------------------------------------------------

class Maze:

    # --------------------------------------------------------------------------
    # Properties
    # --------------------------------------------------------------------------

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    # --------------------------------------------------------------------------
    # Initialize
    # --------------------------------------------------------------------------

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._grid = ndarray(self.create_maze_grid())

    # --------------------------------------------------------------------------
    # Create the grid for the futur maze
    # --------------------------------------------------------------------------

    def create_maze_grid(self) -> [[Cell]]:
        maze = []
        for y in range(self._height):
            maze_line = []
            for x in range(self._width):
                maze_line.append(Cell(Coordinate(x, y)))
            maze.append(maze_line)
        return maze

    def open_wall(self, cell: Cell, direction: DirectionType) -> bool:
        """
        Open a wall between two cells
        """
        neighbour = self.__get_cell_neighbour(cell, direction)
        if neighbour is None:
            return False
        cell.open_wall(direction)
        neighbour.open_wall(direction.opposite())
        return True

    def __get_cell_neighbour(self, cell: Cell, direction: DirectionType) -> \
            Optional[Cell]:
        """
        Get the cell's neighbour in the given direction
        """
        coordinate = cell.coordinate
        if direction == DirectionType.NORTH:
            coordinate.y -= 1
        elif direction == DirectionType.SOUTH:
            coordinate.y += 1
        elif direction == DirectionType.EAST:
            coordinate.x += 1
        elif direction == DirectionType.WEST:
            coordinate.x -= 1
        else:
            raise ValueError("Unknown enum value")
        return self.__get_cell(coordinate)

    def __get_cell(self, coordinate: Coordinate) -> Optional[Cell]:
        """
        Get the cell at the given coordinate
        """
        if coordinate.is_valid(self._width, self._height):
            return self._grid[coordinate.y][coordinate.x]
        else:
            return None

from maze_generator.Maze.cell import Cell
from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.neighbour import Neighbour
from numpy import ndarray
from typing import Optional
from random import Random


class MazeGrid:

    # --------------------------------------------------------------------------
    # Properties
    # --------------------------------------------------------------------------

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def __getitem__(self, key: int) -> [Cell]:
        return self._grid[key]

    # --------------------------------------------------------------------------
    # Initialize
    # --------------------------------------------------------------------------

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._grid = self.create_grid()
        Random().seed()

    def create_grid(self) -> [[Cell]]:
        """
        Create the grid for the future maze
        """
        maze = []
        for y in range(self._height):
            maze_line = []
            for x in range(self._width):
                maze_line.append(Cell(Coordinate(x, y)))
            maze.append(maze_line)
        return maze

    def get_random_unvisited_neighbour(self, cell) -> Optional[Neighbour]:
        """
        Get a random unvisited neighbour cell or None if the cell as no
        unvisited neighbour
        """
        unvisited_neighbours = self.get_unvisited_neighbours(cell)
        if unvisited_neighbours.__len__() == 0:
            return None
        index = Random().randint(0, unvisited_neighbours.__len__() - 1)
        return unvisited_neighbours[index]

    def get_unvisited_neighbours(self, cell) -> [Neighbour]:
        """
        Get the list of unvisited neighbours of the cell
        """
        unvisited_neighbours = []
        for direction in DirectionType.all():
            print("direction " + direction.__str__())
            neighbour = self.get_cell_neighbour(cell, direction)
            if neighbour is not None:
                if not neighbour.isVisited:
                    unvisited_neighbours.append(Neighbour(direction, neighbour))
        return unvisited_neighbours

    def get_cell_neighbour(self,
                           cell: Cell,
                           direction: DirectionType) -> Optional[Cell]:
        """
        Get the cell's neighbour in the given direction
        """
        coordinate = Coordinate(cell.coordinate.x, cell.coordinate.y)
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
        return self.get_cell(coordinate)

    def get_cell(self, coordinate: Coordinate) -> Optional[Cell]:
        """
        Get the cell at the given coordinate
        """
        if coordinate.is_valid(self._width, self._height):
            return self._grid[coordinate.y][coordinate.x]
        else:
            return None

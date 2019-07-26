from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.cell import Cell


class Neighbour:

    def __init__(self, direction: DirectionType, cell: Cell):
        self.direction = direction
        self.cell = cell

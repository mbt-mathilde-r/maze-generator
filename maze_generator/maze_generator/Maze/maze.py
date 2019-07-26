from maze_generator.Maze.cell import Cell
from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.direction_type import DirectionType
from numpy import matrix


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
        self._grid = self.create_maze_grid()

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

    def cellAt(self, cell: Cell, direction: DirectionType) -> Cell:
        coordinate = cell.coordinate
        if direction == DirectionType.NORTH:
            coordinate.y -= 1
        elif direction == DirectionType.SOUTH:
            coordinate.y += 1
        elif direction == DirectionType.EAST:
            coordinate.x += 1
        elif direction == DirectionType.WEST
            coordinate -= 1
        else
            raise ValueError("Unknown enum value")

        if coordinate.x < 0


    def open_wall(self, cell: Cell, direction: DirectionType):
        print("open wall")

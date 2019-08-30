from maze_generator.Maze.cell import Cell
from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.maze_grid import MazeGrid
from maze_generator.Maze.direction_type import DirectionType
# TEMP
from maze_generator.displayer.display_type import DisplayType
from maze_generator.displayer.displayer import Displayer
import time

# ------------------------------------------------------------------------------
# Representation of a maze grid with cells and walls
# ------------------------------------------------------------------------------

class Maze:

    # --------------------------------------------------------------------------
    # Properties
    # --------------------------------------------------------------------------

    @property
    def width(self) -> int:
        return self._grid.width

    @property
    def height(self) -> int:
        return self._grid.height

    def __getitem__(self, key: int) -> [Cell]:
        return self._grid[key]

    # --------------------------------------------------------------------------
    # Initialize
    # --------------------------------------------------------------------------

    def __init__(self, width: int, height: int, step_by_step: bool = False):
        self._grid = MazeGrid(width, height)
        self._step_by_step = step_by_step
        self.build_maze()

    # --------------------------------------------------------------------------
    # Create Maze
    # --------------------------------------------------------------------------

    def build_maze(self):
        self.iterate_neighbour_opening_walls(self._grid.get_cell(Coordinate(
            0, 0)))

    def iterate_neighbour_opening_walls(self, cell: Cell):
        if cell is None:
            return
        cell.isVisited = True
        neighbour = self._grid.get_random_unvisited_neighbour(cell)
        if neighbour is None:
            return
        self.open_wall(cell, neighbour.direction)

        self.iterate_neighbour_opening_walls(neighbour.cell)
        self.iterate_neighbour_opening_walls(cell)

    # --------------------------------------------------------------------------
    # Maze walls
    # --------------------------------------------------------------------------

    def open_wall(self, cell: Cell, direction: DirectionType) -> bool:
        """
        Open a wall between two cells
        """
        neighbour = self._grid.get_cell_neighbour(cell, direction)
        if neighbour is None:
            return False
        cell.open_wall(direction)
        neighbour.open_wall(direction.opposite())
        if self._step_by_step:
            self.display(DisplayType.ASCII)
            time.sleep(0.05)
        return True

    def display(self, display_type: DisplayType):
        """
        Display the current maze
        :param display_type: type of display for the maze
        """
        Displayer.display(self._grid, display_type)


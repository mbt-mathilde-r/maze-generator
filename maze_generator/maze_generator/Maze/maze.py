from maze_generator.Maze.cell import Cell
from maze_generator.generator.maze_digger import MazeDigger
from maze_generator.Maze.maze_grid import MazeGrid
from maze_generator.displayer.display_type import DisplayType
from maze_generator.displayer.displayer import Displayer
import time

# ------------------------------------------------------------------------------
# Representation of a maze grid with cells and walls
# ------------------------------------------------------------------------------
from maze_generator.generator.maze_resolver import MazeResolver


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

    def __init__(self, grid: MazeGrid, step_by_step: bool = False):
        self._grid = grid
        self._step_by_step = step_by_step
        self.__build_maze()

    def __build_maze(self):
        maze_digger = MazeDigger(step_action=self.step_display)
        maze_digger.dig(grid=self._grid)

    # --------------------------------------------------------------------------
    # Resolve
    # --------------------------------------------------------------------------

    def resolve(self):
        maze_resolver = MazeResolver(step_action=self.step_display)
        maze_resolver.resolve(self._grid)

    # --------------------------------------------------------------------------
    # Display
    # --------------------------------------------------------------------------

    def display(self, display_type: DisplayType):
        """
        Display the current maze
        :param display_type: type of display for the maze
        """
        Displayer.display(self._grid, display_type)

    def step_display(self):
        if self._step_by_step:
            self.display(DisplayType.ASCII)
            time.sleep(0.05)

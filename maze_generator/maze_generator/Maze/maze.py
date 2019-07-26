from maze_generator.Maze.cell import Cell
from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.maze_grid import MazeGrid
from maze_generator.Maze.direction_type import DirectionType


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

    def __init__(self, width: int, height: int):
        self._grid = MazeGrid(width, height)
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
        print("unvisited neighbour")
        print(neighbour.cell.coordinate.__str__())
        cell.open_wall(neighbour.direction)
        self.iterate_neighbour_opening_walls(neighbour.cell)

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
        return True


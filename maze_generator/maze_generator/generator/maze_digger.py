from maze_generator.Maze.cell import Cell
from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.maze_grid import MazeGrid

# ------------------------------------------------------------------------------
# Use a maze grid to dig a maze path
# ------------------------------------------------------------------------------


class MazeDigger:

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self, step_action=None):
        self._step_action = step_action

    # --------------------------------------------------------------------------
    # Create Maze
    # --------------------------------------------------------------------------
    
    def dig(self, grid: MazeGrid):
        self.__iterate_neighbour_opening_walls(grid, grid.get_cell(Coordinate(
            0, 0)))
        self.__unvisit_all_cells(grid)
        self.__open_enter_and_exit_wall(grid)

    def __iterate_neighbour_opening_walls(self, grid: MazeGrid, cell: Cell):
        if cell is None:
            return
        cell.isVisited = True
        neighbour = grid.get_random_unvisited_neighbour(cell)
        if neighbour is None:
            return
        self.__open_wall(grid, cell, neighbour.direction)

        self.__iterate_neighbour_opening_walls(grid, neighbour.cell)
        self.__iterate_neighbour_opening_walls(grid, cell)

    def __open_wall(self, grid: MazeGrid, cell: Cell,
                    direction: DirectionType) -> bool:
        """
        Open a wall between two cells
        """
        neighbour = grid.get_cell_neighbour(cell, direction)
        if neighbour is None:
            return False
        cell.open_wall(direction)
        neighbour.open_wall(direction.opposite())
        if self._step_action is not None:
            self._step_action()
        return True

    def __open_enter_and_exit_wall(self, grid: MazeGrid):
        self.__open_enter_wall(grid)
        self.__open_exit_wall(grid)

    def __open_enter_wall(self, grid: MazeGrid):
        cell = grid.get_cell(Coordinate(x=0, y=0))
        open_direction = DirectionType.WEST

        cell.open_wall(open_direction)
        cell.isStart = True

    def __open_exit_wall(self, grid: MazeGrid):
        cell = grid.get_cell(Coordinate(x=grid.width - 1, y=grid.height - 1))
        open_direction = DirectionType.EAST

        cell.open_wall(open_direction)
        cell.isEnd = True

    def __unvisit_all_cells(self, grid: MazeGrid):
        grid.change_visit_all(is_visited=False)


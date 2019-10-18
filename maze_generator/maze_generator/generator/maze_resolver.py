from maze_generator.Maze.cell import Cell
from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.maze_grid import MazeGrid
from typing import Optional

# ------------------------------------------------------------------------------
# Resolve maze grid
# ------------------------------------------------------------------------------
from maze_generator.Maze.neighbour import Neighbour


class MazeResolver:

    # --------------------------------------------------------------------------
    # Step Action
    # --------------------------------------------------------------------------

    def __init__(self, grid: MazeGrid, step_action=None):
        self._grid = grid
        self._step_action = step_action

    # --------------------------------------------------------------------------
    # Resolver
    # --------------------------------------------------------------------------

    def resolve(self):
        print("Start resolve")
        start_cell = self._grid.get_start_cell()
        end_cell = self._grid.get_end_cell()

        if start_cell is None:
            raise Exception("Missing start cell on maze grid")
        if end_cell is None:
            raise Exception("Missing end cell on maze grid")

        resolve_path = self.__resolve_brutforce(start_cell, end_cell)
        self._grid.change_visit_all(False)
        self.__set_path_on_grid(resolve_path)

    def __resolve_brutforce(self, start: Cell, end: Cell) -> [Cell]:
        start.isVisited = True
        self._step_action()
        if start == end:
            return [start]
        neighbour = self.__get_accessible_neighbour(start)
        if not neighbour:
            start.isInvalid = True
            return []
        path = self.__resolve_brutforce(start=neighbour, end=end)
        if len(path) > 0:
            return [start] + path
        return self.__resolve_brutforce(start=start, end=end)

    def __get_accessible_neighbour(self, cell: Cell) -> Optional[Cell]:
        """
        An accessible neighbour is a cell next to the given cell, without wall
        between them, this cell should not have been visited yet
        """
        for direction in DirectionType.all():
            if not cell.is_direction_open(direction):
                continue
            neighbour = self._grid.get_cell_neighbour(cell, direction)
            if neighbour.isVisited:
                continue
            return neighbour
        return None

    def __set_path_on_grid(self, path: [Cell]):
        for i in range(0, len(path)):
            path[i].isVisited = True



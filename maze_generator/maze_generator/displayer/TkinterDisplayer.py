from tkinter import *

from maze_generator.Maze.cell import Cell
from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.maze_grid import MazeGrid


class TkinterDisplayer:

    def __init__(self):
        self._window_padding = 20
        self._cell_width = 20
        self._cell_height = 20
        self._canvas = None

        self._window = Tk()

    def display(self, maze: MazeGrid):
        if self._canvas is None:
            self._canvas = self.__create_canvas(maze)

        self.__draw_maze(self._canvas, maze)
        self._window.mainloop()

    def __create_canvas(self, maze: MazeGrid) -> Canvas:
        width = maze.width * self._cell_width + self._window_padding
        height = maze.height * self._cell_height + self._window_padding
        maze_canvas = Canvas(self._window, width=width, height=height,
                             bg="white")
        maze_canvas.pack()
        return maze_canvas

    def __draw_maze(self, canvas: Canvas, maze: MazeGrid):
        height = maze.height
        width = maze.width

        for y in range(0, height):
            for x in range(0, width):
                self.draw_cell(canvas, maze.get_cell(Coordinate(x=x, y=y)))

    def draw_cell(self, canvas: Canvas, cell: Cell):
        x = cell.coordinate.x
        y = cell.coordinate.y
        start_x = x * self._cell_width + (self._window_padding / 2)
        start_y = y * self._cell_height + (self._window_padding / 2)
        stop_x = start_x + self._cell_width
        stop_y = start_y + self._cell_height

        if cell.isVisited:
            canvas.create_rectangle(start_x, start_y, stop_x, stop_y,
                                    fill="green", outline="green")

        if not cell.is_direction_open(DirectionType.NORTH):
            canvas.create_line(start_x, start_y, stop_x, start_y)
        if not cell.is_direction_open(DirectionType.WEST):
            canvas.create_line(start_x, start_y, start_x, stop_y)
        if not cell.is_direction_open(DirectionType.EAST):
            canvas.create_line(stop_x, start_y, stop_x, stop_y)
        if not cell.is_direction_open(DirectionType.SOUTH):
            canvas.create_line(start_x, stop_y, stop_x, stop_y)


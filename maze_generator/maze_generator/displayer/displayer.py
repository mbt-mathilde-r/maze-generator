from maze_generator.Maze.maze_grid import MazeGrid
from maze_generator.displayer.TkinterDisplayer import TkinterDisplayer
from maze_generator.displayer.ascii_displayer import AsciiDisplayer
from maze_generator.displayer.display_type import DisplayType


class Displayer:

    __tkinter = None

    @staticmethod
    def init(completion):
        if Displayer.__tkinter is None:
            Displayer.__tkinter = TkinterDisplayer()
            Displayer.__tkinter.start(completion)

    @staticmethod
    def display(maze: MazeGrid, display_type: DisplayType):
        if display_type == DisplayType.ASCII:
            AsciiDisplayer.display(maze)
        if display_type == DisplayType.TKINTER:
            Displayer.__tkinter.display(maze)

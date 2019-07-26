from maze_generator.Maze.maze import Maze
from maze_generator.displayer.display_type import DisplayType

class Displayer:

    @staticmethod
    def display(maze: Maze, display_type: DisplayType):
        if display_type == DisplayType.ASCII:
            Displayer.display_as_ascii(maze)

    @staticmethod
    def display_as_ascii(maze: Maze):
        #TODO

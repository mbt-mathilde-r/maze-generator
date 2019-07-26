from maze_generator.Maze.maze import Maze
from maze_generator.displayer.display_type import DisplayType
from maze_generator.displayer.displayer import Displayer


class MainMazeGenerator:

    # --------------------------------------------------------------------------
    # Initializatio
    # --------------------------------------------------------------------------

    def __init__(self):
        print("Todo")

    if __name__ == '__main__':
        print("Hello")
        maze = Maze(5, 5)
        Displayer.display(maze, DisplayType.ASCII)

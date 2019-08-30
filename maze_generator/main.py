from maze_generator.Maze.maze import Maze
from maze_generator.displayer.display_type import DisplayType
from maze_generator.displayer.displayer import Displayer


class MainMazeGenerator:

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self):
        print("Todo")

    if __name__ == '__main__':
        maze = Maze(90, 15, step_by_step=True)
        maze.display(DisplayType.ASCII)

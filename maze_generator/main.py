#!/usr/local/bin/python3
from maze_generator.Maze.maze import Maze
from maze_generator.Maze.maze_grid import MazeGrid
from maze_generator.displayer.display_type import DisplayType


class MainMazeGenerator:

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self):
        print("Todo")

    if __name__ == '__main__':
        maze = Maze(MazeGrid(40, 40), step_by_step=False)
        maze.resolve()
        maze.display(DisplayType.TKINTER)


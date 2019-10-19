#!/usr/local/bin/python3
from maze_generator.Maze.maze import Maze
from maze_generator.Maze.maze_grid import MazeGrid
from maze_generator.displayer.display_type import DisplayType
from maze_generator.displayer.displayer import Displayer
import sys  
import time

class MainMazeGenerator:

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self):
        print("Todo")

    def create_maze(self, width: int, height: int) -> Maze:
        maze = Maze(MazeGrid(width=width, height=height), step_by_step=False)
        maze.display(DisplayType.TKINTER)
        return maze
    
    def resolve(self, maze: Maze):
        maze.resolve()
        maze.display(DisplayType.TKINTER)

    def start(self):
        maze = self.create_maze(width=40, height=40)
        maze.display(DisplayType.TKINTER)
        self.resolve(maze)

    def init(self):
        sys.setrecursionlimit(10**6)
        Displayer.init(self.start)

if __name__ == '__main__':
    MainMazeGenerator().init()
        


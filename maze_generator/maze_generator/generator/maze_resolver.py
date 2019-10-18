from maze_generator.Maze.maze_grid import MazeGrid

# ------------------------------------------------------------------------------
# Resolve maze grid
# ------------------------------------------------------------------------------


class MazeResolver:
    
    # --------------------------------------------------------------------------
    # Step Action
    # --------------------------------------------------------------------------
    
    def __init__(self, step_action=None):
        self._step_action = step_action

    # --------------------------------------------------------------------------
    # Resolver
    # --------------------------------------------------------------------------

    def resolve(self, grid: MazeGrid):
        print("Start resolve")
    

from maze_generator.Maze.maze_grid import MazeGrid

# ------------------------------------------------------------------------------
# Resolve maze grid
# ------------------------------------------------------------------------------


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
        self.resolve_brutforce()

    def resolve_brutforce(self):
        print("bruteforce")

    


class Coordinate:
    """
    A representation of coordinate x and y.
    """

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + self.x.__str__() + ", y: " + self.y.__str__()

    def is_valid(self, max_x: int, max_y: int) -> bool:
        return 0 <= self.x < max_x \
               and 0 <= self.y < max_y



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

    def is_valid(self, maxX: int, maxY: int) -> bool:
        return 0 <= self.x < maxX \
               and 0 <= self.y < maxY


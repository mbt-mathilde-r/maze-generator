
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
        print("x: " + self.x.__str__() + ", y: " + self.y.__str__())

    def is_valid(self, maxX: int, maxY: int) -> bool:
        return 0 <= self.x < maxX \
               and 0 <= self.y < maxY


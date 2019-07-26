
class Coordinate:
    """
    A representation of coordinate x and y.
    """

    # --------------------------------------------------------------------------
    # Properties
    # --------------------------------------------------------------------------

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    # --------------------------------------------------------------------------
    # Initialization
    # --------------------------------------------------------------------------

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def isValid(self, maxX: int, maxY: int) -> bool:
        return 0 <= self._x < maxX \
               and 0 <= self._y < maxY

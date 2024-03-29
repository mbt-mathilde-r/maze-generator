from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.direction_type import DirectionType
from maze_generator.Maze.maze_grid import MazeGrid


class AsciiDisplayer:

    @staticmethod
    def display(maze: MazeGrid):
        result = AsciiDisplayer.create_string(maze)
        print(result)

    @staticmethod
    def create_string(maze: MazeGrid) -> str:
        height = maze.height
        width = maze.width

        rows = []
        header_row = ['╔']
        for x in range(width - 1):
            header_row.append(AsciiDisplayer.__get_top_character(maze, x))
            header_row.append(AsciiDisplayer.__get_top_cross_character(maze, x))
        header_row.append("═╗")

        rows.append(''.join(header_row))
        for y in range(height):
            character = AsciiDisplayer.__get_leading_character(maze, y)
            row = [character]
            for x in range(width):
                row.append(AsciiDisplayer.__get_cell_character(maze, x, y))
                row.append(AsciiDisplayer.__get_next_east_wall_character(maze, x, y))
            rows.append(''.join(row))

            row = [AsciiDisplayer.__get_leading_cross_character(maze, y)]
            for x in range(width):
                row.append(AsciiDisplayer.__get_next_south_wall_character(maze,
                                                                     x,
                                                                     y))
                row.append(AsciiDisplayer.__get_cross_character(maze, x, y))

            rows.append(''.join(row))

        footer_row = ['╚']
        for x in range(width - 1):
            footer_row.append(AsciiDisplayer.__get_bottom_character(maze, x))
            footer_row.append(AsciiDisplayer.__get_bottom_cross_character(maze, x))
        footer_row.append('═╝')

        row_length = len(rows)
        rows[row_length - 1] = ''.join(footer_row)
        result = '\n'.join(rows)
        return result

    @staticmethod
    def __get_cross_character(grid: MazeGrid, x: int, y: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=y))
        south = grid.get_cell_neighbour(me, DirectionType.SOUTH)
        east = grid.get_cell_neighbour(me, DirectionType.EAST)

        north_wall = not me.is_direction_open(DirectionType.EAST) \
            if me is not None else False
        east_wall = not east.is_direction_open(DirectionType.SOUTH) \
            if east is not None else False
        south_wall = not south.is_direction_open(DirectionType.EAST) \
            if south is not None else False
        west_wall = not me.is_direction_open(DirectionType.SOUTH) \
            if me is not None else False
        return AsciiDisplayer.__cross_walls_to_character(north_wall=north_wall,
                                                    south_wall=south_wall,
                                                    east_wall=east_wall,
                                                    west_wall=west_wall)

    @staticmethod
    def __get_cell_character(grid: MazeGrid, x: int, y: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=y))
        if me.isStart:
            return "\033[92m░\033[0m"
        if me.isEnd:
            return "\033[95m░\033[0m"
        if me.isInvalid:
            return "\033[94m░\033[0m"
        if me.isVisited:
            return "\033[93m░\033[0m"
        return " "

    @staticmethod
    def __get_top_cross_character(grid: MazeGrid, x: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=0))
        return "═" if me.is_direction_open(DirectionType.EAST) else "╦"

    @staticmethod
    def __get_top_character(grid: MazeGrid, x: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=0))
        return " " if me.is_direction_open(DirectionType.NORTH) else "═"

    @staticmethod
    def __get_bottom_character(grid: MazeGrid, x: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=grid.height - 1))
        return " " if me.is_direction_open(DirectionType.SOUTH) else "═"

    @staticmethod
    def __get_bottom_cross_character(grid: MazeGrid, x: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=grid.height - 1))
        return "═" if me.is_direction_open(DirectionType.EAST) else "╩"

    @staticmethod
    def __get_leading_cross_character(grid: MazeGrid, y: int) -> str:
        me = grid.get_cell(Coordinate(x=0, y=y))
        return '║' if me.is_direction_open(DirectionType.SOUTH) else '╠'

    @staticmethod
    def __get_leading_character(grid: MazeGrid, y: int) -> str:
        me = grid.get_cell(Coordinate(x=0, y=y))
        return ' ' if me.is_direction_open(DirectionType.WEST) else '║'

    @staticmethod
    def __get_next_east_wall_character(grid: MazeGrid, x: int, y: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=y))
        return ' ' if me.is_direction_open(DirectionType.EAST) else '║'

    @staticmethod
    def __get_next_south_wall_character(grid: MazeGrid, x: int, y: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=y))
        return ' ' if me.is_direction_open(DirectionType.SOUTH) else '═'

    @staticmethod
    def __cross_walls_to_character(north_wall: bool, south_wall: bool,
                                   east_wall: bool, west_wall: bool) -> str:
        if north_wall and east_wall and south_wall and west_wall:
            return '╬'
        elif north_wall and east_wall and south_wall:
            return '╠'
        elif north_wall and west_wall and south_wall:
            return '╣'
        elif north_wall and east_wall and west_wall:
            return '╩'
        elif south_wall and east_wall and west_wall:
            return '╦'
        elif west_wall and south_wall:
            return '╗'
        elif west_wall and north_wall:
            return '╝'
        elif north_wall and east_wall:
            return '╚'
        elif south_wall and east_wall:
            return '╔'
        elif north_wall and south_wall:
            return '║'
        elif east_wall and west_wall:
            return '═'
        elif north_wall or south_wall:
            return '║'
        elif east_wall or west_wall:
            return '═'
        return ' '

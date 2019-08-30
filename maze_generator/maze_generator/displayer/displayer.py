from maze_generator.Maze.coordinate import Coordinate
from maze_generator.Maze.maze_grid import MazeGrid
from maze_generator.Maze.direction_type import DirectionType
from maze_generator.displayer.display_type import DisplayType

class Displayer:

    @staticmethod
    def display(maze: MazeGrid, display_type: DisplayType):
        if display_type == DisplayType.ASCII:
            Displayer.__display_as_ascii(maze)

    @staticmethod
    def __display_as_ascii(maze: MazeGrid):
        height = maze.height
        width = maze.width

        rows = []
        header_row = ['╔']
        for x in range(width - 1):
            header_row.append('═')
            header_row.append(Displayer.__get_header_character(maze, x))
        header_row.append("═╗")

        rows.append(''.join(header_row))
        for y in range(height):
            row = ['║']
            for x in range(width):
                cell = maze.get_cell(Coordinate(x, y))
                # Cell
                if cell.isVisited:
                    row.append("\033[92m░\033[0m")
                else:
                    row.append(" ")
                # Wall
                if cell.is_direction_open(DirectionType.EAST):
                    row.append(' ')
                else:
                    row.append('║')
            rows.append(''.join(row))

            row = ['║']
            for x in range(width):
                coord = Coordinate(x, y)
                cell = maze.get_cell(coord)
                # Wall
                if cell.is_direction_open(DirectionType.SOUTH):
                    row.append(' ')
                else:
                    row.append('═')

                character = Displayer.__get_cross_character(maze, coord)
                row.append(character)

            rows.append(''.join(row))

        footer_row = ['╚']
        for x in range(width - 1):
            footer_row.append('═')
            footer_row.append(Displayer.__get_footer_character(maze, x))
        footer_row.append('═╝')

        row_length = len(rows)
        rows[row_length - 1] = ''.join(footer_row)
        result = '\n'.join(rows)
        print(result)

    @staticmethod
    def __get_cross_character(grid: MazeGrid, coordinate: Coordinate)\
                -> str:
        me = grid.get_cell(coordinate)
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
        return Displayer.__walls_to_character(north_wall=north_wall,
                                              south_wall=south_wall,
                                              east_wall=east_wall,
                                              west_wall=west_wall)

    @staticmethod
    def __get_header_character(grid: MazeGrid, x: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=0))

        south_wall = not me.is_direction_open(DirectionType.EAST) \
            if me is not None else False

        return Displayer.__walls_to_character(north_wall=False,
                                              south_wall=south_wall,
                                              east_wall=True,
                                              west_wall=True)

    @staticmethod
    def __get_footer_character(grid: MazeGrid, x: int) -> str:
        me = grid.get_cell(Coordinate(x=x, y=grid.height - 1))

        north_wall = not me.is_direction_open(DirectionType.EAST) \
            if me is not None else False

        return Displayer.__walls_to_character(north_wall=north_wall,
                                              south_wall=False,
                                              east_wall=True,
                                              west_wall=True)

    @staticmethod
    def __walls_to_character(north_wall: bool, south_wall: bool, east_wall:
    bool, west_wall: bool) -> str:
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
        return 'x'





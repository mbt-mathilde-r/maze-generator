from maze_generator.Maze.maze import Maze
from maze_generator.Maze.direction_type import DirectionType
from maze_generator.displayer.display_type import DisplayType


class Displayer:

    @staticmethod
    def display(maze: Maze, display_type: DisplayType):
        if display_type == DisplayType.ASCII:
            Displayer.__display_as_ascii(maze)

    @staticmethod
    def __display_as_ascii(maze: Maze):
        height = maze.height
        width = maze.width
        rows = [' ' + '_ ' * width]

        for y in range(height):
            row = ['|']
            for x in range(width):
                if maze[x][y].is_direction_open(DirectionType.EAST):
                    row.append('  ')
                else:
                    row.append(' |')
            rows.append(''.join(row))

            row = ['|']
            for x in range(width):
                if maze[x][y].is_direction_open(DirectionType.SOUTH):
                    row.append(' +')
                else:
                    row.append('-+')
            rowLength = len(row)
            row[rowLength-1] = '-|'
            rows.append(''.join(row))
        rowsLength = len(rows)
        rows[rowsLength - 1] = ''.join([' ' + '- ' * width])
        result = '\n'.join(rows)
        print(result)

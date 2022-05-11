from typing import List, Tuple

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class Maze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string,
            where rows are separated by newlines (\n).

        Raises:
            ValueError, if maze_str is invalid, i.e. if it is not the correct type,
            if any of its dimensions is less than three, or if it contains
            characters besides {'\n', ' ', '*'}.
        """
        # We internally treat this as a List[List[str]], as it makes indexing easier.

        if not isinstance(maze_str, str):
            raise ValueError('Maze_str is not a string')

        if len(maze_str) < 9:
            raise ValueError('Dimension of maze is less than three!')

        if all(ch in ('\n', ' ', '*') for ch in maze_str):
            raise ValueError('String contains characters that are not allowed!')

        self._maze = list(list(row) for row in maze_str.splitlines())

        self._exits: List[Tuple[int, int]] = []
        self._max_recursion_depth = 0

        self.max_row = len(self._maze) - 1
        self.max_col = len(self._maze[0]) - 1

        self.traversed: List[Tuple[int, int]] = []

        self.init = 0

    def find_exits(self, start_row: int, start_col: int, depth: int = 0) -> bool:
        """Find and save all exits into `self._exits` using recursion, save
        the maximum recursion depth into 'self._max_recursion_depth' and mark the maze.

        An exit is an accessible from S empty cell on the outer rims of the maze.

        Args:
            start_row (int): row to start from. 0 represents the topmost cell.
            start_col (int): column to start from; 0 represents the left-most cell.
            depth (int): Depth of current iteration.

        Raises:
            ValueError: If the starting position is out of range or not walkable path.
        """
        maze = self._maze
        self._max_recursion_depth = depth

        if self.init == 0:
            maze[start_row][start_col] = 'S'
            self.init = 1

        if (start_row == 0 or start_row == self.max_row) and (maze[start_row][start_col] == ' '):
            maze[start_row][start_col] = 'X'
            self._exits.append((start_row, start_col))

        if (start_col == 0 or start_col == self.max_col) and (maze[start_row][start_col] == ' '):
            maze[start_row][start_col] = 'X'
            self._exits.append((start_row, start_col))

        if maze[start_row][start_col] == ' ':
            maze[start_row][start_col] = '.'

        neighbour_list = self.get_neighbours(start_row, start_col)

        final_neighbour_list = []

        for cords in neighbour_list:
            if cords == ['N', 'N']:
                continue
            if not maze[cords[0]][cords[1]] == '#' and not maze[cords[0]][cords[1]] == 'X':
                if not self.traversed.count((cords[0], cords[1])) > 1:
                    final_neighbour_list.append(cords)

        if len(final_neighbour_list) == 0:
            return True

        for k in final_neighbour_list:

            if (k[0] == 0 or k[0] == self.max_row) and (maze[k[0]][k[1]] == ' '):
                maze[k[0]][k[1]] = 'X'
                self._exits.append((k[0], k[1]))

            if (k[1] == 0 or k[1] == self.max_col) and (maze[k[0]][k[1]] == ' '):
                maze[k[0]][k[1]] = 'X'
                self._exits.append((k[0], k[1]))

            if maze[k[0]][k[1]] == ' ':
                maze[k[0]][k[1]] = '.'
                self.traversed.append((k[0], k[1]))
                return self.find_exits(k[0], k[1], depth=depth + 1)
        else:
            self.traversed.append((k[0], k[1]))
            return self.find_exits(k[0], k[1], depth=depth + 1)

    def get_neighbours(self, row: int, col: int):
        # List = [ROW, COL]

        right = ['N', 'N']
        left = ['N', 'N']
        top = ['N', 'N']
        bottom = ['N', 'N']

        if not col + 1 > self.max_col:
            right = [row, col + 1]

        if not col - 1 < 0:
            left = [row, col - 1]

        if not row + 1 > self.max_row:
            bottom = [row + 1, col]

        if not row - 1 < 0:
            top = [row - 1, col]

        return right, left, top, bottom

    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__

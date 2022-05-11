from typing import List, Tuple

maze_str = "## ###\n" \
           "#    #\n" \
           "## # #\n" \
           "#  #  \n" \
           "  ## #\n" \
           "#### #"

maze = list(list(row) for row in maze_str.splitlines())
max_row = len(maze) - 1
max_col = len(maze[0]) - 1
init = 0
print(maze)
depth = 0
traversed: List[Tuple[int, int]] = []

def find_exits(start_row: int, start_col: int, sent):
    global init
    global depth

    if depth > 900:
        return True
    depth += 1

    if init == 0:
        if maze[start_row][start_col] == '#':
            raise ValueError('Starting position is not walkable path')
        maze[start_row][start_col] = 'S'
        init = 1

    if (start_row == 0 or start_row == max_row) and (maze[start_row][start_col] == ' '):
        maze[start_row][start_col] = 'X'

    if (start_col == 0 or start_col == max_col) and (maze[start_row][start_col] == ' '):
        maze[start_row][start_col] = 'X'

    neighbour_list = get_neighbours(start_row, start_col)

    final_neighbour_list = []

    for cords in neighbour_list:
        if cords == ['N', 'N']:
            continue
        else:
            final_neighbour_list.append(cords)
    print(f' {start_row, start_col} {final_neighbour_list} {sent}')

    if maze[start_row][start_col] == ' ':
        maze[start_row][start_col] = '.'

    if not start_col + 1 > max_col:
        if len(final_neighbour_list) > 0:
            find_exits(final_neighbour_list[0][0], final_neighbour_list[0][1], 0)
        if maze[start_row][start_col + 1] != '#':
            find_exits(start_row, start_col + 1, 1)

    if not start_col - 1 < 0:
        if len(final_neighbour_list) > 0:
            find_exits(final_neighbour_list[0][0], final_neighbour_list[0][1], 2)
        if maze[start_row][start_col - 1] != '#':
            find_exits(start_row, start_col - 1, 3)

    if not start_row + 1 > max_row:
        if len(final_neighbour_list) > 0:
            find_exits(final_neighbour_list[0][0], final_neighbour_list[0][1], 4)
        if maze[start_row + 1][start_col] != '#':
            find_exits(start_row + 1, start_col, 5)

    if not start_row - 1 < 0:
        if len(final_neighbour_list) > 0:
            find_exits(final_neighbour_list[0][0], final_neighbour_list[0][1], 6)
        if maze[start_row - 1][start_col] != '#':
            find_exits(start_row - 1, start_col, 7)

def get_neighbours(row: int, col: int):
    # List = [ROW, COL]

    right = ['N', 'N']
    left = ['N', 'N']
    top = ['N', 'N']
    bottom = ['N', 'N']

    if not col + 1 > max_col:
        if maze[row][col + 1] == ' ':
            right = [row, col + 1]

    if not col - 1 < 0:
        if maze[row][col - 1] == ' ':
            left = [row, col - 1]

    if not row + 1 > max_row:
        if maze[row + 1][col] == ' ':
            bottom = [row + 1, col]

    if not row - 1 < 0:
        if maze[row - 1][col] == ' ':
            top = [row - 1, col]

    return right, left, top, bottom


find_exits(1, 1, -1)
print(maze)
"""
['#', '#', ' ', '#', '#', '#'], 
['#', 'S', '.', '.', '.', '#'] 
['#', '#', ' ', '#', '.', '#'], 
['#', ' ', ' ', '#', '.', 'X'], 
[' ', ' ', '#', '#', '.', '#'], 
['#', '#', '#', '#', 'X', '#']
"""

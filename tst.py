"""maze_str = "### ##\n" \
           "##M  #\n" \
           "      \n" \
           "# ## #\n" \
           "#### #"""

from typing import List, Tuple

maze_str =  "## ###\n" \
            "#    #\n" \
            "## # #\n" \
            "#  #  \n" \
            "  ## #\n" \
            "#### #"


# maze = maze_str.split('\n')
maze = list(list(row) for row in maze_str.splitlines())
max_row = len(maze) - 1
max_col = len(maze[0]) - 1
print(maze)
init = 0
depth = 0
traversed: List[Tuple[int, int]] = []

def find_exit(start_row, start_col):
    global init
    global depth

    depth += 1

    if depth > 900:
        return True

    if init == 0:
        maze[start_row][start_col] = 'S'
        init = 1

    if (start_row == 0 or start_row == max_row) and (maze[start_row][start_col] == ' '):
        maze[start_row][start_col] = 'X'

    if (start_col == 0 or start_col == max_col) and (maze[start_row][start_col] == ' '):
        maze[start_row][start_col] = 'X'

    if maze[start_row][start_col] == ' ':
        maze[start_row][start_col] = '.'

    neighbour_list = get_neighbours(start_row, start_col)

    final_neighbour_list = []

    for cords in neighbour_list:
        if cords == ['N', 'N']:
            continue
        if not maze[cords[0]][cords[1]] == '#' and not maze[cords[0]][cords[1]] == 'X':
            if traversed.count((cords[0], cords[1])) < 2:
                final_neighbour_list.append(cords)

    if len(final_neighbour_list) == 0:
        return True
    last = []

    for k in final_neighbour_list:
        last.clear()
        last.append(k[0])
        last.append(k[1])
        if (k[0] == 0 or k[0] == max_row) and (maze[k[0]][k[1]] == ' '):
            maze[k[0]][k[1]] = 'X'

        if (k[1] == 0 or k[1] == max_col) and (maze[k[0]][k[1]] == ' '):
            maze[k[0]][k[1]] = 'X'

        if maze[k[0]][k[1]] == ' ':
            maze[k[0]][k[1]] = '.'
            traversed.append((k[0], k[1]))
            print(f' {k[0], k[1]} - exit search')
            return find_exit(k[0], k[1])

    print(last)
    print(final_neighbour_list)


def get_neighbours(row: int, col: int):
    # List = [ROW, COL]

    right = ['N', 'N']
    left = ['N', 'N']
    top = ['N', 'N']
    bottom = ['N', 'N']

    if not col + 1 > max_col:
        right = [row, col + 1]

    if not col - 1 < 0:
        left = [row, col - 1]

    if not row + 1 > max_row:
        bottom = [row + 1, col]

    if not row - 1 < 0:
        top = [row - 1, col]

    return right, left, bottom, top

#lst_nei = get_neighbours(5, 4)

find_exit(1, 1)
print(maze)

""" ['#', '#', ' ', '#', '#', '#'], \
    ['#', ' ', ' ', ' ', ' ', '#'], \
    ['#', '#', ' ', '#', ' ', '#'], \
    ['#', ' ', ' ', '#', ' ', ' '], \
    [' ', ' ', '#', '#', ' ', '#'], \
    ['#', '#', '#', '#', ' ', '#']"""
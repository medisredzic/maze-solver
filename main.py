"""maze_str = "### ##\n" \
           "##M  #\n" \
           "      \n" \
           "# ## #\n" \
           "#### #"""

from typing import List, Tuple

"""maze_str =  "## ###\n" \
            "#    #\n" \
            "## # #\n" \
            "#  #  \n" \
            "  ## #\n" \
            "#### #"""

maze_str = "###############\n"\
        "#             #\n"\
        "############# #\n"\
        "#             #\n"\
        "# #############\n"\
        "#             #\n"\
        "############# #\n"\
        "#             #\n"\
        "# #############\n"\
        "#             #\n"\
        "############# #\n"\
        "############# #\n"\
        "############# #\n"\
        "#             #\n"\
        "###############\n"


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

    if depth > 900:
        return True

    if init == 0:
        maze[start_row][start_col] = 'S'
        init = 1

    if (start_row == 0 or start_row == max_row) and (maze[start_row][start_col] == ' '):
        maze[start_row][start_col] = 'X'
        #self._exits.append((start_row, start_col))

    if (start_col == 0 or start_col == max_col) and (maze[start_row][start_col] == ' '):
        maze[start_row][start_col] = 'X'
        #self._exits.append((start_row, start_col))

    if maze[start_row][start_col] == ' ':
        maze[start_row][start_col] = '.'

    neighbour_list = get_neighbours(start_row, start_col)

    final_neighbour_list = []

    for cords in neighbour_list:
        if cords == ['N', 'N']:
            continue
        if not maze[cords[0]][cords[1]] == '#' and not maze[cords[0]][cords[1]] == 'X':
            if not traversed.count((cords[0], cords[1])) > 1:
                final_neighbour_list.append(cords)

    if len(final_neighbour_list) == 0:
        return True
    depth += 1
    for k in final_neighbour_list:

        if (k[0] == 0 or k[0] == max_row) and (maze[k[0]][k[1]] == ' '):
            maze[k[0]][k[1]] = 'X'
            #self._exits.append((k[0], k[1]))

        if (k[1] == 0 or k[1] == max_col) and (maze[k[0]][k[1]] == ' '):
            maze[k[0]][k[1]] = 'X'
            #self._exits.append((k[0], k[1]))

        if maze[k[0]][k[1]] == ' ':
            maze[k[0]][k[1]] = '.'
            traversed.append((k[0], k[1]))
            return find_exit(k[0], k[1])
    else:
        if maze[k[0]][k[1]] == '.':
            return True
        else:
            traversed.append((k[0], k[1]))
            return find_exit(k[0], k[1])

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

    return right, left, top, bottom

lst_nei = get_neighbours(5, 4)
print(lst_nei)
find_exit(1, 1)
print(maze)
""" ['#', '#', ' ', '#', '#', '#'], \
    ['#', ' ', ' ', ' ', ' ', '#'], \
    ['#', '#', ' ', '#', ' ', '#'], \
    ['#', ' ', ' ', '#', ' ', ' '], \
    [' ', ' ', '#', '#', ' ', '#'], \
    ['#', '#', '#', '#', ' ', '#']"""

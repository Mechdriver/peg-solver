from copy import deepcopy

STARTING_PEGS = 14
BOARD_SIZE = 5

class Triangle:
    def __init__(self, size):
        self.board = []
        for i in range(0, size):
            row = []
            for j in range(0, i + 1):
                row.append(1)
            self.board.append(row)

    def set_start_position(self, start_pos):
        self.empties = [start_pos]
        self.board[start_pos[0]][start_pos[1]] = 0

def print_board(board):
    spaces = len(board)
    extra_spaces = spaces + 2
    filler = ' ' * extra_spaces
    print (filler + '^')
    for i in range(0, len(board)):
        filler = ' ' * spaces
        print(filler + '/', end=' ')
        for j in range(0, len(board[i])):
            print (str(board[i][j]), end=' ')
        print('\\')
        spaces -= 1
    bottom = '-' * 13
    print(' ' + bottom)

def is_movable_peg(triangle, pos, mid):
    if (0 <= pos[0] < len(triangle.board) and
        0 <= pos[1] < len(triangle.board[pos[0]]) and
        0 <= mid[0] < len(triangle.board) and
        0 <= mid[1] < len(triangle.board[mid[0]])):

        if (triangle.board[pos[0]][pos[1]] and triangle.board[mid[0]][mid[1]]):
            return True

def process_move(triangle, moves, orig, pos, mid, peg_count):
    row = orig[0]
    col = orig[1]
    next_triangle = deepcopy(triangle)

    next_triangle.board[row][col] = 'X'
    next_triangle.board[pos[0]][pos[1]] = 'P'
    next_triangle.board[mid[0]][mid[1]] = 'J'

    next_triangle.empties.remove(orig)
    next_triangle.empties.append(pos)
    next_triangle.empties.append(mid)

    new_moves = list(moves)
    new_moves.append(deepcopy(next_triangle.board))

    next_triangle.board[row][col] = 1
    next_triangle.board[pos[0]][pos[1]] = 0
    next_triangle.board[mid[0]][mid[1]] = 0

    return solve_board(next_triangle, new_moves, peg_count - 1)

def solve_board(triangle, moves, peg_count):
    if (peg_count == 1):
        moves.append(triangle.board)
        return moves

    for orig in triangle.empties:
        row = orig[0]
        col = orig[1]

        pos = (row - 2, col)
        mid = (row - 1, col)
        if (is_movable_peg(triangle, pos, mid)):
            res = process_move(triangle, moves, orig, pos, mid, peg_count)
            if (res):
                return res

        pos = (row + 2, col)
        mid = (row + 1, col)
        if (is_movable_peg(triangle, pos, mid)):
            res = process_move(triangle, moves, orig, pos, mid, peg_count)
            if (res):
                return res

        pos = (row + 2, col + 2)
        mid = (row + 1, col + 1)
        if (is_movable_peg(triangle, pos, mid)):
            res = process_move(triangle, moves, orig, pos, mid, peg_count)
            if (res):
                return res

        pos = (row - 2, col - 2)
        mid = (row - 1, col - 1)
        if (is_movable_peg(triangle, pos, mid)):
            res = process_move(triangle, moves, orig, pos, mid, peg_count)
            if (res):
                return res

        pos = (row, col + 2)
        mid = (row, col + 1)
        if (is_movable_peg(triangle, pos, mid)):
            res = process_move(triangle, moves, orig, pos, mid, peg_count)
            if (res):
                return res

        pos = (row, col - 2)
        mid = (row, col - 1)
        if (is_movable_peg(triangle, pos, mid)):
            res = process_move(triangle, moves, orig, pos, mid, peg_count)
            if (res):
                return res

    return False

valid = 0
triangle = Triangle(BOARD_SIZE)
print_board(triangle.board)
print("Hi! I can solve the peg puzzle for you.")
print("Enter the co-ordinates of the empty space. Example: 0 0")

while not valid:
    start_pos = input()
    start_pos = start_pos.split(' ')
    start_pos = (int(start_pos[0]), int(start_pos[1]))

    triangle = Triangle(BOARD_SIZE)

    if (0 <= start_pos[0] < len(triangle.board) and
        0 <= start_pos[1] < len(triangle.board[start_pos[0]])):

        triangle.set_start_position(start_pos)
        print("Great! Is this the board that you want?")
        print_board(triangle.board)
        print("Yes or no?")
        ans = input()
        if (ans.lower() == 'yes'):
            valid = 1
        else:
            print("Enter the co-ordinates of the starting space. Example: 0 0")
    else:
        print("Oops! You can't start there. Try again. Example: 2 1")

print("I'm thinking...")
moves = solve_board(triangle, [], STARTING_PEGS)
print("Ok! Follow along!")
print("'P' is the Peg that you move.")
print("'J' is the peg that you Jump!")
print("'X' marks the spot you end up.")
for i in range(0, len(moves) - 1):
    print_board(moves[i])
    input("Press Enter for the next move...")

print("And that's all there is to it!")
print("Your board should look like this:")
print_board(moves[len(moves) - 1])
print("You're welcome!")

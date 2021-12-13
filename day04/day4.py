file = open("input.txt", "r")

file_lines = list(file)
revealed_numbers = [int(x) for x in file_lines[0].split(',')]

def has_won(board):
    for i in range(5):
        line = sum(board[i])
        if line == -5: return True

        column = board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i]
        if column == -5: return True

    return False

def mark_number(board, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = -1

def board_value(board):
    total = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                total += board[i][j]

    return total

boards = []

board_numbers_lines = [x for x in file_lines[1:] if x != '\n']

i = 0
while i < len(board_numbers_lines):
    new_board = []
    for j in range(5):
        line_values = [int(x) for x in board_numbers_lines[i+j].split()]
        new_board.append(line_values)

    boards.append(new_board)
    i += 5

def answer1():
    for revealed_number in revealed_numbers:
        for board in boards:
            mark_number(board, revealed_number)
            if has_won(board):
                return revealed_number * board_value(board)

def answer2():
    winners_count = 0
    for revealed_number in revealed_numbers:
        for board in boards:
            if has_won(board):
                continue

            mark_number(board, revealed_number)
            if has_won(board):
                winners_count += 1

                if winners_count == len(boards):
                    return revealed_number * board_value(board)


# print(answer1())
print(answer2())


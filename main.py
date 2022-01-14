"""
functions related to creating, printing,
and evaluating tic-tac-toe boards

:author: Hope Crisafi
:note: I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.
"""


def remove_blank_lines(list_of_strings):
    """
    Given a list of strings, return a copy
    with all empty strings removed
    :param list_of_strings: list of strings, some of which may be ''; this list is unchanged
    :return: list identical to list_of_strings, but all empty strings removed
    """
    result = list()
    for s in list_of_strings:
        if s != '':
            result.append(s)
    return result


def get_board_from_file(filename):
    """
    Reads board, returns a list of rows.
    :param filename: text file with a tic-tac-toe board such as
    X X X
    O X O
    X O O
    where each line is one row
    :return: list of strings where each string is a
    row from filename; any blank lines in the file are removed
    Example: ["X X X", "O X O", "X O O"]
    """
    board_list = []
    board_file = open(filename, "r")
    for line in board_file:
        board_list.append(line.strip())
    board_file.close()
    board_list = remove_blank_lines(board_list)
    return board_list


def print_row(row):
    """
    Nicely prints a row of the board.
    :param row: string of Xs and Os
    """
    nice_row = ''
    for i in range(0, len(row)):
        nice_row += row[i]
        if i != len(row) - 1:
            nice_row += ' | '
    print(nice_row)


def print_board(board):
    """
    prints the tic-tac-toe board
    :param board: list of rows
    """
    for i in range(0, len(board)):
        row = board[i]
        print_row(row)
        if i != len(board) - 1:
            print('----------')


def three_in_row(board, player, start_x, start_y, dx, dy):
    """
    Determines if a player has three in a row, starting
    from a starting position (start_x, start_y) and going
    in the direction indicated by (dx, dy). Example:
    (start_x, start_y) = (2,2) means we start at the lower
    right (row 2, col 2). (dx, dy) = (-1, 0) means the next
    square we check is (2+dx, 2+dy) = (1,2).  And the last
    square we check is (1+dx, 2+dy) = (0,2).  So we've just
    checked the rightmost column - (2,2), (1,2), and (0,2).
    :param board: list of rows
    :param player: string -- either "X" or "O"
    :param start_x: row to start checking at; first row is row 0
    :param start_y: col to start checking at; first col is col 0
    :param dx: 1 if checking downward, -1 if checking upward, 0 if checking this row
    :param dy: 1 if checking rightward, -1 if checking leftward, 0 if checking this col
    """
    x = start_x
    y = start_y
    for i in range(0, 3):
        if board[x][y] != player:
            return False
        x += dx
        y += dy
    return True


def is_winner(board, player):
    """
    Returns True if and only if the given player has won.
    :param board: list of row strings
    :param player: string - "X" or "O"
    :return: True if player won; False if player lost or tied
    """
    if three_in_row(board, player, 0, 0, 1, 1):
        return True
    else:
        for i in range(0, 3):
            if (three_in_row(board, player, 0, i, 1, 0)
                    or three_in_row(board, player, i, 0, 0, 1)):
                return True
        return False


def get_winner(board):
    """
    Returns the name of the winner, or None if there is no winner
    :param board: list of row strings
    :return: "X" if X is winner, "O" if O is winner, None if tie
    """
    if is_winner(board, 'X'):
        return 'X'
    elif is_winner(board, 'O'):
        return 'O'
    #problem is this function will always return else
    else:
        return None


def confirm_result2(board, expected_winner): #expected winner is x, o, or none
    """
    Compares the actual winner and what the function get_winner
    thinks the winner should be
    :param board: a game board
    :param expected_winner: X or O
    :return: who the correct winner is
    """
    computer_winner = get_winner(board)
    #print('confirming result')
    if computer_winner == expected_winner:
        return print("PASS")
    else:
        print_board(board)
        return print("FAIL")


def confirm_result(board, expect_winner):
    """
    compares expected and actual result
    :param board: a game board
    :param expect_winner: X or O
    :return: X if winner, or O if winner
    """
    #print(get_winner(board))
    #print(expect_winner)
    if get_winner(board) == expect_winner:
        return print('pass')
    else:
        print(board)
        print('expected result: {}'.format(expect_winner))
        return print('fail')


def main():
    """
    uses all of the functions together to determine a tic tac toe winner
    :return: game results
    """
    board = get_board_from_file("tie.txt")
    winner = confirm_result(board, "tie")


def main2():
    """
    uses all of the functions together to determine a tic tac toe winner, but the board is manually entered
    in the code and more than one board is tested
    :return: all possible game results
    """
    board1 =  ["XXX",
               "OOX",
               "XOO"]
    winner1 = confirm_result(board1, 'X')

    board2 =  ["OXX",
               "XOX",
               "XOO"]
    winner2 = confirm_result(board2, 'O')

    board3 =  ["XOX",
               "OXO",
               "OXO"]
    winner3 = confirm_result(board3, 'tie')


print(main())
print(main2())


if __name__ == "__main__":
    main()


"question: I got the function to work without changing get_winner, is this considered incorrect?" \
"I am not sure why my code keeps returning 'None' at the end of the print statements"
"should the main functions return something"

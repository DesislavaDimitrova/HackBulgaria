import random


new_board = [" "] * 9
human = ""
AI = ""
winning_moves = ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6))


def choose_sign(human, AI):
    human = input("Choose X or O: ")
    if human == "X":
        AI = "O"
    else:
        AI = "X"
    return human, AI


def display_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--- --- ---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--- --- ---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


def determine_winner(new_board, human, AI):
    for row in winning_moves:
        if new_board[row[0]] == new_board[row[1]] == new_board[row[2]] != " ":
            winner = new_board[row[0]]
            if winner == human:
                return 1
            elif winner == AI:
                return 0
    if "" not in new_board:
        return "Tie"
    return None


def human_move(new_board, human):
    while True:
        players_move = int(input("Please choose a number 0-8 for your move:"))
        if new_board[players_move] == ' ':
            return players_move
        else:
            print("You should choose an empty space!")


def AI_move(new_board, human, AI):
    best = [4, 0, 2, 6, 8]
    blank = []
    for i in range(0, 9):
        if new_board[i] == "":
            blank.append(i)
    for i in blank:
        new_board[i] = AI
        if determine_winner(new_board, human, AI) is 0:
            return i
        new_board[i] = ""

    for i in blank:
        new_board[i] = human
        if determine_winner(new_board, human, AI) is 1:
            return i
        new_board[i] = ""
    return int(blank[random.randrange(len(blank))])


def human_starts(new_board, human, AI):
    while determine_winner(new_board, human, AI) is None:
        move = human_move(new_board, human)
        new_board[int(move)] = human
        display_board(new_board)
        oth_move = AI_move(new_board, human, AI)
        new_board[int(oth_move)] = AI
        display_board(new_board)
    return determine_winner(new_board, human, AI)


def main(new_board, human, AI):
    a = choose_sign(human, AI)
    human = a[0]
    AI = a[1]
    display_board(new_board)
    human_starts(new_board, human, AI)

main(new_board, human, AI)

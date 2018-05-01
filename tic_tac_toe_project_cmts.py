from random import randint

def display_board(board):

    print ('     |     |    ')
    print ('  ' + board[1] + '  |' + '  ' + board[2] + '  |' + '  ' + board[3])
    print ('     |     |    ')
    print ('----------------')
    print ('     |     |    ')
    print ('  ' + board[4] + '  |' + '  ' + board[5] + '  |' + '  ' + board[6])
    print ('     |     |    ')
    print ('----------------')
    print ('     |     |    ')
    print ('  ' + board[7] + '  |' + '  ' + board[8] + '  |' + '  ' + board[9])
    print ('     |     |    ')


def player_input():

    player1 = ''

    while not (player1 == 'X' or player1 == 'O'):
        player1 = input('Player 1: Would you like to be "X" or "O"? ').upper()

    if player1 == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark)
           )


def choose_first():
    player = randint(1, 2)
    return 'Player' + str(player)

def space_check(board, position):

    return board[position] == " "

def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position) == True:
        position = int(input("Choose your next position (1-9): "))

    return position

def replay():

    play_again = input("Do you want to play again? Y or N ").upper()

    return play_again == 'Y'

print('Welcome to Tic Tac Toe!')

while True:
    # creates list that holds the positions
    theBoard = [' '] * 10
    # assigns a marker to each player after player1 chooses
    player1_marker, player2_marker = player_input()
    # determines which player will go first
    turn = choose_first()
    print(turn + ' will go first.')

    # get confirmation to start
    play_game = input("Are you ready to play? Enter Yes or No: ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False


    while game_on:
        if turn == 'Player1':
            # player 1's turn
            display_board(theBoard)
            # prompts player to choose a valid position (1-9 and not filled)
            position = player_choice(theBoard)
            # assigns player 1's marker to that position
            place_marker(theBoard, player1_marker, position)

            # checks to see if player 1 has won
            if win_check(theBoard, player1_marker):
                # if player 1 has won, print the board and Congratulations
                # set game_on to false and end the loop
                display_board(theBoard)
                print('Player 1 has won!')
                game_on = False
            # checks to see if the board is full

            else:
                if full_board_check(theBoard):
                    # if the board is full and player 1 hasn't won after their turn,
                    # then it's a draw
                    # breaks out of the loop
                    display_board(theBoard)
                    print('The game is a draw!')
                    game_on = False
                else:
                    # if the board isn't full, then go to player 2's turn
                    turn = 'Player2'
        else:
            # Player 2's turn
            # print the board
            display_board(theBoard)
            # prompt Player 2 to choose a valid position (1-9 and not filled)
            position = player_choice(theBoard)
            # assign player 2's marker to that position
            place_marker(theBoard, player2_marker, position)

            # checks if player 2 has won
            if win_check(theBoard, player2_marker):
                # print the the board
                # set game_on to false and end the loop
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            # if player 2 hasn't won, then check to see if the board is full
            # if the board is full and player 2 hasn't won after their turn,
            # then it's a draw
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    game_on = False
                # if the board isn't full, then set the turn to player1
                else:
                    turn = 'Player1'
# if outside of the loop (either someone has won or there's a draw)
# prompts user to say yes or no to playing again
# if user does not say yes, then breaks out of the first while loop
    if not replay():
        break

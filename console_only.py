# ANPING HE (17685951)  KUAN-PING CHANG(71018021)
import connectfour
import common


def game_UI()->None:
    '''Main function, the user interface'''
    state = common.start_game() # Print and creates the starting state
    while True:
        common.print_turn(state)
        while True:
            INPUT = common.piece_input()
            if INPUT[0] == 'DROP': # Dropping a piece
                try:
                    state = connectfour.drop_piece(state, INPUT[1])
                    break
                except connectfour.InvalidMoveError:
                    print('Sorry, your move is invalid. Please try again.')
                except connectfour.GameOverError:
                    print('Sorry, the game is already over.')
            elif INPUT[0] == 'POP': # Popping a piece
                try:
                    state = connectfour.pop_piece(state, INPUT[1])
                    break
                except connectfour.InvalidMoveError:
                    print('Sorry, your move is invalid. Please try again.')
                except connectfour.GameOverError:
                    print('Sorry, the game is already over.')
        print()
        common.print_board(state.board)
        if common.decide_over(state) == True:
            # Print out the winner and stop the game if
            # there is a winner, continue otherwise.
            break

if __name__ == '__main__':
    game_UI()

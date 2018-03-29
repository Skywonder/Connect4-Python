# ANPING HE (17685951)  KUAN-PING CHANG(71018021)

import connectfour


def print_board(l:list)->None:
    '''
    prints out the game board in a human readable format
    '''
    result = ''
    result += '1  2  3  4  5  6  7\n'
    for x in range(connectfour.BOARD_ROWS):
        for c in l:
            if c[x] == connectfour.NONE:
                result += '.  '
            elif c[x] == connectfour.RED:
                result += 'R  '
            elif c[x] == connectfour.YELLOW:
                result += 'Y  '
        result += '\n'
    print(result)
    return

def start_game()->connectfour.ConnectFourGameState:
    '''print an empty play board and create the starting state'''
    state = connectfour.new_game_state()
    print('Welcome to ConnectFour!')
    print_board(state.board)
    return state
    
def piece_input()->list:
    '''Prompt the user for input, checking validity and return the value
    as a list'''
    while True:
        a = input('Please type your move (DROP or POP): ')
        if a.strip().upper() in ('DROP','POP'):
            while True:
                try:
                    b = int(input('Please enter the column number (1-7): '))
                    if (b>0) and (b<8):
                        # The index number in this step is corrected for
                        # zero indexing.
                        return [a.strip().upper(),b-1]
                    else:
                        print('Error! Please enter an number between 1-7.')
                except:
                    print('Error! Please enter an number between 1-7.')
                
        else:
            print('Error! The move you entered is not valid. Please choose from DROP or POP.')

def print_turn(state: connectfour.ConnectFourGameState)->None:
    '''take as input the state and prints out the player's turn'''
    if state.turn == connectfour.RED:
        print('Now it is Red\'s turn')
    elif state.turn == connectfour.YELLOW:
        print('Now it is Yellow\'s turn')
    return

def decide_over(state: connectfour.ConnectFourGameState)->bool:
    '''takes as input the state, and prints out the winner and
    return true if there is one'''
    if connectfour.winning_player(state) == connectfour.YELLOW:
        print('Game Over! The winner is Yellow!')
        return True
    elif connectfour.winning_player(state) == connectfour.RED:
        print('Game Over! The winner is Red!')
        return True
    return False

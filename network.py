# ANPING HE (17685951)  KUAN-PING CHANG(71018021)
import common
import I32CFSP
import connectfour

def get_username()->str:
    '''prompts the user to enter username'''
    while True:
        name = input('Please enter your username (no white spaces): ').strip()
        if len(name.split())>1:
            print('Error! Username cannot contain white spaces. Please try again.')
        else:
            return name

def initiate_game(con:'Connection',username:'username')->'connection state':
    '''initiating the network game, printing out the starting
    game board, returns None if the intiation process does not
    conform to protocol'''
    username1 = 'I32CFSP_HELLO'+' '+username
    a = I32CFSP.talk(con,username1)
    if a != ['WELCOME',username]:
        return None
    b = I32CFSP.talk(con,'AI_GAME')
    if b!= ['READY']:
        return None
    state = common.start_game()
    return state

def game_UI():
    '''The main game interface'''
    host = I32CFSP.get_host()
    port = I32CFSP.get_port()
    try: # This try statement raises exception when connection failed
        con = I32CFSP.connect(host,port)
        username = get_username()
        state = initiate_game(con,username)
        while True:
            if state == None: # Checks whether the intiation conforms to protocol
                break
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
            if common.decide_over(state) == True: # This decides if the player wins
                # Print out the winner and stop the game if
                # there is a winner, continue otherwise.
                break
            common.print_turn(state)
            print('Please wait...')
            message = INPUT[0]+' '+str(INPUT[1])
            feedback = I32CFSP.talk(con,message)
            if feedback[0] == 'OKAY' and feedback[1] == 'DROP':
                try:
                    state = connectfour.drop_piece(state,int(feedback[2]))
                except ValueError:
                    print('Sorry, the column number is invalid.')
                    break
                except connectfour.InvalidMoveError:
                    print('Sorry, your move is invalid.')
                    break
                except connectfour.GameOverError:
                    print('Sorry, the game is already over.')
                    break
            elif feedback[0] == 'OKAY' and feedback[1] == 'POP':
                try:
                    state = connectfour.pop_piece(state,int(feedback[2]))
                except ValueError:
                    print('Sorry, the column number is invalid.')
                    break
                except connectfour.InvalidMoveError:
                    print('Sorry, your move is invalid.')
                    break
                except connectfour.GameOverError:
                    print('Sorry, the game is already over.')
                    break
            elif feedback[1].upper() not in ('DROP','POP'):
                print('Error! Invalid move.')
                break
            print()
            common.print_board(state.board)
            if common.decide_over(state) == True: # This decides if the server wins
                # Print out the winner and stop the game if
                # there is a winner, continue otherwise.
                break
        I32CFSP.close(con)
    except:
        print('Error! Cannot connect to server.')

if __name__ == '__main__':
    game_UI()









    
    

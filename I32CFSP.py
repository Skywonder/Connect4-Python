# ANPING HE (17685951)  KUAN-PING CHANG(71018021)
import socket

def get_host()->str:
    '''prompts the user for host address, and check for validity'''
    while True:
        result = input('Please enter the host name or address: ').strip()
        if result == '':
            print('Error! Invalid host name or address. Please try again.')
        else:
            return result

def get_port()->int:
    '''prompts the user for port number (0-65535), and returns it'''
    while True:
        try:
            result = int(input('Please enter the port number: ').strip())
            if result >= 0 and result <= 65535:
                return result
            else:
                print('Please enter an integer between 0 and 65535.')
        except:
            print('Please enter an integer between 0 and 65535.')

def connect(host:str, port:int)-> 'A socket connection':
    '''connects to the server, and set up an psudo file'''
    c = socket.socket()
    c.connect((host,port))
    infile = c.makefile('r',newline = '\r\n')
    outfile = c.makefile('w', newline = '\r\n')
    return (c, infile, outfile)

def close(connection:'socket connection')->None:
    '''close the files and connection'''
    c, infile, outfile = connection
    print('Closing connection...')
    infile.close()
    outfile.close()
    c.close()
    print('Connection closed')
    return

def _send(con:'socket connection',s:str)->None:
    '''sends the command to the server'''
    c,infile,outfile = con
    s += '\r\n'
    outfile.write(s)
    outfile.flush()
    return

def _receive(con:'socket connection'):
    '''receives responses from the server'''
    c,infile,outfile = con
    result = infile.readline()[:-1]
    return result    
    
def talk(con:'socket connection',s:str)->list:
    '''sends commands to the server and interpreting the response
    from the server'''
    _send(con,s)
    response = _receive(con)
    response = response.strip().split()
    if response[0] == 'OKAY':
        a = _receive(con).strip().split()
        response.extend(a)
        b = _receive(con).strip().split()
        response.extend(b)
    elif response[0] == 'INVALID':
        _receive(con)
    return response


















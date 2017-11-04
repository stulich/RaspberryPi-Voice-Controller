from socket import *
import directions

# Set server port for the socket
serverPort = 25565

# Create a server socket
serverSocket = socket.socket(AF_INET, SOCK_STREAM)

# "bind" the socket to the localhost and server port.
serverSocket.bind(("", serverPort))

# listen(backlog), where backlog is the maximum number of queued connections
serverSocket.listen(5)

# dictionary of commands that map to functions
commandToFunction = {
    'go': 'directions.goForward()',
    'forward': 'directions.goForward()',
    'go forward': 'directions.goForward()',
    'back': 'directions.goBackward()',
    'turn right': 'directions.turnRight()',
    'right': 'directions.turnRight()',
    'go right': 'directions.turnRight()',
    'turn left': 'directions.turnLeft()',
    'left': 'directions.turnLeft()',
    'go left': 'directions.turnLeft()',
}

try:
    # Accepts a new connection. addr is the address of the incoming connection
    Socket_connection, addr = serverSocket.accept()

    while 1:
        # Data received over the buffer which is string containing command
        direction = Socket_connection.recv(1024)

        # if the command is recognized execute the command
        if commandToFunction.hasKey(direction):
            exec(commandToFunction(direction))

        # else pass
        else:
             pass

#if error occurs
except:
    print('An error has occured')

#closes socket at end
finally:
    serverSocket.close()



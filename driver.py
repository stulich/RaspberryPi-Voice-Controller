from socket import *
import directions
import thread

# Set server port for the socket
serverPort = 25571

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
    'stop':'directions.stop()',
    'full send':'directions.explore()',
    'Explorer':'directions.explore()',
    'explore':'directions.explore()',
}

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# "bind" the socket to the localhost and server port.
serverSocket.bind(("", serverPort))

# listen(backlog), where backlog is the maximum number of queued connections
serverSocket.listen(5)


try:
    print('waiting for new connection')
    # creates new thread to monitor distance in front of the machine
    thread.start_new_thread(directions.start_led_controller)

    #runs loop to constantly monitor for input
    while 1:

        # Accepts a new connection. addr is the address of the incoming connection
        Socket_connection, addr = serverSocket.accept()

        # direction received over the buffer which is string containing command
        direction = Socket_connection.recv(1024)
        direction=direction.decode('utf-8')

        #splices direction to remove encoding
        direction = direction[2:].lstrip(' ')
        print(direction)
        if direction.lower() == 'explore':
            thread.start_new_thread(directions.explore)
        # if the command is recognized execute the command
        if direction in commandToFunction:
            exec(commandToFunction[direction])
        else:
             pass

#if error occurs
except KeyboardInterrupt as c:
    print(c)
    serverSocket.close()
    robot.stop()
    exit()

#closes socket at end
finally:
    serverSocket.close()



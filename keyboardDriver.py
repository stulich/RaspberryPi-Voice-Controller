import curses
import directions as robot

def driver(win):
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected Key:")
    win.nodelay(False)
    while 1:
        try:
            #key=win.getkey()
            key=win.getch()
            win.clear()
            win.addstr("Detected Key:")
            win.addstr(str(key))
            
            if key == 10:
                break
            if key == 32:
                robot.stop()
            if key == 258:
                robot.goBackward()
            if key == 259:
                robot.goForward()
            if key == 260:
                robot.turnLeft()
            if key == 261:
                robot.turnRight()
            if key == 101:
                robot.explore()
        except KeyboardInterrupt as e:
            robot.stop()
            exit()

curses.wrapper(driver)


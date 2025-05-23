import mainScreen
import platform
import screen

#코드 진입(windoe mac 구별별)
def main():
    if platform.system()=="Windows":
        import msvcrt
        screen.setStdscr(msvcrt)
        screen.setPlatform(1)
        mainScreen.main()
    else:
        import curses
        screen.setPlatform(2)
        curses.wrapper(mac)

def mac(stdscr):
    screen.setStdscr(stdscr)
    mainScreen.main()

main()
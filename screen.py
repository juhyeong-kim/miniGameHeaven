import os

max=2
window=1
_platform = 0
stdscr=0

def setStdscr(_stdscr):
    global stdscr
    stdscr = _stdscr

def setPlatform(plat):
    global _platform
    _platform = plat


#화면 지우기
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#커서 이동
def move_cursor_to(x, y):
    print(f"\033[{y};{x}H", end="")  # ANSI 코드 출력


#키 입력 받기(하나만 enterX)
def getKey():
    key=stdscr.getch()
    if _platform==window:
        key=int.from_bytes(key, byteorder='big')
    return chr(key)

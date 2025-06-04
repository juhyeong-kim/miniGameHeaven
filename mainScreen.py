import screen
import Gomoku
import dino_game
# import dino_game
cursor_y = 0
max=4
gameIng = True
menu = [
    ["1. 오목"],
    ["2. 게임2"],
    ["3. 다이노 게임"],
    ["4. 게임3"],
    ["5. 종료"]
]

def on_press():
    global cursor_y, gameIng, max
    key = screen.getKey()  # 키 입력 대기 (1byte 입력받기)
    print("key : ",key)
    # 전역 변수 사용
    if key == 'w':  # W: 위로 이동
        cursor_y = cursor_y-1  # 위쪽 경계값 제한
        if cursor_y<0:
            cursor_y=0
    elif key == 's':  # S: 아래로 이동
        cursor_y = cursor_y+1  # 아래쪽 경계값 제한
        if cursor_y>max:
            cursor_y=max
    elif key == 'l':  # A: 왼쪽으로 이동
        gameIng = False

def mainScreen():
    screen.move_cursor_to(0, 0)
    print("╔═══════════════════════════════════════════════════════════════════════════╗\r")
    print("║                                                                           ║\r")
    print("║      ███╗   ███╗██╗███╗   ██╗██╗ ██████╗  █████╗ ███╗   ███╗███████╗      ║\r")
    print("║      ████╗ ████║██║████╗  ██║██║██╔════╝ ██╔══██╗████╗ ████║██╔════╝      ║\r")
    print("║      ██╔████╔██║██║██╔██╗ ██║██║██║  ███║███████║██╔████╔██║█████╗        ║\r")
    print("║      ██║╚██╔╝██║██║██║╚██╗██║██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝        ║\r")
    print("║      ██║ ╚═╝ ██║██║██║ ╚████║██║╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗      ║\r")
    print("║      ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝      ║\r")
    print("║                                                                           ║\r")
    print("║            ██╗  ██╗███████╗ █████╗ ███╗   ██╗███████╗███╗   ██╗           ║\r")
    print("║            ██║  ██║██╔════╝██╔══██╗████╗  ██║██╔════╝████╗  ██║           ║\r")
    print("║            ███████║█████╗  ███████║██╔██╗ ██║█████╗  ██╔██╗ ██║           ║\r")
    print("║            ██╔══██║██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██║╚██╗██║           ║\r")
    print("║            ██║  ██║███████╗██║  ██║██║ ╚████║███████╗██║ ╚████║           ║\r")
    print("║            ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝           ║\r")
    print("║                                                                           ║\r")
    print("║                                                                           ║\r")
    print("║                                                                           ║\r")
    print("║                          이동 : wasd   │   선택 : l                       ║\r")
    print("║                                                                           ║\r")
    print("║     ┌──────────────────────────────────────────────────────────────┐      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     │                                                              │      ║\r")
    print("║     └──────────────────────────────────────────────────────────────┘      ║\r")
    print("║                                                                           ║\r")
    print("╚═══════════════════════════════════════════════════════════════════════════╝\r")

def showMenu():
    x=32
    y=23
    screen.move_cursor_to(x, y)
    i=0
    for item in menu:
        screen.move_cursor_to(x, y+i)
        if(cursor_y == i):
            print("-->",end="")
        print(menu[i],"   ")
        i=i+1

    
    screen.move_cursor_to(0, 0)



def main():
    global gameIng
    while True:
        while gameIng:
            mainScreen()
            showMenu()
            on_press()
            #screen.clearScreen()
        screen.clearScreen()

        if cursor_y == 0:
            Gomoku.main()
        elif cursor_y == 2:
            dino_game.main()
        elif cursor_y == max:
            exit()

        gameIng=True

#curses.wrapper(main)
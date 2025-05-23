import screen

gameIng = True

def on_press():
    key = screen.getKey() 
    if key == 'w':
        print("w\r")
    elif key == 's':
        print("s\r")
    elif key == 'a':
        print("a\r")
    elif key == 'd':
        print("d\r")
    elif key == 'l':
        print("l\r")
        gameIng=False

def drawScreen():
    screen.move_cursor_to(0, 0)
    print("Hello World!!\r")

def main():
    while gameIng:
        drawScreen()
        on_press()
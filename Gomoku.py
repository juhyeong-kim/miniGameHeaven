import screen
from copy import deepcopy

map1 =[
        ['┌','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┐'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['└','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┘']
    ]

map2 = [[0 for _ in range(29)] for _ in range(29)]
black=1
white=2
dol = black


cursor_x, cursor_y = 1, 1
dolx, doly = 5, 5
gameIng = True
winDolChk=0


class pc:
    map=[]

    # 방어 (defense)
    defenseLevelOne = -1             # 한 칸만 있을 때
    defenseLevelTwo_oneBlock = -5    # 양쪽이 막힌 두 칸
    defenseLevelTwo = -10            # 열린 두 칸(양방)
    defenseLevelTwo_center = -12
    defenseLevelThree_oneBlock = -50 # 양쪽이 막힌 세 칸
    defenseLevelThree = -100         # 열린 세 칸(양방)
    defenseLevelThree_center = -120
    defenseLevelFour_oneBlock = -300 # 막힌 4(즉시 막아야함)
    defenseLevelFour = -500         # 열린 4(즉사, 반드시 막아야함)

    # 공격 (attack)
    attackLevelOne = -1
    attackLevelTwo_oneBlock = -3
    attackLevelTwo = -8
    attackLevelTwo_center = -10
    attackLevelThree_oneBlock = -30
    attackLevelThree = -70
    attackLevelThree_center = -90
    attackLevelFour_oneBlock = -700
    attackLevelFour = -800           # 열린4, 즉시승리 가능
    
    dolMin=0
    setDolX=0
    setDolY=0
    dol = white
    rival = black
    

    def __init__(self,mapchk):
        self.map=deepcopy(mapchk)

    def setMyDol(self, dol):
        self.dol=dol
        if dol==black:
            self.rival=white
        elif dol==white:
            self.rival=black

    def weightChk(self,mapchk):
        global winDolChk
        directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),  # 오른쪽, 왼쪽, 아래, 위
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # 우하단, 좌하단, 우상단, 좌상단
        ]

        self.map = deepcopy(mapchk)
        for y in range(5,24,1):
            for x in range(5,24,1):
                for dy,dx in directions:
                    if self.map[y][x]==self.rival:
                        if self.map[y][x]==self.rival and self.map[y+dy][x+dx]==self.rival:
                            if self.map[y+dy*2][x+dx*2]==self.rival:
                                if self.map[y+dy*3][x+dx*3]==self.rival:
                                    #four
                                    if self.map[y+dy*4][x+dx*4]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.defenseLevelFour_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*4][x+dx*4]<0:
                                            self.map[y+dy*4][x+dx*4]+=self.defenseLevelFour_oneBlock
                                    else:
                                        self.map[y+dy*4][x+dx*4]+=self.defenseLevelFour
                                        self.map[y-dy][x-dx]+=self.defenseLevelFour
                                    
                                else:
                                    #three
                                    if self.map[y+dy*3][x+dx*3]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.defenseLevelThree_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*3][x+dx*3]<0:
                                            self.map[y+dy*3][x+dx*3]+=self.defenseLevelThree_oneBlock
                                    else:
                                        self.map[y+dy*3][x+dx*3]+=self.defenseLevelThree
                                        self.map[y-dy][x-dx]+=self.defenseLevelThree
                            else:
                                #two
                                if self.map[y+dy*2][x+dx*2]>0:
                                    if self.map[y-dy][x-dx]<0:
                                        self.map[y-dy][x-dx]+=self.defenseLevelTwo_oneBlock
                                elif self.map[y-dy][x-dx]>0:
                                    if self.map[y+dy*2][x+dx*2]<0:
                                        self.map[y+dy*2][x+dx*2]+=self.defenseLevelTwo_oneBlock
                                else:
                                    self.map[y+dy*2][x+dx*2]+=self.defenseLevelTwo
                                    self.map[y-dy][x-dx]+=self.defenseLevelTwo
                        else:
                            #one
                                if self.map[y+dy][x+dx]<1:
                                    self.map[y+dy][x+dx]+=self.defenseLevelOne
                        if self.map[y+dy][x+dx]==self.rival and self.map[y+dy*2][x+dx*2]<1 and self.map[y+dy*3][x+dx*3]==self.rival:
                            self.map[y+dy*2][x+dx*2] += self.defenseLevelThree_center
                        elif  self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.rival and self.map[y+dy*3][x+dx*3]==self.rival:
                            self.map[y+dy][x+dx] += self.defenseLevelThree_center
                        elif self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.rival:
                            self.map[y+dy][x+dx] += self.defenseLevelTwo_center
                    
                    elif self.map[y][x]==self.dol:
                        if self.map[y][x]==self.dol and self.map[y+dy][x+dx]==self.dol:
                            if self.map[y+dy*2][x+dx*2]==self.dol:
                                if self.map[y+dy*3][x+dx*3]==self.dol:
                                    #four
                                    if self.map[y+dy*4][x+dx*4]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.attackLevelFour_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*4][x+dx*4]<0:
                                            self.map[y+dy*4][x+dx*4]+=self.attackLevelFour_oneBlock
                                    else:
                                        self.map[y+dy*4][x+dx*4]+=self.attackLevelFour
                                        self.map[y-dy][x-dx]+=self.attackLevelFour
                                    
                                else:
                                    #three
                                    if self.map[y+dy*3][x+dx*3]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.attackLevelThree_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*3][x+dx*3]<0:
                                            self.map[y+dy*3][x+dx*3]+=self.attackLevelThree_oneBlock
                                    else:
                                        self.map[y+dy*3][x+dx*3]+=self.attackLevelThree
                                        self.map[y-dy][x-dx]+=self.attackLevelThree
                            else:
                                #two
                                if self.map[y+dy*2][x+dx*2]>0:
                                    if self.map[y-dy][x-dx]<0:
                                        self.map[y-dy][x-dx]+=self.attackLevelTwo_oneBlock
                                elif self.map[y-dy][x-dx]>0:
                                    if self.map[y+dy*2][x+dx*2]<0:
                                        self.map[y+dy*2][x+dx*2]+=self.attackLevelTwo_oneBlock
                                else:
                                    self.map[y+dy*2][x+dx*2]+=self.attackLevelTwo
                                    self.map[y-dy][x-dx]+=self.attackLevelTwo
                        else:
                            #one
                                if self.map[y+dy][x+dx]<1:
                                    self.map[y+dy][x+dx]+=self.attackLevelOne
                        if self.map[y+dy][x+dx]==self.dol and self.map[y+dy*2][x+dx*2]<1 and self.map[y+dy*3][x+dx*3]==self.dol:
                            self.map[y+dy*2][x+dx*2] += self.attackLevelThree_center
                        elif  self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.dol and self.map[y+dy*3][x+dx*3]==self.dol:
                            self.map[y+dy][x+dx] += self.attackLevelThree_center
                        elif self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.dol:
                            self.map[y+dy][x+dx] += self.attackLevelTwo_center
        
        for y in range(0,29,1):
            for x in range(0,29,1):
                if self.map[y][x]<self.dolMin:
                    self.dolMin = self.map[y][x]
                    self.setDolX=x
                    self.setDolY=y
        self.dolMin=0
    
    def setDol(self):
        global map2
        map2[self.setDolY][self.setDolX] = self.dol                   
    
    def showMap(self):
        for i in range(0,29,1):
            for j in range(0,29,1):
                print(self.map[i][j],end=' ')
            print("\r")

                    

ai = pc(map2)



def on_press():
    global cursor_x, cursor_y, doly, dolx, dol, gameIng, winDolChk
    key = screen.getKey()  # 키 입력 대기 (1byte 입력받기)
    # 전역 변수 사용
    if key == 'w':  # W: 위로 이동
        cursor_y = max(1, cursor_y - 1)  # 위쪽 경계값 제한
        doly = max(5, doly - 1)
    elif key == 's':  # S: 아래로 이동
        cursor_y = min(19, cursor_y + 1)  # 아래쪽 경계값 제한
        doly = min(23, doly + 1) 
    elif key == 'a':  # A: 왼쪽으로 이동
        cursor_x = max(1, cursor_x - 2)  # 왼쪽 경계값 제한
        dolx = max(5, dolx - 1) 
    elif key == 'd':  # D: 오른쪽으로 이동
        cursor_x = min(37, cursor_x + 2)  # 오른쪽 경계값 제한
        dolx = min(23, dolx + 1) 
    elif key == 'l':
        if map2[doly][dolx]==0:
            map2[doly][dolx] = dol
            if winChk(dolx,doly,dol):
                gameIng=False
                winDolChk = dol
                return
            # else:
            #     if dol==black:
            #         dol=white
            #     else:
            #         dol=black
                
            ai.weightChk(map2)
            ai.setDol()
            if winChk(ai.setDolX,ai.setDolY,ai.dol):
                gameIng=False
                winDolChk = ai.dol
                return



def winChk(x,y,dol):
    right=0
    left=0
    up=0
    down=0
    riup=0
    rido=0
    leup=0
    ledo=0

    right = chkDol(x+1,y,1,0,dol,right)
    left = chkDol(x-1,y,-1,0,dol,left)
    up = chkDol(x,y-1,0,-1,dol,up)
    down = chkDol(x,y+1,0,1,dol,down)
    riup = chkDol(x+1,y-1,1,-1,dol,riup)
    rido = chkDol(x+1,y+1,1,1,dol,rido)
    leup = chkDol(x-1,y-1,-1,-1,dol,leup)
    ledo = chkDol(x-1,y+1,-1,1,dol,ledo)
    
    if right + left + 1 > 4:
        return True
    elif up + down + 1 >4:
        return True 
    elif riup + ledo + 1 >4:
        return True
    elif rido + leup + 1 >4:
        return True
    return False

def chkDol(x,y,plusX,plusY,dol,wei):
    if map2[y][x]==dol:
        wei = chkDol(x+plusX,y+plusY,plusX,plusY,dol,wei+1)
    return wei

def drawMap():
    screen.move_cursor_to(0,0)
    for i in range(0,19,1):
        j2=0
        for j in range(0,37,1):
            startStr = ""
            str = ""
            lastStr = ""
            if i==cursor_y-1 and j==cursor_x-1:
                startStr="\033[1;34m"
                lastStr="\033[0m"
            if j%2==0:
                if map2[i+5][j2+5]!=0:
                    if map2[i+5][j2+5]==black:
                        str='○'
                    elif map2[i+5][j2+5]==white:
                        str='●'
                else:
                    str=map1[i][j]
                j2=j2+1
            else:
                str = map1[i][j]
            startStr= startStr+str+lastStr
            print(startStr,end="")
        print("\r")


setDolIng=True
def on_press_setDol():
    global cursor_y, dol, setDolIng
    key = screen.getKey()  # 키 입력 대기 (1byte 입력받기)
    # 전역 변수 사용
    if key == 'w':  # W: 위로 이동
        cursor_y = 1
    elif key == 's':  # S: 아래로 이동
        cursor_y = 2
    elif key == 'l':
        if cursor_y==1:
            dol = black
            ai.setMyDol(white)
        elif cursor_y==2:
            dol = white
            ai.setMyDol(black)
        setDolIng=False
        
def drawDolMenu():
    screen.move_cursor_to(0,2)
    if(cursor_y==1):
        print("--> 검은 돌\r")
        print("하얀 돌    \r")
    else:
        print("검은 돌    \r")
        print("--> 하얀 돌\r")

def drawSetDolMenu():
    global dol,setDolIng,cursor_y,cursor_x,dolx, doly
    screen.clearScreen()
    setDolIng=True
    screen.move_cursor_to(0,0)
    print("돌을 선택하세요")
    while setDolIng:
        drawDolMenu()
        on_press_setDol()
    cursor_x, cursor_y = 1, 1
    dolx, doly = 5, 5
    screen.clearScreen()
        


def main():
    global gameIng
    for i in range(0,29,1):
        for j in range(0,29,1):
            map2[i][j]=0
    for i in range(0,29,1):
        map2[i][0]=3
        map2[i][1]=3
        map2[i][2]=3
        map2[i][3]=3
        map2[i][4]=3
        map2[0][i]=3
        map2[1][i]=3
        map2[2][i]=3
        map2[3][i]=3
        map2[4][i]=3
        map2[i][24]=3
        map2[i][25]=3
        map2[i][26]=3
        map2[i][27]=3
        map2[i][28]=3
        map2[24][i]=3
        map2[25][i]=3
        map2[26][i]=3
        map2[27][i]=3
        map2[28][i]=3
    
    drawSetDolMenu()    
    
    if(dol==white):
        map2[14][14]=black
    drawMap()
    while gameIng:
        screen.move_cursor_to(cursor_x, cursor_y)
        on_press()
        drawMap()
        #ai.showMap()
    
    screen.move_cursor_to(0, 20)
    if winDolChk==white:
        print("흰색 승")
    else:
        print("블랙 승")
    on_press()
    gameIng = True
    screen.clearScreen()

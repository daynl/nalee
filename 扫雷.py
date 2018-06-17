# -*- coding: utf-8 -*-
#!/usr/bin/python  
import sys  
import random  
import pygame
import pygame.locals
import tkinter

background_image_filename = 'b.jpg'
mine_image_filename='a.jpg'
win_image_filename='win.jpg'
over_image_filename='over.jpg'
cover_image_filename='zero.png'

running=1

class Window(tkinter.Frame):    
    def __init__(self, master= None):  
        tkinter.Frame.__init__(self, master)  
        self.master = master  
        self.init_window()  
  
    def init_window(self):  
        # 设置窗体的标题
        self.master.title("")  
        self.pack(fill=tkinter.BOTH, expand=1)  
        # 创建一个按钮，调用tkinter下的Button类 
        w = tkinter.Label(self, text="CONTINUE OR NOT") 
        w.pack()  
        quitButton2 = tkinter.Button(self, text="YES",command=self.client)  
        quitButton2.place(x=50,y=20)
        quitButton1 = tkinter.Button(self, text="NO",command=self.client_exit)  
        quitButton1.place(x=150,y=20)
    def client_exit(self):
        pygame.quit()
        exit()
        self.master.destroy()  
    def client(self):
        self.master.destroy()
    
class MineSweeping():  
    #扫雷主程序  
    def __init__(self,row=8,line=8,mineNum = 15):  
        self.row = row  
        self.line = line
        self.score = 0 #分数  
        self.mineNum = mineNum
        self.xy_list = [[0 for i in range(self.line)] for i in range(self.row)]
        self.xy_num = [[0 for i in range(self.line)] for i in range(self.row)]
    def initData(self):
        # 初始化状态值
        # 游戏开始的时候状态值为清零(再重新设置状态值)
        self.xy_list = [[0 for i in range(self.line)] for i in range(self.row)]
        # 设置雷的数量  
        self.xy_num = [[0 for i in range(self.line)] for i in range(self.row)]
        maxMine = self.mineNum  
        while maxMine > 0 :
            num_x = random.randint(0,self.row-1)  
            num_y = random.randint(0,self.line-1)  
            if self.xy_list[num_x][num_y] == 0:  
                self.xy_list[num_x][num_y] = 1
                self.xy_num[num_x][num_y]=self.xy_num[num_x][num_y]+1
                if num_y>0 :
                    self.xy_num[num_x][num_y-1]=self.xy_num[num_x][num_y-1]+1
                if num_x>0:
                    self.xy_num[num_x-1][num_y]=self.xy_num[num_x-1][num_y]+1
                if num_x>0 and num_y>0:
                    self.xy_num[num_x-1][num_y-1]=self.xy_num[num_x-1][num_y-1]+1
                if num_x>0 and num_y<7:
                    self.xy_num[num_x-1][num_y+1]=self.xy_num[num_x-1][num_y+1]+1
                if num_x<7 and num_y>0:
                    self.xy_num[num_x+1][num_y-1]=self.xy_num[num_x+1][num_y-1]+1
                if num_x<7:
                    self.xy_num[num_x+1][num_y]=self.xy_num[num_x+1][num_y]+1
                if num_x<7 and num_y<7:
                    self.xy_num[num_x+1][num_y+1]=self.xy_num[num_x+1][num_y+1]+1
                if num_y<7:
                    self.xy_num[num_x][num_y+1]=self.xy_num[num_x][num_y+1]+1
                maxMine -= 1
  
    def  mine_clear(self,x,y):  
        # 设置显示进行扫过的数目  
        # 设置数字  
        # 0 表示未扫过的安全位置
        # 1 表示雷
        # 2 表示扫过的位置 
        #获取坐标的数字  
        pos = self.xy_list[x][y]  
        if pos == 0 :  
            self.xy_list[x][y] = 2 
            if y>0 and self.xy_list[x][y-1]!=1:
                self.xy_list[x][y-1]=3
            if x>0 and self.xy_list[x-1][y]!=1:
                self.xy_list[x-1][y]=3
            if x<7 and y<7 and self.xy_list[x+1][y+1]!=1:
                self.xy_list[x+1][y+1]=3
            return 0  
        elif pos == 2 :
            return 2  
        elif pos == 3 :
            return 2  
        else:  
            return 1  
    def mineFace(self,state,x,y):  
        #显示界面的内容  
        #设置游戏的状态  
        #1 表示运行的状态  
        #2 表示输出的状态  
        #3 表示游戏结束的状态  
        #4 表示游戏获得了完胜  
        coverer=pygame.image.load(cover_image_filename).convert()
        if state == 1:
            font1 = pygame.font.SysFont('simsun',48)
            screen.blit(font1.render('Score:',True,(255,127,0)),(20,25))
            screen.blit(coverer, (160, 25))
            screen.blit(font1.render('%s' % self.score,True,(255,127,0)),(170,25))
            while x:
                while y:
                    rc = (175, 175, 175)
                    rp = (50+50*x, 50+50*y)
                    rs = (49, 49)
                    pygame.draw.rect(screen, rc, pygame.Rect(rp, rs))
                    y=y-1
                x=x-1
                y=self.line
            pygame.display.update()

        if state == 2:
            font1 = pygame.font.SysFont('simsun',48)
            screen.blit(font1.render('Score:',True,(255,127,0)),(20,25))     #font.render第一个参数是文本内容，第二个参数是否抗锯齿，第三个参数字体颜色
            screen.blit(coverer, (160, 25))
            screen.blit(font1.render('%s' % self.score,True,(255,127,0)),(170,25))
            rc = (200, 200, 200)
            rp = (100+50*x, 100+50*y)
            rs = (49, 49)
            pygame.draw.rect(screen, rc, pygame.Rect(rp, rs))
            font3 = pygame.font.SysFont('simsun',48)
            screen.blit(font3.render('%s' % self.xy_num[x][y],True,(255,127,0)),(115+50*x, 110+50*y))
            if y>0 and self.xy_list[x][y-1]!=1:
                rc = (200, 200, 200)
                rp = (100+50*x, 100+50*(y-1))
                rs = (49, 49)
                pygame.draw.rect(screen, rc, pygame.Rect(rp, rs))
                font3 = pygame.font.SysFont('simsun',48)
                screen.blit(font3.render('%s' % self.xy_num[x][y-1],True,(255,127,0)),(115+50*x, 110+50*(y-1)))
            if x>0 and self.xy_list[x-1][y]!=1:
                rc = (200, 200, 200)
                rp = (100+50*(x-1), 100+50*y)
                rs = (49, 49)
                pygame.draw.rect(screen, rc, pygame.Rect(rp, rs))
                font3 = pygame.font.SysFont('simsun',48)
                screen.blit(font3.render('%s' % self.xy_num[x-1][y],True,(255,127,0)),(115+50*(x-1), 110+50*y))
            if x<7 and y<7 and self.xy_list[x+1][y+1]!=1:
                rc = (200, 200, 200)
                rp = (100+50*(x+1), 100+50*(y+1))
                rs = (49, 49)
                pygame.draw.rect(screen, rc, pygame.Rect(rp, rs))
                font3 = pygame.font.SysFont('simsun',48)
                screen.blit(font3.render('%s' % self.xy_num[x+1][y+1],True,(255,127,0)),(115+50*(x+1), 110+50*(y+1)))
            pygame.display.update()
        if state == 3:
            miner=pygame.image.load(mine_image_filename).convert()
            screen.blit(miner, (100+50*x, 100+50*y))
            pygame.display.update()

    def MainLoop(self):  
        #创建游戏主循环  
        #创建界面的运行  
        coverer=pygame.image.load(cover_image_filename).convert()
        self.mineFace(1,self.line,self.row)  
        self.score = 0
        self.initData()  
        #print self.xy_list  
        while 1:       
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #获取坐标的位置
                x, y = pygame.mouse.get_pos()
                #获得鼠标位置
                x = (int)((x-100)/50)
                y = (int)((y-100)/50)
                if x>-1 and y>-1:
                    num = self.mine_clear(x,y)
                #判断是否过的了完胜
                win = True
                for i in self.xy_list:
                    if 0 in i:
                        win = False 
                        break 
                if win:
                    num = 4 
                    #执行刷新界面的函数  
                if num == 0 or num==2:
                    self.score += 10 
                    self.mineFace(2,x,y)
                elif num==-1:
                    self.mineFace(1,self.line,self.row)
                elif num == 1:
                    self.mineFace(3,x,y)
                    screen.blit(coverer, (160, 25))
                    screen.blit(font1.render('%s' % self.score,True,(255,127,0)),(170,25))
                    overer=pygame.image.load(over_image_filename).convert()
                    screen.blit(overer, (150, 100))
                    pygame.display.update()
                    # 是不是进行下一局
                    root = tkinter.Tk()  
                    root.geometry("200x55")  
                    Window(root)  
                    root.mainloop()
                    break
                
                if num==4:
                    self.score += 10
                    self.mineFace(2,x,y)
                    winner=pygame.image.load(win_image_filename).convert()
                    screen.blit(winner, (150, 100))
                    pygame.display.update()
                    root = tkinter.Tk()  
                    root.geometry("200x55")  
                    Window(root)  
                    root.mainloop()      
                    break

if __name__ == '__main__': 
    pygame.init()
    score=0
    screen = pygame.display.set_mode((840, 600),0, 32)
    SCREEN_SIZE = (840, 600)
    screen = pygame.display.set_mode(SCREEN_SIZE,0, 32)
    event_text = []
    pygame.display.set_caption("扫雷")
    background = pygame.image.load(background_image_filename).convert()
    font = pygame.font.SysFont("arial", 16);
    font_height = font.get_linesize()
    event = pygame.event.wait()
    pygame.mixer.music.load('月光.mp3')
    pygame.mixer.music.play()
    #将背景图画上去
    pygame.display.update()
    while running:
        #游戏主循环
        event = pygame.event.wait()
        event_text.append(str(event))
        screen.blit(background, (0,0))
        #将背景图画上去
        my_font = pygame.font.SysFont("arial", 16)
        font1 = pygame.font.SysFont('simsun',48)
        font2 = pygame.font.SysFont(None,32)
        screen.blit(font1.render('Score:',True,(255,127,0)),(20,25))     #font.render第一个参数是文本内容，第二个参数是否抗锯齿，第三个参数字体颜色
        screen.blit(font2.render('Sweeping',True,(255,127,0)),(300,50))
        x, y = pygame.mouse.get_pos()
        #获得鼠标位置
        pygame.display.update()
        #刷新一下画面
        mi=MineSweeping(8,8,15)
        mi.MainLoop()
        if event.type == pygame.QUIT:
            running=0
        pygame.display.update()
    pygame.quit()
    sys.exit() 

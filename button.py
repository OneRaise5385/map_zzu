import pygame

class Button():
    '''按钮'''
    def __init__(self,screen,x,y,describe=''):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.describe = describe

        # 设置按钮尺寸和其他属性
        self.width = 100
        self.height = 60
        self.font = pygame.font.SysFont(None,48)

        # 创建按钮的rect对象
        self.rect = pygame.Rect(x,y,self.width,self.height)

class SelectStats():
    '''跟踪起点和目的地的状态'''
    def __init__(self):
        self.active = True


def select_start(screen,stats0):
    '''选择起点'''
    # 添加起点景点按钮
    v0 = Button(screen,411,480,'这是东门')
    v4 = Button(screen,308,0,'看病难')
    v5 = Button(screen,205,0,'这是北门')
    v8 = Button(screen,68,171,'北体育馆')
    v14 = Button(screen,205,274,'沙土堆儿')
    v16 = Button(screen,0,342,'中心体育馆')
    v20 = Button(screen,0,460,'本源体育场很大')
    v22 = Button(screen,228,470,'很高')
    v22_1 = Button(screen,308,480,'没空调')
    v27 = Button(screen,205,651,'值得去')
    v31 = Button(screen,102,754,'南体育场')
    v33 = Button(screen,205,788,'这里举行升旗仪式，国旗护卫队很帅')
    v37 = Button(screen,205,857,'这里是南门')
    text = ''
    '''选择景点'''
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and stats0.active == True:  #  监视鼠标状态及位置
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if v0.rect.collidepoint(mouse_x,mouse_y):  # 如果在按钮的范围内则赋值景点与景点信息
                text = v0.describe
                v = 0
            elif v4.rect.collidepoint(mouse_x,mouse_y):
                text = v4.describe
                v = 4
            elif v5.rect.collidepoint(mouse_x,mouse_y):
                text = v5.describe
                v = 5
            elif v8.rect.collidepoint(mouse_x,mouse_y):
                text = v8.describe
                v = 8
            elif v14.rect.collidepoint(mouse_x,mouse_y):
                text = v14.describe
                v = 14
            elif v16.rect.collidepoint(mouse_x,mouse_y):
                text = v16.describe
                v = 16
            elif v20.rect.collidepoint(mouse_x,mouse_y):
                text = v20.describe
                v = 20
            elif v22.rect.collidepoint(mouse_x,mouse_y):
                text = v22.describe
                v = 22
            elif v22_1.rect.collidepoint(mouse_x,mouse_y):
                text = v22_1.describe
                v = 22
            elif v27.rect.collidepoint(mouse_x,mouse_y):
                text = v27.describe
                v = 27
            elif v31.rect.collidepoint(mouse_x,mouse_y):
                text = v31.describe
                v = 31
            elif v33.rect.collidepoint(mouse_x,mouse_y):
                text = v33.describe
                v = 33
            elif v37.rect.collidepoint(mouse_x,mouse_y):
                text = v37.describe
                v = 37
        print(text)
    if text != '':
        stats0.active = False
        return v,text  # 返回顶点与景点信息
    

def select_to(screen,stats0,stats1):
    '''选择终点'''
    v0 = Button(screen,411,480,'这是东门')
    v4 = Button(screen,308,0,'看病难')
    v5 = Button(screen,205,0,'这是北门')
    v8 = Button(screen,68,171,'北体育馆')
    v14 = Button(screen,205,274,'沙土堆儿')
    v16 = Button(screen,0,342,'中心体育馆')
    v20 = Button(screen,0,460,'本源体育场很大')
    v22 = Button(screen,228,470,'钟楼很高')
    v22_1 = Button(screen,308,480,'图书馆没空调')
    v27 = Button(screen,205,651,'校史馆值得去')
    v31 = Button(screen,102,754,'南体育场')
    v33 = Button(screen,205,788,'这里举行升旗仪式，国旗护卫队很帅')
    v37 = Button(screen,205,857,'这里是南门')
    text = ''
    '''选择地点'''
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and stats0.active == False:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if v0.rect.collidepoint(mouse_x,mouse_y):
                text = v0.describe
                print('测试')
                v = 0
            elif v4.rect.collidepoint(mouse_x,mouse_y):
                text = v4.describe
                v = 4
            elif v5.rect.collidepoint(mouse_x,mouse_y):
                text = v5.describe
                v = 5
            elif v8.rect.collidepoint(mouse_x,mouse_y):
                text = v8.describe
                v = 8
            elif v14.rect.collidepoint(mouse_x,mouse_y):
                text = v14.describe
                v = 14
            elif v16.rect.collidepoint(mouse_x,mouse_y):
                text = v16.describe
                v = 16
            elif v20.rect.collidepoint(mouse_x,mouse_y):
                text = v20.describe
                v = 20
            elif v22.rect.collidepoint(mouse_x,mouse_y):
                text = v22.describe
                v = 22
            elif v22_1.rect.collidepoint(mouse_x,mouse_y):
                text = v22_1.describe
                v = 22
            elif v27.rect.collidepoint(mouse_x,mouse_y):
                text = v27.describe
                v = 27
            elif v31.rect.collidepoint(mouse_x,mouse_y):
                text = v31.describe
                v = 31
            elif v33.rect.collidepoint(mouse_x,mouse_y):
                text = v33.describe
                v = 33
            elif v37.rect.collidepoint(mouse_x,mouse_y):
                text = v37.describe
                v = 37
        print(text)
    if text != '':
        stats0.active = True
        stats1.active = False
        return v,text


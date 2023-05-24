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

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(x,y,self.width,self.height)

        
def select():
    '''选择地点'''
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if v0.rect.collidepoint(mouse_x,mouse_y):
                text = v0.describe
            elif v4.rect.collidepoint(mouse_x,mouse_y):
                text = v4.describe
            elif v5.rect.collidepoint(mouse_x,mouse_y):
                text = v5.describe
            elif v8.rect.collidepoint(mouse_x,mouse_y):
                text = v8.describe
            elif v14.rect.collidepoint(mouse_x,mouse_y):
                text = v14.describe
            elif v16.rect.collidepoint(mouse_x,mouse_y):
                text = v16.describe
            elif v20.rect.collidepoint(mouse_x,mouse_y):
                text = v20.describe
            elif v22.rect.collidepoint(mouse_x,mouse_y):
                text = v22.describe
            elif v22_1.rect.collidepoint(mouse_x,mouse_y):
                text = v22_1.describe
            elif v27.rect.collidepoint(mouse_x,mouse_y):
                text = v27.describe
            elif v31.rect.collidepoint(mouse_x,mouse_y):
                text = v31.describe
            elif v33.rect.collidepoint(mouse_x,mouse_y):
                text = v33.describe
            elif v37.rect.collidepoint(mouse_x,mouse_y):
                text = v37.describe


v0 = Button(screen,0,0,'东门：这是东门')
v4 = Button(screen,0,0,'校医院：看病难')
v5 = Button(screen,0,0,'北门：这是北门')
v8 = Button(screen,0,0,'北体育馆：北体育馆')
v14 = Button(screen,0,0,'厚山：沙土堆')
v16 = Button(screen,0,0,'中心体育馆')
v20 = Button(screen,0,0,'本源体育场：很大')
v22 = Button(screen,0,0,'钟楼：很高')
v22_1 = Button(screen,0,0,'图书馆：没空调')
v27 = Button(screen,0,0,'校史馆：值得去')
v31 = Button(screen,0,0,'南体育场')
v33 = Button(screen,0,0,'这里举行升旗仪式，国旗护卫队很帅')
v37 = Button(screen,0,0,'南门：这里是南门')


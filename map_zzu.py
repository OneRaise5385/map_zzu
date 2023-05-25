import sys
import pygame
import button
from dijkstra import creat_routes

def run_map_zzu():
    '''初始化并创建一个屏幕对象'''
    pygame.init()
    screen = pygame.display.set_mode((480,900))  # 创建一个屏幕对象
    pygame.display.set_caption('Map_ZZU')  # 设置标题
    myfont = pygame.font.Font('font.ttf', 30)  # 设置字体
    myfont1 = pygame.font.Font('font.ttf', 20)
    
    # 初始化选择状态信息
    stats0 = button.SelectStats()  # 起点按钮状态
    stats1 = button.SelectStats()  # 终点按钮状态
    search = button.Button(screen,380,0)  # 查询按钮
    start = None  # 起点信息
    to = None  # 终点信息

    # 开始程序循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and search.rect.collidepoint(mouse_x,mouse_y):
                stats0 = button.SelectStats()
                stats1 = button.SelectStats()

        # 绘制郑州大学平面图
        screen.blit(pygame.image.load('route/zzu.png'),(0,0))
        # 绘制查询按钮
        text_search = myfont1.render('Search',True,(255,255,255))
        screen.blit(text_search,(400,0))

        # 选择景点
        if stats1.active == True:
            if stats0.active == True:
                start = button.select_start(screen,stats0)
            elif stats0.active == False:
                to = button.select_to(screen,stats0,stats1)

        # 显示景点信息
        if start != None:
            text_start = myfont.render(start[1],True,(255,255,255))
            screen.blit(text_start,(0,0))
        if to != None:
            text_to = myfont.render(to[1],True,(255,255,255))
            screen.blit(text_to,(0,40))

        # 绘制路径
        if stats1.active == False:
            for i in creat_routes(start[0],to[0]):
                screen.blit(pygame.image.load(i),(0,0))

        # 让最近绘制的更新
        pygame.display.flip()

# 运行主程序
run_map_zzu()

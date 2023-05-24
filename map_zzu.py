import sys
import pygame
import dijkstra
import zzu_graph

def creat_routes(start,to):
    zzu_path = zzu_graph.set_zzu_graph()
    min_path = dijkstra.dijkstra_shortest_paths(zzu_path,start)
    min_v = dijkstra.findv(min_path,start,to)
    min_route = dijkstra.create_route(min_v)
    return min_route


def run_map_zzu():
    '''初始化并创建一个屏幕对象'''
    pygame.init()
    screen = pygame.display.set_mode((600,900))
    pygame.display.set_caption('Map_ZZU')

    # 开始程序循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 填充背景
        screen.fill((230,230,230))

        # 绘制地图
        screen.blit(pygame.image.load('route/zzu.png'),(0,0))
        for i in creat_routes(0,20):
            screen.blit(pygame.image.load(i),(0,0))


        pygame.display.flip()  # 让最近绘制的屏幕可见

run_map_zzu()

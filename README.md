# map_zzu
数据结构期末作业：zzu校园导航
## 简介
本项目针对郑州大学设计一个校园导航系统，采用dijkstra算法求两点之间最短距离，同时使用优先队列数据结构实现，并制作出程序的GUI界面。
文件中共包含以下内容：route文件夹，里面主要存储GUI实现中的路径和郑州大学平面图；font.ttf字体文件；程序主体部分button.py, dijkstra.py, map_zzu.py, structure.py, zzu_graph.py；以及说明文档readme.pdf。
## 使用说明
将route.zip压缩包解压缩后将文件夹route放在与map_zzu.py同一路径下运行map_zzu.py即可
## 变量函数说明
### structure.py
- GraphAL()：用邻接表实现的图结构的类
- add_vertex()：新增顶点
- add_edge()：新增边
- get_edge()：获取边的信息
- vertex_num()：顶点个数
- _out_edges()：获取出边的静态方法
- PrioQue()：基于list实现的优先队列
- is_empty(): 判断是否为空
- peek(): 队列顶部的值
- dequeue(): 出队
- enqueue(): 入队
### zzu_graph.py
- set_zzu_graph(): 创建地图的图
- zzu_graph：郑州大学地图图结构
- v0: 东门
- v4: 校医院
- v5: 北门
- v8: 北体
- v14: 厚山
- v16: 中体
- v20: 本源体育场
- v22: 钟楼or图书馆
- v27: 校史馆
- v31: 南体
- v37: 南门
### dijkstra.py
- dijkstra_shortest_paths(): 用dijkstra算法求出最短路径
- findv(): 获取最短路径中经过的顶点
- create_route(): 生成地图路径的索引
- creat_routes(): 获取路径
- zzu_path: 郑州大学图结构
- min_path: 最短路径
- min_v: 最短路径对应的顶点
- min_toure: 最短路径对应的路径索引
### button.py
- Button(): 定义按钮类
- SelectStats(): 跟踪起点和目的地的状态的类
- select_start(): 选择起点
- v0-v37: 景点对应的按钮
- select_to(): 选择终点
- text：对应景点信息
### map_zzu.py
- run_map_zzu(): 初始化并创建一个屏幕对象
- screen: 创建一个屏幕对象
- my_font: 字体文件
- stats0: 按钮状态信息
- search: 查询按钮信息

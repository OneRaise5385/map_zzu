from structure import *


def dijkstra_shortest_paths(graph, v0):
    '''用dijkstra算法求出最短路径'''
    vnum = graph.vertex_num()
    # vnum = 40
    assert 0 <= v0 < vnum
    count, paths = 0, [None]*vnum
    cands = PrioQue([(0, v0, v0)])
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        # print(paths[vmin])
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths

def findv(paths,start,to):
    '''获取最短路径中经过的顶点'''
    r = [to]  # r: 最短路径中依次经过的顶点集合
    u = paths[to][0]  # u:最短路径中依次经过的顶点
    r.append(u)
    while u != start:
        u = paths[u][0]
        r.append(u)
    return r

def create_route(r):
    '''生成地图路径的索引'''
    indexes = []
    for i in range(0,len(r) - 1):
        index = 'route/v'
        if len(str(r[i])) == 1:
            index += '0'
            index += str(r[i])
        else:
            index += str(r[i])
        if len(str(r[i + 1])) == 1:
            index += '0'
            index += str(r[i + 1])
        else:
            index += str(r[i + 1])
        index += '.png'
        indexes.append(index)
    return indexes
 


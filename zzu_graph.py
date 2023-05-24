from structure import GraphAL

def set_zzu_graph():
    '''创建地图的图'''
    route_init = []  # 地图初始化
    zzu_graph = GraphAL(route_init,0)  # 创建空的地图图结构

    v0 = zzu_graph.add_vertex()   # 东门
    v1 = zzu_graph.add_vertex()
    v2 = zzu_graph.add_vertex()
    v3 = zzu_graph.add_vertex()
    v4 = zzu_graph.add_vertex()   # 校医院
    v5 = zzu_graph.add_vertex()   # 北门
    v6 = zzu_graph.add_vertex()
    v7 = zzu_graph.add_vertex()
    v8 = zzu_graph.add_vertex()   # 北体
    v9 = zzu_graph.add_vertex()
    v10 = zzu_graph.add_vertex()
    v11 = zzu_graph.add_vertex()
    v12 = zzu_graph.add_vertex()
    v13 = zzu_graph.add_vertex()
    v14 = zzu_graph.add_vertex()  # 厚山
    v15 = zzu_graph.add_vertex()
    v16 = zzu_graph.add_vertex()  # 中体
    v17 = zzu_graph.add_vertex()
    v18 = zzu_graph.add_vertex()
    v19 = zzu_graph.add_vertex()
    v20 = zzu_graph.add_vertex()  # 本源体育场
    v21 = zzu_graph.add_vertex()
    v22 = zzu_graph.add_vertex()  # 钟楼or图书馆
    v23 = zzu_graph.add_vertex()
    v24 = zzu_graph.add_vertex()
    v25 = zzu_graph.add_vertex()
    v26 = zzu_graph.add_vertex()
    v27 = zzu_graph.add_vertex()  # 校史馆
    v28 = zzu_graph.add_vertex()
    v29 = zzu_graph.add_vertex()
    v30 = zzu_graph.add_vertex()
    v31 = zzu_graph.add_vertex()  # 南体
    v32 = zzu_graph.add_vertex()
    v33 = zzu_graph.add_vertex()  # 升旗
    v34 = zzu_graph.add_vertex()
    v35 = zzu_graph.add_vertex()
    v36 = zzu_graph.add_vertex()
    v37 = zzu_graph.add_vertex()  # 南门
    v38 = zzu_graph.add_vertex()
    v39 = zzu_graph.add_vertex()
    # v = zzu_graph.add_vertex()

    # 添加边
    zzu_graph.add_edge(v0,v1,2)
    zzu_graph.add_edge(v0,v39,2)
    zzu_graph.add_edge(v1,v0,2)
    zzu_graph.add_edge(v1,v2,8)
    zzu_graph.add_edge(v1,v19,7.5)
    zzu_graph.add_edge(v2,v1,8)
    zzu_graph.add_edge(v2,v15,8.5)
    zzu_graph.add_edge(v2,v3,6)
    zzu_graph.add_edge(v3,v2,6)
    zzu_graph.add_edge(v3,v11,10)
    zzu_graph.add_edge(v3,v4,14)
    zzu_graph.add_edge(v4,v3,14)
    zzu_graph.add_edge(v4,v5,6)
    zzu_graph.add_edge(v5,v4,6)
    zzu_graph.add_edge(v5,v6,3)
    zzu_graph.add_edge(v6,v5,3)
    zzu_graph.add_edge(v6,v7,16)
    zzu_graph.add_edge(v6,v10,5)
    zzu_graph.add_edge(v7,v6,16)
    zzu_graph.add_edge(v7,v8,4.8)
    zzu_graph.add_edge(v7,v12,6)
    zzu_graph.add_edge(v8,v7,4.8)
    zzu_graph.add_edge(v8,v9,4.8)
    zzu_graph.add_edge(v9,v8,4.8)
    zzu_graph.add_edge(v9,v10,2.3)
    zzu_graph.add_edge(v9,v13,7)
    zzu_graph.add_edge(v10,v6,5)
    zzu_graph.add_edge(v10,v9,2.3)
    zzu_graph.add_edge(v10,v11,2.3)
    zzu_graph.add_edge(v11,v10,2.3)
    zzu_graph.add_edge(v11,v3,10)
    zzu_graph.add_edge(v11,v15,7)
    zzu_graph.add_edge(v12,v7,6)
    zzu_graph.add_edge(v12,v16,3.5)
    zzu_graph.add_edge(v12,v13,8)
    zzu_graph.add_edge(v12,v7,6)
    zzu_graph.add_edge(v13,v9,7)
    zzu_graph.add_edge(v13,v12,8)
    zzu_graph.add_edge(v13,v14,3.6)
    zzu_graph.add_edge(v13,v18,7)
    zzu_graph.add_edge(v14,v13,3.6)
    zzu_graph.add_edge(v14,v15,3.6)
    zzu_graph.add_edge(v15,v11,7)
    zzu_graph.add_edge(v15,v14,3.6)
    zzu_graph.add_edge(v15,v2,8.5)
    zzu_graph.add_edge(v15,v19,7)
    zzu_graph.add_edge(v16,v12,3.5)
    zzu_graph.add_edge(v16,v17,3.5)
    zzu_graph.add_edge(v17,v16,3.5)
    zzu_graph.add_edge(v17,v18,8)
    zzu_graph.add_edge(v17,v20,3.1)
    zzu_graph.add_edge(v18,v13,7)
    zzu_graph.add_edge(v18,v17,8)
    zzu_graph.add_edge(v18,v19,8.6)
    zzu_graph.add_edge(v18,v21,v4)
    zzu_graph.add_edge(v19,v15,7)
    zzu_graph.add_edge(v19,v18,8.6)
    zzu_graph.add_edge(v19,v1,7.5)
    zzu_graph.add_edge(v19,v22,2)
    zzu_graph.add_edge(v20,v17,3.1)
    zzu_graph.add_edge(v20,v24,3.1)
    zzu_graph.add_edge(v21,v18,4)
    zzu_graph.add_edge(v21,v24,8)
    zzu_graph.add_edge(v21,v23,8.6)
    zzu_graph.add_edge(v21,v26,8)
    zzu_graph.add_edge(v22,v19,2)
    zzu_graph.add_edge(v22,v23,2)
    zzu_graph.add_edge(v23,v22,2)
    zzu_graph.add_edge(v23,v21,8.6)
    zzu_graph.add_edge(v23,v39,7.5)
    zzu_graph.add_edge(v23,v28,8)
    zzu_graph.add_edge(v24,v20,3.1)
    zzu_graph.add_edge(v24,v21,8)
    zzu_graph.add_edge(v24,v25,6)
    zzu_graph.add_edge(v25,v24,6)
    zzu_graph.add_edge(v25,v26,8.8)
    zzu_graph.add_edge(v25,v30,8.6)
    zzu_graph.add_edge(v26,v25,8.8)
    zzu_graph.add_edge(v26,v21,8)
    zzu_graph.add_edge(v26,v27,3.5)
    zzu_graph.add_edge(v26,v32,7)
    zzu_graph.add_edge(v27,v26,3.5)
    zzu_graph.add_edge(v27,v28,3.5)
    zzu_graph.add_edge(v28,v23,8)
    zzu_graph.add_edge(v28,v27,3.5)
    zzu_graph.add_edge(v28,v29,8.2)
    zzu_graph.add_edge(v28,v34,7)
    zzu_graph.add_edge(v29,v39,7.5)
    zzu_graph.add_edge(v29,v28,8.2)
    zzu_graph.add_edge(v29,v35,6.2)
    zzu_graph.add_edge(v30,v25,8.6)
    zzu_graph.add_edge(v30,v36,11.4)
    zzu_graph.add_edge(v30,v31,3.4)
    zzu_graph.add_edge(v31,v30,3.4)
    zzu_graph.add_edge(v31,v32,3.4)
    zzu_graph.add_edge(v32,v31,3.4)
    zzu_graph.add_edge(v32,v26,7)
    zzu_graph.add_edge(v32,v33,2)
    zzu_graph.add_edge(v32,v36,4.2)
    zzu_graph.add_edge(v33,v32,2)
    zzu_graph.add_edge(v33,v34,2)
    zzu_graph.add_edge(v34,v28,7)
    zzu_graph.add_edge(v34,v33,2)
    zzu_graph.add_edge(v34,v38,4.2)
    zzu_graph.add_edge(v34,v35,9.2)
    zzu_graph.add_edge(v35,v29,6.2)
    zzu_graph.add_edge(v35,v34,9.2)
    zzu_graph.add_edge(v35,v38,13.2)
    zzu_graph.add_edge(v36,v30,11.4)
    zzu_graph.add_edge(v36,v32,4.2)
    zzu_graph.add_edge(v36,v37,2)
    zzu_graph.add_edge(v37,v36,2)
    zzu_graph.add_edge(v37,v38,2)
    zzu_graph.add_edge(v38,v37,2)
    zzu_graph.add_edge(v38,v34,4.2)
    zzu_graph.add_edge(v38,v35,13.2)
    zzu_graph.add_edge(v39,v0,2)
    zzu_graph.add_edge(v39,v23,7.5)
    zzu_graph.add_edge(v39,v29,7.5)

    return zzu_graph

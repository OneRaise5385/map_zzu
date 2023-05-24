class GraphAL():
    '''用邻接表实现的图结构'''
    def __init__(self, mat=[], unconn=0):
        '''初始化'''
        vnum = len(mat)
        self._mat = [self._out_edges(mat[i], unconn)
                     for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        '''新增顶点'''
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        '''新增边'''
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:  # 修改 mat[vi][vj] 的值
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:  # 原无到vj的边，退出循环在正确位置加入
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        '''获取边的信息'''
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        '''获取出边'''
        return self._mat[vi]
    
    def vertex_num(self):
        '''顶点个数'''
        return self._vnum
    
    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges
    
    def __str__(self):
        '''字符输出'''
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]"\
               + "\nUnconnected: " + str(self._unconn)

class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def is_empty(self):
        return not self._elems

    def peek(self):
        return self._elems[-1]

    def dequeue(self):
        return self._elems.pop()

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

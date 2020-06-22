'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-11 11:36:03
@LastEditors: hu_xz
@LastEditTime: 2020-06-19 17:03:18
'''
#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 朋友圈
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 并查集
        # 因为1和2是朋友，2和1也是朋友，因此矩阵是个对称矩阵
        size = len(M)
        uf = UF(size)
        for i in range(size):
            for j in range(i, size):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count

class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 

    def union(self, p, q):
        rootq = self.find(q)
        rootp = self.find(p)
        if rootp == rootq:
            return 

        if self.size[rootq] > self.size[rootp]:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        self.count -= 1

        
                      
# @lc code=end

#%%
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 并查集
        uf = UnionFind(len(M))
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count

class UnionFind:
    def __init__(self, n):
        # 一开始互不连通
        self.count = n
        # 父节点初始指向自己
        self.parent = [i for i in range(n)]
        # 初始化每棵树的size
        self.size = [1 for _ in range(n)]

    def find(self, son):
        # 路径压缩，使得每棵树的高度为常数
        # 优化时间复杂度为O(1)
        while son != self.parent[son]:
            # 子节点指向爷爷节点
            self.parent[son] = self.parent[self.parent[son]]
            son = self.parent[son]
        return son
        # root = son
        # while self.parent[son] != root:
        #     root = self.parent[root]
        # while self.parent[son] != son:
        #     x = son;son = self.parent[son];self.parent[x] = root
        # return root

    def union(self, p, q):
        # 暴力合并会造成线性的时间复杂度O(n)
        # 优化--》 使得小树接到大树上，较平衡
        # 因此初始化一个size，即树的节点数，降到O(logN)
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return 

        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q 
            self.size[root_q] += self.size[root_p]
        
        self.count -= 1

    # def is_connection(self, p, q):
    #     return self.find(p) == self.find(q)
M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
s = Solution()
s.findCircleNum(M)
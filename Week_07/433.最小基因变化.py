'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-15 15:55:30
@LastEditors: hu_xz
@LastEditTime: 2020-06-19 15:40:02
'''
#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
#

# @lc code=start
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # 双向bfs
        if end not in bank:
            return -1
        bank = set(bank)
        start = set([start])
        end = set([end])
        d = {'A':'GCT', 'G':'ACT', 'C':'AGT', 'T':'AGC'}
        count = 0
        while start:
            count += 1
            deque = set()
            for vocab in start:
                for i, item in enumerate(vocab):
                    for char in d[item]:
                        tmp = vocab[:i] + char + vocab[i+1:]
                        if tmp in end:
                            return count
                        if tmp in bank:
                            deque.add(tmp)
                            bank.remove(tmp)
        
            if len(end) <  len(deque):
                start, end = end, deque
            else:
                start = deque
        return -1
  
# @lc code=end

#%%


# %%

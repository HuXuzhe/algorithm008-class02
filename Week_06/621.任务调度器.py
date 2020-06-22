'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-05 00:17:18
@LastEditors: hu_xz
@LastEditTime: 2020-06-19 09:47:46
'''
#
# @lc app=leetcode.cn id=621 lang=python
#
# [621] 任务调度器
#

# @lc code=start
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # (任务最多的长度-1) * (冷却长度+1) + 相同多任务的任务个数
        most = collections.Counter(tasks)
        most_value = most.most_common()[0][1]
        most_num_list = [k for k, v in most.items() if v == most_value]
        time = (most_value - 1) * (n + 1) + len(most_num_list)
        return max(time, len(tasks))


# @lc code=end

#%%


#%%
import collections
a = [1,2,3,4,5,1,1,1,2,2,2,3,3]
count = collections.Counter(a)
print(count)
most = count.most_common()
print(most)
nums_most = len([i for i, v in count.items() if v == most])

# %%

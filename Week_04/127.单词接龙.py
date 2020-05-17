'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-17 15:12:01
@LastEditors: hu_xz
@LastEditTime: 2020-05-17 22:16:22
'''
#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict, step = set(wordList), 1
        s1, s2 = set([beginWord]), set([endWord])
        
        if endWord not in wordDict:
            return 0

        while s1:
            stack = set([])
            wordDict -= s1

            for s in s1:
                for i in range(len(s)):
                    for j in string.ascii_lowercase:
                        tmp = s[:i] + j + s[i+1:]
                        if tmp not in wordDict:
                            continue
                        elif tmp in s2:
                            return step + 1
                        else:
                            stack.add(tmp)    # {vocab}

            if len(stack) < len(s2):
                s1 = stack
            else:
                s1, s2 = s2, stack
            step += 1
        return 0


        
# @lc code=end



# %%


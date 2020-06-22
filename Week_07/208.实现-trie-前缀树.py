'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-07 17:34:00
@LastEditors: hu_xz
@LastEditTime: 2020-06-19 14:25:10
'''
#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
# 用dict模拟字典树
class Trie(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['end'] = True        
       
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return 'end' in node
       
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

#%%
## 通过创建树节点形式实现
import collections
class TrieNode:
    def __init__(self):
        self.data = collections.defaultdict(TrieNode)
        self.is_word = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for chars in word:
            child = node.data.get(chars)
            if not child:
                node.data[chars] = TrieNode()
            node = node.data[chars]
        node.is_word = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for chars in word:
            node = node.data.get(chars)
            if not node:
                return False
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for chars in prefix:
            node = node.data.get(chars)
            if not node:
                return False
        return True

word = 'apple'
obj = Trie()
obj.insert(word)
print(obj.root.data)
param_2 = obj.search(word)
print(param_2)

#%%
# dict.setfault vs dict.get: setdefault将新的键保存在字典中
info = {'name': 'jack', 'age': 18}
info.get('name')
print(info.get('add'))
print(info)
# 结果info={'name': 'jack', 'age': 18}
# %%
info = {'name': 'jack', 'age': 18}
info.setdefault('name')
print(info.setdefault('add'))
print(info)
# 结果info={'name': 'jack', 'age': 18, 'add': None}
# %%
class Trie(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
            print(self.root)
        # 最后给个结果一个True
        node['end'] = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return 'end' in node    
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True    

word = 'apple'
obj = Trie()
obj.insert(word)
print(obj.root)
param_2 = obj.search(word)
print(param_2)
# param_3 = obj.startsWith(prefix)

# %%

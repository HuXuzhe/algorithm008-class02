<!--
 * @Descripttion: 
 * @version: 3.X
 * @Author: hu_xz
 * @Date: 2020-04-12 20:45:53
 * @LastEditors: hu_xz
 * @LastEditTime: 2020-04-19 01:01:16
 -->
# 学习笔记

## 1. 数组（Array）

### 1.1 定义

Java,c++: int a[100];

Python: list=[]  # 可以直接定义一个数组，也称列表

```python
list_1 = [1,2,3,4]
print(list_1)
```

### 1.2 时间复杂度

- 连续的内存空间，支持随机访问，时间复杂度$O(1)$
- insert、delete操作低效，平均时间复杂度$O(n)$

|        操作        | 时间复杂度 |
| :----------------: | :--------: |
| prepend(最前添加)  |  $O(n)$  |
|  append(最后添加)  |  $O(1)$  |
| lookup(查询，搜索) |  $O(1)$  |
|    insert(插入)    |  $O(n)$  |
|    Delete(删除)    |  $O(n)$  |

### 1.3 优缺点

优点：

- 地址连续，访问任意一项都是常数级别$O(1)$时间复杂度

缺点：

- 删除，添加元素时间复杂度高，一般为$O(n)$
- insert前需要保证数组的size足够，否则需要扩容，拷贝等低效操作

## 2. 链表
链表由表头和结点组成，节点分为数据域和指针域，数据域中存储数值，指针域中存储下一个结点的地址

### 2.1 单链表实现逻辑
1. 创建结点类Node和链表类Linklist，Linklist类中包含head属性，head的值为0或Node对象，Node类中包含Value属性存储数据，next属性存储下个节点的地址(Node对象)
2. 循环节点从head开始取next属性，直到next=0为止，返回当前对象
3. 添加节点时调用循环方法返回最后节点对象，把返回节点的next改为当前Node对象，如当前没有节点，则Linklist实例的head属性修改为当前Node对象
4. 删除节点时把前一个节点的next属性修改为后一个节点的Node对象，如果当前节点是最后一个对象
```python
## 单链表
class Node():
    """定义节点类Node"""
    def __init__(self, value=None, pnext=None):
        """
        value: 节点保存的数据
        _next: 保存下一个节点对象
        """
        self.value = value
        self._next = pnext
    # 打印一个实例化对象时，打印的其实是一个对象的地址；
    # 通过__str__（）函数可以打印对象中的具体属性值
    def __str__(self):
        return "Node:{}".format(self.value)

class LinkdeList():
    """
    定义链表类
    """
    def __init__(self):
        self.root = Node()  # 链表头(即head节点)
        self.size = 0  # 链表的长度
        self.next = None  # 增加新数据时，将新数据的地址与其关联

    def append(self, value):
        node = Node(value)
        # 判断是否已经有数据
        if not self.next:  # 如果没有节点时
            self.root._next = node  # 将新节点挂到root后面
        else:
            self.next._next = node  # 将新节点挂到最后一个节点上
        self.next = node  # 保存
        self.size += 1 
    
    def append_first(self, value):
        node = Node(value)  # 初始化节点
        if not self.next:
            self.root.next = node
            self.next = node
        else:
            temp = self.root._next  # 获取原来root 后面的那个节点
            self.root._next = node  # 将新的节点挂到root上
            node._next = temp  # 新的节点的下一个节点是原来的root后的节点
        self.size += 1

    def __iter__(self):
        current = self.root._next
        if current:
            while current is not self.next:
                yield current.value  # yiedl相当于return，返回一个值
                current = current._next
            yield current.value
    
    def find(self, value):
        for v in self.__iter__():
            if v == value:
                return True

    def find2(self, value):
        current = self.root._next
        if current:
            while current is not self.next:
                if current.value == value:
                    return current
                current = current._next
        
    def remove(self, value):
        current = self.root._next
        if current:
            while current is not self.next:
                if current.value == value:
                    temp.next = current._next
                    del current
                    self.size -= 1
                    return True
                temp = current    
                current = current._next
        


if __name__ == "__main__":
    link = LinkdeList()
    link.append('孙悟空')
    link.append('猪八戒')
    link.append_first('唐僧')
    for v in link:
        print(v)
    print(link.find('孙悟空'))
    print(link.find('六耳猕猴'))
    print(link.find2('孙悟空'))
    print(link.find2('六耳猕猴'))
    print(link.remove('孙悟空'))
```
结果
```python
唐僧
孙悟空
猪八戒
True
None
Node:孙悟空
None
True
```
### 2.2 双链接
与单链表不同，每个节点既保存了指向下一个节点的指针，同时还保存了上一个节点的指针。
```python
class Node():
    def __init__(self, value=None, prev=None, pnext=None):
        self.value = value  # 赋值
        self.prev = prev
        self.next = pnext
    def __str__(self):
        return "Node:{}".format(self.value)

class DoubleLinkedList():
    def __init__(self):
        self.root = Node()  # 根节点
        self.size = 0
        self.end = None

    def append(self, value):
        node = Node(value)  # 封装节点对象
        # 判断是否有数据
        if not self.end:  # 如果没有元素/节点
            self.root.next = node
            node.prev = self.root  # 设置新节点的上一个节点为root
        else:
            self.end.next = node  
            node.prev = self.end  # 设置新节点的上一个节点为原来的最后一个节点
        self.end = node  # 更新最后一个节点为新加的节点
        self.size += 1
        
    def append_first(self, value):
        node = Node(value)
        if not self.end:
            self.end = node  # 更新最后一个节点为新加的node节点
        else:
            temp = self.root.next  # 保存原来的第一个节点
            node.next = temp  # 设置新节点的下一个节点为原来的第一个节点
            temp.prev = node  # 更新原来的第一个节点的上一个节点位置为新的node节点
        
        node.prev = self.root  # 设置新节点的上一个节点为root
        self.root.next = node  # 将root的下一个节点设置为新的node节点
        self.size += 1

    def __iter__(self):
        current = self.root.next
        if current:
            while current is not self.end:
                yield current.value
                current = current.next
            yield current.value
    
    def revers_iter(self):
        current = self.end  # 获取最后一个节点
        if current:
            while current is not self.root:
                yield current
                current = current.prev
if __name__ == "__main__":
    link = DoubleLinkedList()
    link.append('孙悟空')
    link.append('猪八戒')
    link.append_first('唐三藏')
    for v in link:
        print(v)
    print('-'*30)
    for v in link.revers_iter():
        print(v)
```

结果：
```
唐三藏
孙悟空
猪八戒
------------------------------
Node:猪八戒
Node:孙悟空
Node:唐三藏
```


# 4. 实战练习步骤

1. 5～10分钟：读题+思考
2. 有思路，自己开始做和coding；否则，马上看题解
3. 默写背诵、熟练
4. 开始自己写（闭卷）
5. ！！反馈
   - 看官方的解法，排序后的最优解法
   - 去国际站看dicuss，看解法
6. “五毒神掌”，过遍数，反复练习


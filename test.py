class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList():
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def length(self):
        count = 0
        start = self.head
        if self.head == None:
            return 0
        
        while(True):
            start = start.next
            count +=1
            if start == None:
                return count

    def add(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            start = self.head
            while(True):                
                if start.next == None:
                    start.next=node
                    break
                start = start.next
    
    def delete(self):
        if self.head == None:
            return False
        else:
            start = self.head
            if start.next == None:
                self.head = None
                return print(start.data)
            while(True):               
                temp = start
                start = start.next
                if start.next == None:
                    temp.next=None
                    return print(start.data)
    
    def search(self,index):
        if index >= self.length():
            return "Error"
        if index == 0:
            return  self.head.data   #代码逻辑与下面while 重复了
        start = self.head
        count=0
        while(True):
            if count == index:
                return index, start.data
            start = start.next
            count += 1
               
    def insert(self,index,data):
        '''指定位置插入元素'''
        node = Node(data)
        start = self.head
        count = 0
        length = self.length()
        if index >length:  #length = index+1 ，index 从0开始
           return False

        while(True):
            temp = start
            start = start.next
            count += 1
            if count == index:                
                if index != length:
                    node.next = temp.next
                temp.next=node
                return True
    
    def update(self,index,data):
        if index >= self.length():
            return "Error"
        start = self.head
        count=0
        while(True):
            if count == index:   ###找到了index位置
                start.data = data
                return True  ### 可以返回True
            start = start.next
            count += 1
               
    def display(self):
        start = self.head
        while(True):
            print(start.data)  
            start=start.next
            if start==None:
                break
                         

    
# node1 = Node(1)
# node2 = Node(2)

linklist = LinkList()

# linklist.head = node1

# node1.next= node2

linklist.add(1)

linklist.add(2)

linklist.add(3)



print("判断是否为空：", linklist.is_empty())
print("长度：",linklist.length())
print("查找：",linklist.search(1))
print("打印列表：")
linklist.display()
print("插入：",linklist.insert(1,8))
print("打印列表：")
linklist.display()
print("插入后：",linklist.search(1))
print("打印列表：")
linklist.display()
print("更新：",linklist.update(2,888))
print("打印列表：")
linklist.display()
print("更新后：",linklist.search(2))


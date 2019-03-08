import string
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc=True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        #Сравнение двух элементов 
        if v1<v2:
            return -1
        elif v1==v2:
            return 0
        else:
            return 1 
    
    def len(self):
        # Метод класса Ordered list определяющий кол-во элементов 
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l

    def print_all_nodes(self):
    # Метод класса DLL, позволяющий вывести э-ты DLL 
        node=self.head
        while node!=None:
            print(node.value,node.prev,node.next,'вывод print all nodes')
            node=node.next

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.next=None
            self.prev=None
        else:
            self.tail.next = item
            item.prev=self.tail
        self.tail = item

    def add(self, value):
        # Добавление элемента и последущая сортировка элементов списка
        value_node=Node(value)
        self.add_in_tail(value_node)
        node=self.head
        data=[]
        while node is not None:
            data.append(node.value)
            node=node.next
        if self.__ascending==True:
            for i in range(len(data)-1):
                for j in range(len(data)-i-1):
                    if self.compare(data[j],data[j+1])!=-1:
                        data[j], data[j+1]=data[j+1],data[j]
        elif self.__ascending==False:
            for i in range(len(data)-1):
                for j in range(len(data)-i-1):
                    if self.compare(data[j],data[j+1])!=1:
                        data[j], data[j+1]=data[j+1],data[j]
        for k in range(len(data)):
            self.delete(data[k])
        for k in range(len(data)):
            node_for_ordered_list=Node(data[k])
            self.add_in_tail(node_for_ordered_list)

    def find(self, val):
        # Метод класса LL, реализующий поиск по значению с учетом признака упорядоченности и прерыванием если найдено меньшие или большие значение
        node = self.head
        if self.__ascending==True:     
            while node is not None:
                if node.value >= val:
                    return node
                node = node.next
            return None
        elif self.__ascending==False:     
            while node is not None:
                if node.value <= val:
                    return node
                node = node.next
            return None

    def delete(self, val):
        # Метод удаления значения из OLL
        node = self.head
        while node is not None:
            if (self.len()==1):
                node=None
                self.head=None
                self.tail=None
                break
            elif (node.value==self.head.value) and (node.value==val) and (self.len()!=1):
                new_head=node.next
                new_head.prev=None
                self.head=new_head
                break
            elif (node.value == val) and (self.tail!=node) and (self.len()!=1):
                node_next=node.next
                node_pr.next=node.next
                node_next.prev=node_pr
                break
            elif (node==self.tail) and (node.value==val):
                self.tail=node_pr
                node_pr.next=None
                break
            if node.value!=val:
                node_pr=node
            node=node.next

    def clean(self, asc):
        #Очистка списка и установка параметра asc
        self.__ascending = asc
        node=self.head
        while node is not None:
            node.value=None
            node_pr=node
            node=node.next
            node_pr.next=None
            node_pr.prev=None
        self.head=None
        self.tail=None

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):

    def __init__(self, asc=True):
        super(OrderedStringList,self).__init__()
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        #Переопределённая версия для сравнения строк
        v1=str(v1)
        v2=str(v2)
        for i in range(0,len(v1)):
            if v1[i]==" ":
                pass
            else: 
                break
        for j in range(0,len(v2)):
            if v2[j]==" ":
                pass
            else: 
                break
        for k in range(0,i):
            v1=v1.lstrip()
        for l in range(0,j):
            v2=v2.lstrip()
        i=0
        j=0
        k=0
        l=0
        for i in range(0,len(v1)):
            if v1[i]==" ":
                break
            else:
                pass
        for j in range(0,len(v2)):
            if v2[j]==" ":
                break
            else:
                pass
        lenv1=len(v1)
        lenv2=len(v2)
        for k in range(i,lenv1):
            v1=v1.rstrip()
        for l in range(j,lenv2):
            v2=v2.rstrip()   
        if v1<v2:
            return -1
        elif v1==v2:
            return 0
        else:
            return 1     
    
"""a=OrderedList()
a.add(6)
a.add(599)
a.add(4)
a.print_all_nodes()
a.clean(False)
a.add(4)
a.add(599)
a.add(67)
a.print_all_nodes()
a.add(80)
a.add(9)
a.add(8)
a.add(5)
a.add(1)
a.print_all_nodes()
a.clean(True)
print("#####################################")
a.add(6)
a.add(20)
a.add(9)
print(a.head,a.tail,a.head.value,a.tail.value)
a.add(8)
print(a.head,a.tail,a.head.value,a.tail.value)
a.add(5)
print(a.head,a.tail,a.head.value,a.tail.value)
a.add(3)
print(a.head,a.tail,a.head.value,a.tail.value)
a.add(4)
print(a.head,a.tail,a.head.value,a.tail.value)
a.print_all_nodes()
"""

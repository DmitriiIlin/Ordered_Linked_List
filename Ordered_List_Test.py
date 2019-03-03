import Ordered_List, unittest, random

def random_number():
    i=random.randint(0,10**6)
    return i

def Node_create(i):
    Node=Ordered_List.Node(i)
    return Node

def massive_create(i):
    massive=[]
    for j in range(0,i):
        massive.append(random_number())
    return massive
    
def ordered_massive(massive,order=True):
    massive_len=len(massive)
    if order==True:
        for i in range(massive_len-1):
            for j in range(massive_len-i-1):
                if massive[j]>massive[j+1]:
                    massive[j], massive[j+1]=massive[j+1], massive[j]
    elif order==False: 
        for i in range(massive_len-1):
            for j in range(massive_len-i-1):
                if massive[j]<massive[j+1]:
                    massive[j], massive[j+1]=massive[j+1], massive[j]
    return massive

class Ordered_Linked_Tests(unittest.TestCase):
    # Тесты для класса Ordered_Linked_List
    
    def test_add (self):
        # Тест на добавление элемента
        OLL_1=Ordered_List.OrderedList()
        first=random_number()
        OLL_1.add(first)
        Node_OLL_1=OLL_1.head
        self.assertEqual(Node_OLL_1.value,first)
        OLL_2=Ordered_List.OrderedList()
        massive=massive_create(10)
        for i in range(0,10):
            OLL_2.add(massive[i])
        OLL_2.print_all_nodes()
        massive=ordered_massive(massive)
        print(massive)
        Node_OLL_2=OLL_2.head
        for i in range(0,10):
            print(Node_OLL_2.value,massive[i])
            self.assertEqual(Node_OLL_2.value,massive[i])
            Node_OLL_2=Node_OLL_2.next
        OLL_2.clean(False)
        for i in range(0,10):
            OLL_2.add(massive[i])
        massive=ordered_massive(massive,False)
        Node_OLL_2=OLL_2.head
        for i in range(0,10):
            print(Node_OLL_2.value,massive[i])
            self.assertEqual(Node_OLL_2.value,massive[i])
            Node_OLL_2=Node_OLL_2.next
        
    def test_delete (self):
        #Тест на удаление элемента
        OLL_1=Ordered_List.OrderedList()
        first=random_number()
        OLL_1.add(first)
        OLL_1.delete(first)
        Node_OLL_1=OLL_1.head
        self.assertEqual(Node_OLL_1,None)
        OLL_2=Ordered_List.OrderedList()
        massive=massive_create(10)
        for i in range(0,10):
            OLL_2.add(massive[i])
        massive=ordered_massive(massive)
        j=random.randint(0,9)
        delete_el=massive[j]
        massive.pop(j)
        OLL_2.delete(delete_el)
        Node_OLL_2=OLL_2.head
        for i in range(0,len(massive)):
            print(Node_OLL_2.value,massive[i])
            self.assertEqual(Node_OLL_2.value,massive[i])
            Node_OLL_2=Node_OLL_2.next
    
    def test_find (self):
        #Тест на поиск элемента
        OLL_2=Ordered_List.OrderedList()
        massive=massive_create(10)
        for i in range(0,10):
            OLL_2.add(massive[i])
        massive=ordered_massive(massive)
        j=random.randint(0,9)
        finded_el=massive[j]
        self.assertEqual(OLL_2.find(finded_el).value,finded_el)



        





if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()

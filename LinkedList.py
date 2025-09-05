class LinkedList:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def Traversal(head):
    while head:
        print(f"{head.val} ")
        head = head.next

        
def append(head,value):
    new_node = LinkedList(value)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head


def prepend(head,val):
    new_node = LinkedList(val)
    if not head :
        return new_node
    else :
        new_node.next = head
        return new_node


def index_at_position(head, index, value):
    if index ==0:
        return prepend(head,value)
    
    new_node = LinkedList(value)
    temp = head
    pos = 0
    
    while temp and pos<index-1:
        temp = temp.next
        pos+=1
    
    if not temp:  # Index out of range
        print("Index out of range!")
        return head
    
    new_node.next = temp.next
    temp.next = new_node
    return head

    
    return head
    
    
class CircularLinkedList:
    def __init__(self,hdata=0,next=None):
        self.hdata = hdata
        self.next = next
 
def Traversal_Circular(head):
    if not head:
        return
    temp = head
    while True:
        print(f"{temp.hdata} ")
        temp = temp.next
        if temp == head:
            break        

def append_circular(head,data):
    new_node = CircularLinkedList(data)
    if not head:
        return new_node
    temp = head
    while temp.next!=head:
        temp = temp.next
    temp.next = new_node
    new_node.next = head
    
    return head
        


class DoublyLinkedList:
    def __init__(self,val=0,next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    

a = LinkedList(10)
b = LinkedList(20)
c = LinkedList(30)
d = LinkedList(40)


a.next = b
b.next = c
c.next = d

print("Original List:")
Traversal(a)

print("\nInsert at index 2 (value 60):")
a = index_at_position(a, 2, 60)
Traversal(a)

print("\nAppend 50:")
a = append(a, 50)
Traversal(a)

print("\nPrepend 1:")
a = prepend(a, 1)
Traversal(a)

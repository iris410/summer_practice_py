

class Node:

    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class MyLinkedList():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        curr = self.head.next
        curr_index = 0

        while(curr != self.tail):
            if curr_index == index:
                return curr.value
            curr_index += 1
            curr = curr.next

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = Node(val)
        tem = self.head.next
        self.head.next = new
        new.prev = self.head
        new.next = tem
        tem.prev = new
        return

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new = Node(val)
        tem = self.tail.prev
        self.tail.prev = new
        new.next = self.tail
        new.prev = tem
        tem.next = new
        return

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self.head.next
        curr_index = 0
        while(curr != self.tail):
            if curr_index == index:
                #insert
                new = Node(val)
                tem = curr.prev
                new.next = curr
                curr.prev = new
                tem.next = new
                new.prev = tem
                return
            curr = curr.next
            curr_index += 1
        #if curr = self.tail
        if curr_index == index:
            #insert
            new = Node(val)
            tem = curr.prev
            new.next = curr
            curr.prev = new
            tem.next = new
            new.prev = tem
            return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return -1
        curr_index = 0
        curr = self.head.next
        while(curr != self.tail):
            if curr_index == index:
                tem_p = curr.prev
                tem_n = curr.next
                tem_n.prev = tem_p
                tem_p.next = tem_n
                return
            curr = curr.next
            curr_index += 1



        








# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#You have a linked list and want to find the kth to last node.

#Write a function kth_to_last_node() that takes an integer k and the head_node of a singly-linked list, and returns the kth to last node in the list.

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e 

#Returns the node with value "Devil's Food" (the 2nd to last node)

def kth_to_last_node(k, head_node):
    
    if k < 1:
        raise ValueError('Invalid input')

    current_node = head_node

    counter = 0
    
    while current_node is not None:
        counter += 1
        current_node = current_node.next

    index_nth_node = counter - k
    nth_node = head_node 

    while index_nth_node >= 0:
        nth_node = head_node.next 
        index_nth_node -= 1
    
    return nth_node


print(kth_to_last_node(2, a))

    

    

    



    


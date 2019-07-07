#DELETING A NODE

#Delete a node from a singly-linked list, given only a variable pointing to that node

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

        

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c 

def delete_node(node_to_delete):
    next_node = node_to_delete.next

    if next_node:
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    
    else:
        raise Exception("Can't delete the last node with this technique!")

delete_node(LinkedListNode('B'))



#CHECK IF SINGLY-LINKED LIST CONTAINS A CYCLE

#Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

        

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('B')

a.next = b
b.next = c 
c.next = d

def contains_cycle(first_node):
    
    slow_runner = first_node
    fast_runner = first_node

    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if fast_runner is slow_runner:
            return True
    
    return False 





    
    

contains_cycle(LinkedList('A'))

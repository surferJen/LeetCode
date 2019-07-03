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

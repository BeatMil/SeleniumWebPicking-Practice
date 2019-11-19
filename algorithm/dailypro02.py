# reverse linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next
    
    def reverse(self):
        array = []
        node = self
        while node != None:
            array.append(node.data)
            node = node.next
        array.reverse()
        print(array)
n1 = node(1)
n2 = node(2)
n3 = node(3)
n1.next = n2
n2.next = n3
n1.traverse()
n1.reverse()
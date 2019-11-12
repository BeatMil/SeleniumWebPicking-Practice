class node:
    def __init__(self,data):
        self.current_val = data
        self.next_val = None
    
    def traverse(self):
        node = self
        while node != None:
            print(node.current_val)
            node = node.next_val

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    while l1:
         
    # node_result =
    pass


node1 = node(2)
node1.next_val = node(4)
node1.next_val.next_val = node(3)

node2 = node(5)
node2.next_val = node(6)
node2.next_val.next_val = node (4)


# node1.traverse()
# node2.traverse()
result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8
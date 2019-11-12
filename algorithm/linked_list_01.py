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
    check_val_helper = False

    copy1 = l1
    copy2 = l2

    l1_lenght = 0
    l2_lenght = 0
    # len the node
    while copy1 and copy2:
      l1_lenght += 1
      l2_lenght += 1
      copy1 = copy1.next_val
      copy2 = copy2.next_val
    while l1 and l2:
      if c == 0:
        node_result = node(l1.current_val + l2.current_val)
      elif c == 1:
        check_val = l1.current_val + l2.current_val
        if check_val >= 10:
          node_result.next_val = node(check_val - 10)
          check_val_helper = True
        else:
          node_result.next_val = node(l1.current_val + l2.current_val) 
      elif c == 2:
        if check_val_helper:
          node_result.next_val.next_val = node(l1.current_val + l2.current_val)

        node_result.next_val.next_val = node(l1.current_val + l2.current_val)
      
      l1 = l1.next_val
      l2 = l2.next_val
      c += 1
    return node_result

node1 = node(2)
node1.next_val = node(4)
node1.next_val.next_val = node(3)

node2 = node(5)
node2.next_val = node(6)
node2.next_val.next_val = node (4)


# node1.traverse()
# node2.traverse()
result = Solution().addTwoNumbers(node1, node2)
while result:
  print(result.current_val)
  result = result.next_val
# 7 0 8
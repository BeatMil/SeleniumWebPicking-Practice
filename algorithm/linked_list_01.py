class node:
    def __init__(self,data):
        self.current_val = data
        self.next_val = None

fish = node(5)
print(fish.current_val)

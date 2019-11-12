class human:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def boost_age(self, amount):
        self.age += amount

# beat = human("Beat", 20)
# print(beat.age)
# beat.boost_age(200)
# print(beat.age)

w = input("weight pls")
h = input("height pls")
print(w/h)
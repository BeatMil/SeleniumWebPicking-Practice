from bob import Bob
# input can be only within an array
input_choices = ["a","b","c"]

def inputChecker(array, prompt):
    user_input = input(prompt)
    for i in array:
        if user_input.lower() == i:
            print("Good to go")
            break
    print("Please try again.")

p1 = Bob()
p2 = Bob()
print(p1.name)
print(p2.name)
p1.change_name("Jin")
p2.change_name("BUB")
print(p1.name)
print(p2.name)    
    

# inputChecker(input_choices, "PASSWORD: ")
import bob
# input can be only within an array
input_choices = ["a","b","c"]

def inputChecker(array, prompt):
    user_input = input(prompt)
    for i in array:
        if user_input.lower() == i:
            print("Good to go")
            break
    print("Please try again.")

p1 = bob.Bob()
print(p1.name)
    
    

# inputChecker(input_choices, "PASSWORD: ")
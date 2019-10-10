
print("------------TESTING TRY EXCEPT WITH VARIABLE------------")


# name = input("Insert name: ").capitalize()

# if name.isalpha:
#     print("alpha")

# print(name)


try:
    name = 'beat'
    age = 21
    print(name+age)
except:
    print("str and int cannot add to gether.")

print(name)
print("Hello, %s!" % name)
import os

# with open("pass.txt", "r") as file:
#     file.readlines();
def get_login():
    with open('pass.txt', 'r') as file: 
        array = file.readlines()
        array[0] = array[0][:-1]
        return array

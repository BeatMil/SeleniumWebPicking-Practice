def calculate(ex):
    open_bracket_index = []
    close_bracket_index = []
    for i in range(len(ex)):
        if ex[i] == "(":
            open_bracket_index.append(i)
        elif ex[i] == ")":
            close_bracket_index.append(i)
    first = ex[open_bracket_index[0] + 1:close_bracket_index[0]]
    array = first.split()
    if array[1] == '-':
        first_result = int(array[0]) - int(array[2])
    elif array[1] == '+':
        first_result = int(array[0]) - int(array[2])
    print(first_result)
ex = '-(3 - 1) + 3'
calculate(ex)
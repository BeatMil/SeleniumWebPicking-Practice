array_int = [1,100,50,23,66,55,32,31,16,18]
# my bmi 21.00767
# array_int.sort()
def swap_front(array):
    for j in range(len(array) - 1):
        for i in range(len(array)):
            if i < len(array)-1:
                if array_int[i] > array_int[i+1]:
                    temp = array_int[i]
                    array_int[i] = array_int[i+1]
                    array_int[i+1] = temp

swap_front(array_int)
print(array_int)

# merge_sort
def merge_sort(arr):
    for i in range(int(len(arr))):
        if i < len(arr) - 1:
            if arr[i] > arr[i+1]: 
                box = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = box




arr = [4,2,3,1]
merge_sort(arr)
print(arr)
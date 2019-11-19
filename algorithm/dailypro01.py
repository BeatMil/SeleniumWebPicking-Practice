# list near index
class Solution: 
  def getRange(self, arr, target):
    cut_helper = True
    for i in range(len(arr)):
        if arr[i] == target and cut_helper:
                new_arr = [i]
                cut_helper = False
        elif arr[i] != target and not cut_helper:
            new_arr.append(i - 1)
            break
    return new_arr


        

  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
arr2 = [1,1,1,2,3,4,4,4,5,6,6,7,7,7,8,8]
x = 8
print(Solution().getRange(arr2, x))
# [1, 4]
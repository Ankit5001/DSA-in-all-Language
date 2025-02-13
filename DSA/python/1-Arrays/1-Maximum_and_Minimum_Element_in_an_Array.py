''' Given an array of size N. The task is to find the maximum and
    the minimum element of the array using the minimum number of comparisons.

Examples:
Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
        Maximum element is: 9
Input: arr[] = {22, 14, 8, 17, 35, 3}
Output: Minimum element is: 3
        Maximum element is: 35   '''

array1 = [3, 5, 4, 1, 9]
array2 = [22, 14, 8, 17, 35, 3]
def get_min_max(array):
    Min , Max = float('inf'),float('-inf')
    for i in array:
        Min , Max = min(Min,i),max(Max,i)
    return Min, Max
    
print(get_min_max(array1))
print(get_min_max(array2))
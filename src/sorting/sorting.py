# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    left, right = 0, 0
    index = 0
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr[index] = arrA[left]
            left += 1
        else:
            merged_arr[index] = arrB[right]
            right += 1
        index += 1
    while left < len(arrA):
        merged_arr[index] = arrA[left]
        left += 1
        index += 1
    while right < len(arrB):
        merged_arr[index] = arrB[right]
        right += 1
        index += 1
        

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) > 1:
        # move toward base case
        # split the arr into two
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # call mergesort on both arrays
        arrA = merge_sort(left)
        arrB = merge_sort(right)
        # merge the arrays
        arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


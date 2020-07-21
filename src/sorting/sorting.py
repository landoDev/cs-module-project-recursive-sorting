# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # while there are elements
        # if(arrA[0] > arrB[0]):
            # add b[0] to the end of merged_arr
            # remove arrB[0] from b
        #else:
            # add a[0] to merged arr
            # remove a[0] merged
    # while a has elements
        # a[0] add to merged
        # remove a[0] from merged
    # do the same for b
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    # if len(arr) == 1
        # return
    # move toward base case
    # split the arr into two
    # call mergesort on both arrays
    # merge the arrays



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


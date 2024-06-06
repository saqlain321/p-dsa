def quicksort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quicksort(left) + middle + quicksort(right)
    
#usage
arr = [10,9,8,7,4,5,1,0]
sorted = quicksort(arr)
print("Quick sorted array is : ", sorted)
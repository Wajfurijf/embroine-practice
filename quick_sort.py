def quick_sort(arr):
    #base condition of recursion
    if len(arr) <= 1:
        return arr 

    pivot=arr[len(arr)//2]
    #Dividing the array around the pivot by arranging all the elements smaller than the pivot on the left
    left=[x for x in arr if x < pivot]
    #All elements equal to the pivot are placed in the middle of the sorted array
    middle=[x for x in arr if x == pivot]
    #Dividing the array around the pivot by arranging all the elements greater than the pivot on the right
    right=[x for x in arr if x > pivot]
    
    #call the function recursively
    return quick_sort(left)+middle+quick_sort(right)

arr=list(map(int,input("Enter numbers with space: ").split()))
sorted_arr=quick_sort(arr)
print("Sorted array is:", sorted_arr)


    
    
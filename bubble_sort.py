myArray = [45,400,30,86,12,78,90,23,56,954,67,89,34,21]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1): 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
              
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr;

print("Unsorted Array:", myArray)
sortedArray = bubble_sort(myArray)
print("Sorted Array:", len(sortedArray))